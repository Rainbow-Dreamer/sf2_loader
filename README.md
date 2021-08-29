# sf2_loader
This is an easy-to-use soundfonts loader and audio renderer in python.

This is probably the most handy soundfont loader and renderer via pure programming at the time I am writing now (2021/8/29). This is a python package, it can load any soundfont files, including sf2 and sf3, you can listen to every preset in every bank in the soundfont files that are loaded using very simple syntax, export audio files for each note in a pitch range for any instruments in the soundfont files, export the whole piece of music as audio files with custom audio effects, and the loader could accpet loading as much soundfont files as you can. For more functionalities that this soundfont loader provides, please continue reading.

This sf2 loader is heavily combined with [musicpy](https://github.com/Rainbow-Dreamer/musicpy), which is one of my most popular project, focusing on music programming and music analysis and composition. If you have already learned how to use musicpy to build notes, chords and pieces, you can straightly pass them to the sf2 loader and let it play what you write. Besides of playing music with the loaded soundfonts files, I also write an audio renderer in the sf2 loader, which could render the audio from the loaded soundfont files with the input musicpy data structures and output as audio files, you can choose the output format, such as wav, mp3, ogg, and output file names, sample width, frame rate, channels and so on.

If you are not familiar with musicpy data structures and is not willing to learn it in recent times, you can also straightly using midi files as input to the sf2 loader, and export the rendered audio files using the loaded soundfont files. However, I still recommend you to learn about musicpy, even not to consider music programming and analysis, it could also be very useful for midi files editing and reconstructing. But if you want to change the instruments for some of the tracks or even with different soundfont files in the midi files, you will need to do it in the DAW or using musicpy to load midi files as a piece instance.

This sf2 loader is compatible with both 32-bit and 64-bit python versions, for python >= 3.6, so be sure your installed python version match the requirements for this package to use.



## Installation

You can use pip to install this sf2 loader.

Run this line in cmd/terminal to install.

```python
pip install sf2_loader
```



## Usage

Here are the syntax for the most important functionalities of this sf2 loader.

Firstly, you can import this sf2 loader using this line:

```python
import sf2_loader as sf
```

or you can using this line, which is without namespace, but this is not recommended in big projects because of potential naming conflicts with other python packages you import.

```python
from sf2_loader import *
```

Here we will use the first way of import as the standard.

When you install sf2_loader, the musicpy package will be installed at the same time. The musicpy package is imported in sf2_loader as `mp`, so you can use musicpy package straightly by calling `sf.mp`.

### load a soundfont file

