# ArtLine

The main aim of the project is to create amazing lineart portraits and cartoonize it. 

Sounds Intresting,let's get to the pictures!


## Example Images

1984 photograph “Afghan Girl” by Steve McCurry.

![Afghan Girl](https://i.imgur.com/NDE3QW4.jpg)

A sadhu (holy man) in Varanasi, India by Joel Santos.

![sadhu](https://i.imgur.com/PXLTBbJ.jpg)

Keanu Reeves, Canadian actor.

![Keanu](https://i.imgur.com/labkc8V.jpg)

Gal Gadot, Israeli actress.

![Gal](https://i.imgur.com/bF91WY6.jpg)

Most Creative Facial Hair at the 2019 Beard and Moustache Championships.

![Beard](https://i.imgur.com/yNtwLCJ.jpg)

Model

![Model](https://i.imgur.com/RKTdhHc.jpg)

Virat Kohli, Indian cricketer

![Virat](https://i.imgur.com/jg76waU.jpg)

Taylor Swift, American singer.

![Taylor](https://i.imgur.com/oZzJqw5.jpg)

People's Sexiest Man Alive title  "Black Panther" star Michael B. Jordan.

![Michael](https://i.imgur.com/apAGk7M.jpg)

Natalie Portman, Actress.

![Natalie](https://i.imgur.com/pmaJ6fl.jpg)

V, South Korean singer-songwriter.

![V](https://i.imgur.com/egQRTYj.jpg)

## Cartoonize

**Lets cartoonize the lineart portraits, have a look at some pretty pictures.**

![Imgur](https://i.imgur.com/JQltbBH.jpg)
![Imgur](https://i.imgur.com/CBvaHN4.jpg)     
![Imgur](https://i.imgur.com/qMN2YcY.jpg)
![Imgur](https://i.imgur.com/whumnDY.jpg)
![Imgur](https://i.imgur.com/zjpLHQW.jpg)

## Technical Details

* **Self-Attention Generative Adversarial Network** (https://arxiv.org/abs/1805.08318). Generator is pretrained UNET with spectral normalization and self-attention.Something that I got from Jason Antic's DeOldify(https://github.com/jantic/DeOldify). I have to say this a made huge difference, all of a sudden I started getting proper details around the facial features.

* **Progressive Growing of GANs** (https://arxiv.org/abs/1710.10196). Progressive GANS takes this idea of gradually increasing the image size, In this project the image size were gradually increased and learning rates were adjusted. Thanks to fast.ai for intrdoucing me to Progressive GANS, this helped in generating high quality output.

* **Generator Loss** :  Perceptual Loss/Feature Loss based on VGG16. (https://arxiv.org/pdf/1603.08155.pdf).

**Surprise!! No critic,No GAN. GAN did not make much of a difference so I was happy with No GAN.**

## Dataset

[APDrawing dataset](https://cg.cs.tsinghua.edu.cn/people/~Yongjin/APDrawingDB.zip) 

Anime sketch colorization pair dataset

APDrawing data set consits of mostly close-up portraits so the model would struggle to recogonize cloths,hands etc. For this purpose selected images from Anime sketch colorization pair were used.






