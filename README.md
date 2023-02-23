# ArtLine

**You can sponsor me to support my open source work 💖 [sponsor](https://github.com/sponsors/vijishmadhavan?o=sd&sc=t)**

The main aim of the project is to create amazing line art portraits. 

# Exciting update

#### ControlNet + ArtLine for portraits, Try colab!!

[<img src="https://colab.research.google.com/assets/colab-badge.svg" align="center">](https://colab.research.google.com/github/vijishmadhavan/ArtLine/blob/main/ControlNet_%2BArtLine_.ipynb)


## ControlNet + ArtLine

The model is designed to take in a portrait image and a corresponding written instruction, and then use that instruction to adjust the style of the image.


![model](https://i.imgur.com/QNCw4CN.jpg)

![model](https://i.imgur.com/jJuF3UN.jpg)

![model](https://i.imgur.com/zizgSTf.jpg)

![Shahrukh](https://i.imgur.com/WvKsYXj.jpg)


## Highlights

- [Example Images](#Example-Images)
- [Cartoonize](#Cartoonize)
- [Movie Poster created using ArtLine](#Movie-Poster-created-using-ArtLine)
- [Technical Details](#Technical-Details)


## Example Images

bohemian rhapsody movie , Rami Malek American actor

![bohemian](https://i.imgur.com/od6IA08.jpg)



Photo by Maxim from Pexels

![Imgur](https://i.imgur.com/yksAvUq.jpg)


Keanu Reeves, Canadian actor.

![Keanu](https://i.imgur.com/labkc8V.jpg)

Photo by Anastasiya Gepp from Pexels

![Imgur](https://i.imgur.com/xWEUK7W.jpg)

Interstellar

![Interstellar](https://i.imgur.com/xiuwDGd.jpg)

Pexels Portrait, Model

![Imgur](https://i.imgur.com/NMaPOiE.jpg)

Beyoncé, American singer

![Beyoncé](https://i.imgur.com/QalvHKS.jpg)


**Model-(Smooth)**

[<img src="https://colab.research.google.com/assets/colab-badge.svg" align="center">](https://colab.research.google.com/github/vijishmadhavan/Light-Up/blob/master/ArtLine.ipynb)


**Model-(Quality)**

[<img src="https://colab.research.google.com/assets/colab-badge.svg" align="center">](https://colab.research.google.com/github/vijishmadhavan/Light-Up/blob/master/ArtLine(AR).ipynb)

[![Open in RunwayML Badge](https://open-app.runwayml.com/gh-badge.svg)](https://open-app.runwayml.com/?model=akhaliq/ArtLine)


**Click on the below image to know more about colab demo, credits to Bhavesh Bhatt for the amazing Youtube video.**

[![](https://i.imgur.com/ittgYum.png)](https://www.youtube.com/watch?v=ULqlp6Btk2w&t=324s)


## Line Art

The amazing results that the model has produced has a secret sauce to it. The initial model couldn't create the sort of output I was expecting, it mostly struggled with recognizing facial features. Even though (https://github.com/yiranran/APDrawingGAN) produced great results it had limitations like (frontal face photo similar to ID photo, preferably with clear face features, no glasses and no long fringe.) I wanted to break-in and produce results that could recognize any pose. Achieving proper lines around the face, eyes, lips and nose depends on the data you give the model. APDrawing dataset alone was not enough so I had to combine selected photos from Anime sketch colorization pair dataset. The combined dataset helped the model to learn the lines better.

## Movie Poster created using ArtLine.

The movie poster was created using ArtLine in no time , it's not as good as it should be but I'm not an artist.

![Poster](https://i.imgur.com/QuRnKjB.jpg)

![Poster](https://i.imgur.com/RvTTxdI.jpg)


## Technical Details

* **Self-Attention** (https://arxiv.org/abs/1805.08318). Generator is pretrained UNET with spectral normalization and self-attention. Something that I got from Jason Antic's DeOldify(https://github.com/jantic/DeOldify), this made a huge difference, all of a sudden I started getting proper details around the facial features.

* **Progressive Resizing** (https://arxiv.org/abs/1710.10196),(https://arxiv.org/pdf/1707.02921.pdf). Progressive resizing takes this idea of gradually increasing the image size, In this project the image size were gradually increased and learning rates were adjusted. Thanks to fast.ai for intrdoucing me to Progressive resizing, this helps the model to generalise better as it sees many more different images.

* **Generator Loss** :  Perceptual Loss/Feature Loss based on VGG16. (https://arxiv.org/pdf/1603.08155.pdf).

**Surprise!! No critic,No GAN. GAN did not make much of a difference so I was happy with No GAN.**

The mission was to create something that converts any personal photo into a line art. The initial efforts have helped to recognize lines, but still the model has to improve a lot with shadows and clothes. All my efforts are to improve the model and make line art a click away.

![Imgur](https://i.imgur.com/fhUi3uv.jpg)

## Dataset

[APDrawing dataset](https://cg.cs.tsinghua.edu.cn/people/~Yongjin/APDrawingDB.zip) 

Anime sketch colorization pair dataset

APDrawing data set consits of mostly close-up portraits so the model would struggle to recogonize cloths,hands etc. For this purpose selected images from Anime sketch colorization pair were used.


## Going Forward

I hope I was clear, going forward would like to improve the model further as it still struggles with random backgrounds(I'm creating a custom dataset to address this issue).

*I will be constantly upgrading the project for the foreseeable future.*

## Getting Started Yourself

The easiest way to get started is to simply try out on Colab: https://colab.research.google.com/github/vijishmadhavan/Light-Up/blob/master/ArtLine(Try_it_on_Colab).ipynb

### Installation Details

This project is built around the wonderful Fast.AI library.

- **fastai==1.0.61** (and its dependencies).  Please dont install the higher versions
- **PyTorch 1.6.0** Please don't install the higher versions

### Limitations

- Getting great output depends on Lighting, Backgrounds,Shadows and the quality of photos. You'll mostly get good results in the first go but there are chances for issues as     well. The model is not there yet, it still needs to be tweaked to reach out to all the consumers. It might be useful for "AI Artisits/ Artists who can bring changes to the final output.

- The model confuses shadows with hair, something that I'm trying to solve.

- It does bad with low quality images(below 500px).

- I'm not a coder, bear with me for the bad code and documentation. Will make sure that I improve with upcoming updates.

### Updates

[Get more updates on Twitter](https://twitter.com/Vijish68859437)

Mail me @ vijishmadhavan@gmail.com

### Acknowledgments

- The code is inspired from Fast.AI's Lesson 7 and DeOldify (https://github.com/jantic/DeOldify), Please have look at the Lesson notebook (https://github.com/fastai/course-v3/blob/master/nbs/dl1/lesson7-superres-gan.ipynb)

- Thanks to (https://github.com/yiranran/APDrawingGAN) for the amazing dataset.

## License

All code in this repository is under the MIT license as specified by the LICENSE file.
