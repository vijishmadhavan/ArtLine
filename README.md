# ArtLine
[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com)


[<img src="https://colab.research.google.com/assets/colab-badge.svg" align="center">](https://colab.research.google.com/github/vijishmadhavan/Light-Up/blob/master/ArtLine(Try_it_on_Colab).ipynb)

The main aim of the project is to create amazing line art portraits. 

**Sounds Intresting,let's get to the pictures!!**

![ArtLine](https://i.imgur.com/ittgYum.png)

## Highlights

- [Example Images](#Example-Images)
- [Cartoonize](#Cartoonize)
- [Movie Poster created using ArtLine](#Movie-Poster-created-using-ArtLine)
- [Technical Details](#Technical-Details)


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

bohemian rhapsody movie , Rami Malek American actor

![bohemian](https://i.imgur.com/od6IA08.jpg)

## Cartoonize

**Lets cartoonize the lineart portraits, its still in the making but have a look at some pretty pictures.**

Skrillex , American DJ

![Imgur](https://i.imgur.com/BJW8beC.jpg)

Tom Hanks, Actor

![Imgur](https://i.imgur.com/hvkDTZR.jpg)


## Line Art

The amazing results that the model has produced has a secret sauce to it. The initial model couldn't create the sort of output I was expecting, it mostly struggled with recognizing facial features. Even though (https://github.com/yiranran/APDrawingGAN) produced great results it had limitations like (frontal face photo similar to ID photo, preferably with clear face features, no glasses and no long fringe.) I wanted to break-in and produce results that could recognize any pose. Achieving proper lines around the face, eyes, lips and nose depends on the data you give the model. APDrawing dataset alone was not enough so I had to combine selected photos from Anime sketch colorization pair dataset. The combined dataset helped a bit, but nothing impressive. So here comes the idea of **"blended dataset"**.

The success came in with the idea of generating a blended dataset, i.e. to combine the pair. I did not find any paper or projects doing it, the idea is kind of giving a hint to the model to recognize what's what!!. This secret sauce helped in fixing the issue and generating wonderful output. 

## Movie Poster created using ArtLine.

The movie poster was created using ArtLine in no time , it's not as good as it should be but I'm not an artist.

![Poster](https://i.imgur.com/RvTTxdI.jpg)


## Technical Details

* **Self-Attention Generative Adversarial Network** (https://arxiv.org/abs/1805.08318). Generator is pretrained UNET with spectral normalization and self-attention. Something that I got from Jason Antic's DeOldify(https://github.com/jantic/DeOldify), this made a huge difference, all of a sudden I started getting proper details around the facial features.

* **Progressive Growing of GANs** (https://arxiv.org/abs/1710.10196). Progressive GANS takes this idea of gradually increasing the image size, In this project the image size were gradually increased and learning rates were adjusted. Thanks to fast.ai for intrdoucing me to Progressive GANS, this helped in generating high quality output.

* **Generator Loss** :  Perceptual Loss/Feature Loss based on VGG16. (https://arxiv.org/pdf/1603.08155.pdf).

**Surprise!! No critic,No GAN. GAN did not make much of a difference so I was happy with No GAN.**

The mission was to create something that converts any personal photo into a line art. The initial efforts have helped to recognize lines, but still the model has to improve a lot with shadows and clothes. All my efforts are to improve the model and make line art a click away.

![Imgur](https://i.imgur.com/fhUi3uv.jpg)

## Dataset

[APDrawing dataset](https://cg.cs.tsinghua.edu.cn/people/~Yongjin/APDrawingDB.zip) 

Anime sketch colorization pair dataset

APDrawing data set consits of mostly close-up portraits so the model would struggle to recogonize cloths,hands etc. For this purpose selected images from Anime sketch colorization pair were used.


## Going Forward

I hope I was clear, going forward would like to improve the model further as it still struggles with random backgrounds(I'm creating a custom dataset to address this issue). Cartoonizing the image was never part of the project, but somehow it came up and it did okay!! Still lots to improve. Ill release the cartoonize model when it looks impressive enough to show off.

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

- I'm not a coder, bear with me for the bad code and documentation. Will make sure that I improve with upcoming updates.

### Updates

[Get more updates on Twitter](https://twitter.com/Vijish68859437)

Mail me @ vijishmadhavan@gmail.com

### Acknowledgments

- The code is inspired from Fast.AI's Lesson 7 and DeOldify (https://github.com/jantic/DeOldify), Please have look at the Lesson notebook (https://github.com/fastai/course-v3/blob/master/nbs/dl1/lesson7-superres-gan.ipynb)

- Thanks to (https://github.com/yiranran/APDrawingGAN) for the amazing dataset.

## License

All code in this repository is under the MIT license as specified by the LICENSE file.





