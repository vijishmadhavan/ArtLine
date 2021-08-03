import runway
import numpy as np
import argparse
import torch
from torchvision import transforms
import os.path
import fastai
from fastai.vision import *
from fastai.utils.mem import *
from fastai.vision import open_image, load_learner, image, torch
import numpy as np
import urllib.request
from io import BytesIO
import torchvision.transforms as T
import requests
from io import BytesIO
import fastai
from fastai.vision import *
from fastai.utils.mem import *
from fastai.vision import open_image, load_learner, image, torch
import numpy as np
import urllib.request
from io import BytesIO
import torchvision.transforms as T
import PIL 

class FeatureLoss(nn.Module):
    def __init__(self, m_feat, layer_ids, layer_wgts):
        super().__init__()
        self.m_feat = m_feat
        self.loss_features = [self.m_feat[i] for i in layer_ids]
        self.hooks = hook_outputs(self.loss_features, detach=False)
        self.wgts = layer_wgts
        self.metric_names = ['pixel',] + [f'feat_{i}' for i in range(len(layer_ids))
              ] + [f'gram_{i}' for i in range(len(layer_ids))]

    def make_features(self, x, clone=False):
        self.m_feat(x)
        return [(o.clone() if clone else o) for o in self.hooks.stored]
    
    def forward(self, input, target):
        out_feat = self.make_features(target, clone=True)
        in_feat = self.make_features(input)
        self.feat_losses = [base_loss(input,target)]
        self.feat_losses += [base_loss(f_in, f_out)*w
                             for f_in, f_out, w in zip(in_feat, out_feat, self.wgts)]
        self.feat_losses += [base_loss(gram_matrix(f_in), gram_matrix(f_out))*w**2 * 5e3
                             for f_in, f_out, w in zip(in_feat, out_feat, self.wgts)]
        self.metrics = dict(zip(self.metric_names, self.feat_losses))
        return sum(self.feat_losses)
    
    def __del__(self): self.hooks.remove()



@runway.setup(options={'checkpoint': runway.file(extension='.pkl',description='checkpoint file')})
def setup(opts):
    path = Path(".")
    learn=load_learner(path, opts['checkpoint'])
    return learn


@runway.command('translate', inputs={'source_imgs': runway.image(description='input image to be translated'),}, outputs={'image': runway.image(description='output image containing the translated result')})
def translate(learn, inputs):
    img_t = T.ToTensor()(inputs['source_imgs'])
    img_fast = Image(img_t)
    p,img_hr,b = learn.predict(img_fast)
    return np.uint8(np.clip(image2np(img_hr), 0, 1)*255)


if __name__ == '__main__':
    runway.run(port=8889)

