# sf2_loader
This is an easy-to-use soundfonts loader, player and audio renderer in python.

This is probably the most handy soundfont loader, player and renderer via pure programming at the time I am writing now (2021/8/29). This is a python package, it can load any soundfont files, including sf2 and sf3, you can listen to every preset in every bank in the soundfont files that are loaded using very simple syntax, play or export audio files for each note in a pitch range for any instruments in the soundfont files, play or export the whole piece of music as audio files with custom audio effects, and the loader could accpet loading as much soundfont files as you can. For more functionalities that this soundfont loader provides, please continue reading.

This sf2 loader is heavily combined with [musicpy](https://github.com/Rainbow-Dreamer/musicpy), which is one of my most popular project, focusing on music programming and music analysis and composition. If you have already learned how to use musicpy to build notes, chords and pieces, you can straightly pass them to the sf2 loader and let it play what you write. Besides of playing music with the loaded soundfonts files, I also write an audio renderer in the sf2 loader, which could render the audio from the loaded soundfont files with the input musicpy data structures and output as audio files, you can choose the output format, such as wav, mp3, ogg, and output file names, sample width, frame rate, channels and so on. In fact, this project borns with my attempt at making muscipy's sampler module being able to load soundfont files to play and export audio files.

If you are not familiar with musicpy data structures and is not willing to learn it in recent times, you can also straightly using midi files as input to the sf2 loader, and export the rendered audio files using the loaded soundfont files. However, I still recommend you to learn about musicpy, even not to consider music programming and analysis, it could also be very useful for midi files editing and reconstructing. But if you want to change the instruments for some of the tracks or even with different soundfont files in the midi files, you will need to do it in the DAW or using musicpy to load midi files as a piece instance.

This sf2 loader is compatible with both 32-bit and 64-bit python versions, for python >= 3.6, so be sure your installed python version match the requirements for this package to use.

This package is currently being tested on Windows, Linux and macOS. For Windows version, this package is tested on Windows 10.

Update: (2021/9/5) The Linux compatible version is ready, the installation and configuration of linux compatible version is at the installation section of this readme. This linux compatible version of sf2_loader is tested on Ubuntu 18.04.5.

Update: (2021/9/5) The macOS compatible version is ready, the installation and configuration of linux compatible version is at the installation section of this readme. This macOS compatible version of sf2_loader is tested on Catalina.10.15.5.

## Installation

### Windows
You can use pip to install this sf2 loader.

Run this line in cmd/terminal to install.

```python
pip install sf2_loader
```

Note: This package uses pydub as a required python package, which requires ffmpeg or libav installed to have abilities to deal with non-wav files (like mp3, ogg files),
so I strongly recommend to install ffmpeg/libav and configure it correctly to make pydub working perfectly. You can refer to this [link](https://github.com/jiaaro/pydub#getting-ffmpeg-set-up) which is pydub's github main page readme to see how to do it, or you can follow the steps I provide here, which is easier and faster.

Firstly, download the ffmpeg rar file from this [link](https://github.com/Rainbow-Dreamer/musicpy/releases/download/3.39/ffmpeg.rar), this is from the release page of musicpy which requires ffmpeg for the musicpy's sampler module.  
Then, unzip the folder `ffmpeg` from the rar file, put the folder in C:\ (or equivalent root path if you are using Linux/macOS).  
Then, add the path `C:\\ffmpeg\\bin` (this will be different for Linux/macOS) to the system environment variable PATH.  
Finally, restart the computer.  
Now you are all done with the set up of ffmpeg for pydub. If there are no warnings about ffmpeg from pydub pop up after you import this package, then you are good to go.

### Linux

You can download the Linux compatible version of sf2_loader from [release page](https://github.com/Rainbow-Dreamer/sf2_loader/releases/latest) of this project. You don't need to pip install this package, just open terminal in the folder `sf2_loader(linux compatible)`, firstly run `pip install midiutil`, and then run `sudo python setup.py install` to install this package. Then, there are some important and necessary steps to configure this package in order to use it on Linux:

Firstly, you need to install fluidsynth on Linux, you can refer to this [link](https://github.com/FluidSynth/fluidsynth/wiki/Download#distributions) to see how to install fluidsynth on different Linux systems. Here I will put the install command for Ubuntu and Debian:
```
sudo apt-get install fluidsynth
```
Run this command in terminal on Ubuntu or Debian, and waiting for fluidsynth to finish installing.

Secondly, you need to install ffmpeg on Linux (the same reason as in Windows), you can just run this command in terminal to install ffmpeg on Linux:
```
sudo apt-get install ffmpeg libavcodec-extra
```
Thirdly, I strongly recommend you to pip install simpleaudio on Linux, since it is the recommended way to play the pydub audio objects (which is used in play functions in this package). But install simpleaudio on Linux isn't as straightforward as on Windows, you can refer to this [link](https://simpleaudio.readthedocs.io/en/latest/installation.html) to see how to install simpleaudio on Linux. If your installation of simpleaudio on Linux is successful, then simpleaudio is used when you use this package. If you are failed to install simpleaudio on Linux (which happens in some Linux systems actually, I have encountered this when testing on a Ubuntu system), this package will use ffplay to play the audio, which has been installed when you install ffmpeg.

### macOS

You can download the macOS compatible version of sf2_loader from [release page](https://github.com/Rainbow-Dreamer/sf2_loader/releases/latest) of this project. You don't need to pip install this package, just open terminal in the folder `sf2_loader(macOS compatible)`, and run `python setup.py install` to install this package. Then, there are some important and necessary steps to configure this package in order to use it on macOS:

Firstly, you need to install fluidsynth on macOS, the easiest way to install ffmpeeg in macOS is using homebrew. You need to make sure you have installed homebrew in macOS first, and then run `brew install fluidsynth` in terminal, and waiting for fluidsynth to be installed.

If you haven't installed homebrew before and cannot find a good way to install homebrew, here I will provide a very easy way to install homebrew on macOS, thanks from Ferenc Yim's answer from this [Stack Overflow question](https://stackoverflow.com/questions/29910217/homebrew-installation-on-mac-os-x-failed-to-connect-to-raw-githubusercontent-com):

open this [link](https://raw.githubusercontent.com/Homebrew/install/master/install.sh) in your browser, right-click and save it to your computer, and then open a terminal and run it with:  
`/bin/bash path-to/install.sh`, and waiting for homebrew to be installed.

Secondly, you need to install ffmpeg on macOS (the same reason as in Windows), you can just run this command in terminal to install ffmpeg on macOS using homebrew:
```
brew install ffmpeg
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

### Initialize a soundfont loader

To initialize a soundfont loader, you can pass a soundfont file path to the class `sf2_loader`, or leave it as empty, and use `load` function of `sf2_loader` to load soundfont files later.

```python
loader = sf.sf2_loader(soundfont_file_path)
# or
loader = sf.sf2_loader()

# examples
loader = sf.sf2_loader(r'C:\Users\Administrator\Desktop\celeste.sf2')
# or
loader = sf.sf2_loader('C:/Users/Administrator/Desktop/celeste.sf2')
```



### Load sondfont files

You can load a soundfont file when you initialize a `sf2_loader` by passing a soundfont file path to the initialize function, or use `load` function of the sf2 loader to load new soundfont files into the sf2 loader.

Each time you load a soundfont file, the sf2 loader will save the soundfont file name and the soundfont id, you can get and use them by calling the attributes `file` and `sfid_list` of the sf2 loader.

You can unload a loaded soundfont file by index (1-based) using `unload` function of the sf2 loader.

```python
loader = sf.sf2_loader(soundfont_file_path)
loader.load(soundfont_file_path2)

# examples
loader = sf.sf2_loader(r'C:\Users\Administrator\Desktop\celeste.sf2')
loader.load(r'C:\Users\Administrator\Desktop\celeste2.sf2')

>>> loader.file
['C:\\Users\\Administrator\\Desktop\\celeste.sf2', 'C:\\Users\\Administrator\\Desktop\\celeste2.sf2']

# if the soundfont file does not exist in the given file path, the soundfont id will be -1

>>> loader.sfid_list
[1, 2]

loader.unload(2) # unload the second loaded soundfont files of the sf2 loader

>>> loader.file
['C:\\Users\\Administrator\\Desktop\\celeste.sf2']
```



### The representation of the soundfont loader

You can print the sf2 loader and get the information that the sf2 loader currently has.

```python
>>> loader
[soundfont loader]
loaded soundfonts: ['C:\\Users\\Administrator\\Desktop\\celeste.sf2', 'C:\\Users\\Administrator\\Desktop\\celeste2.sf2']
soundfonts id: [1, 2]
current track: 0
current soundfont id: 1
current soundfont name: celeste.sf2
current bank number: 0
current preset number: 0
current preset name: Stereo Grand
```



### Change current track, soundfont id, bank number and preset number

You can use the `program_select` function of the sf2 loader to change either one or some or all of the current track, soundfont id, bank number and preset number of the sf2 loader.

There are also some syntactic sugar I added for this sf2 loader, which is very convenient in many cases. 

For example, you can use `loader < preset` to change the current preset number of the sf2 loader to change the instrument of the soundfont files that the sf2 loader will use to play and export, while current track, soundfont id and bank number remain unchanged. This syntactic sugar also accept second parameter as the bank number, which is used as `loader < (preset, bank_num)`.

You can also use `loader % (track, bank_num, preset_num)` to change current track, bank number and preset number of the sf2 loader, while current soundfont file that is using remain unchanged.

There are also a change function for each attribute of current track, soundfont id, bank number and preset number. Note that if you want to change the preset by the name of the preset, you can use `change_preset` function or the syntactic sugar `loader < preset` and `loader < (preset, bank_num)`, but not to use `program_select` function because it only accepts numbers.

```python
loader.program_select(track, sfid, bank_num, preset_num)
# If you only need to change one or some of the attributes,
# you can just specify the parameters you want to change,
# the unspecified parameters will remain unchanged.

# There is also a parameter called correct, if you set it to True,
# when the given parameters cannot find any valid instruments,
# the sf2 loader will go back to the program before the change.
# If you set it to False, the program will be forced to change to the
# given parameters regardless of whether the sf2 loader can find any valid
# instruments or not.

# examples
loader.program_select(preset_num=2) # change current preset number to 2

loader.program_select(bank_num=9, preset_num=3) # change current bank number to 9 and current preset number to 3

loader.change_preset(2) # change current preset number to 2
loader.change_preset('Strings') # change current preset to Strings
loader.change_bank(9) # change current bank number to 9
loader.change_track(2) # change current track to 2
loader.change_sfid(2) # change current soundfont id to 2
loader.change_soundfont('celeste2.sf2')
# change current soundfont file to celeste2.sf2, the parameter could be full path or
# just the file name of the soundfont file, but it must be loaded in
# the sf2 loader already

loader < 2 # change current preset number to 2
loader < 'Strings' # change current preset to Strings
loader < (3, 9) # change current bank number to 9, current preset number to 3
loader < ('Strings', 9) # change current bank number to 9, current preset to Strings
loader % (2, 9, 3) # change current track to 2, current bank number to 9, current
# preset number to 3
```



### Get the instrument names

If you want to get the instrument names of the soundfont files you load in the sf2 loader, you can use `get_all_instrument_names` function of the sf2 loader, which will give you a list  of instrument names that current bank number and current soundfont file has (or you can specify them), with given maximum number of preset number to try, start from 0. Sometimes, some of the preset numbers does not have instruments in current bank number, when it happens, fluidsynth will throw out warning messages, but it doesn't crash your programs, just print on the screen. By default, the maximum number of the preset number to try is 128, which is from 0 to 127. If you want to get the exact preset numbers for all of the instrument names in current bank number, you can set the parameter `get_ind` to `True`.

```python
loader.get_all_instrument_names(track=None,
                               	sfid=None,
                               	bank_num=None,
                                num=0,
                                max_num=128,
                                get_ind=False,
                                mode=0)

# mode: if mode is 1, the current preset number will be set to the first available
# instrument in the current bank number
```



To get the instrument name of  a given track, soundfont id, bank number and preset number, you can use `get_instrument_name` function.

```python
loader.get_instrument_name(track=None,
                           sfid=None,
                           bank_num=None,
                           preset_num=None,
                           num=0)
```



To get current instrument name, you can use `get_current_instrument` function.

```python
loader.get_current_instrument(num=0)
```



To get the instrument name in current track of a given soundfont id, bank number and preset number, you can use `preset_name` function.

```python
loader.preset_name(sfid=None, bank_num=None, preset_num=None)
```

Here is an example of get all of the instrument names in current bank number.

```python
>>> loader.get_all_instrument_names()
['Stereo Grand', 'Bright Yamaha Grand', 'Electric Piano', 'Honky-tonk EMU2', 'Electric Piano 1', 'Legend EP 2', 'St.Harpsichd_Lite', 'Clavinet', 'Celesta', 'Glockenspiel', 'Music Box', 'VivesPS06', 'prc:Marimba', 'Xylophone', 'Tubular Bells', 'Dulcimer', 'DrawbarOrgan', 'PercOrganSinkla', 'Rock Organ', 'Church Organ', 'Reed Organ', 'Accordian', 'Harmonica', 'Bandoneon', 'TyrosNylonLight', 'Steel Guitar', 'Jazz Gt', 'Dry Clean Guitar', 'Palm Muted Guitar', 'Garcia _0_29', 'Les Sus_0_30', 'Guitar Harmonic', 'Acoustic Bass', 'MM JZ.F_0_33', 'BassPick&Mutes', 'Fretless Bass', 'Slap Bass 1', 'Slap Bass 2', 'Synth Bass 1', 'Synth Bass 2', 'Violin', 'Viola', 'Cello', 'Contrabass', 'Tremolo', 'Pizzicato Section', 'ClavinovaHarp', 'Timpani', 'Strings Orchest', 'Slow Strings', 'Synth Strings 1', 'Synth Strings 2', 'Ahh Choir', 'Ohh Voices', 'SynVoxUT', 'Orchestra Hit', 'Romantic Tp', 'Solo Bo_0_57', 'Tuba', 'Sweet Muted', 'FH LONG_0_60', 'BRASS', 'AccesVirusBrass', 'Synth B_0_63', 'Soprano Sax', 'Altsoft vib', 'Blow Tenor', 'Bari Sax', 'Oboe', 'English Horn', 'Bassoon', 'Clarinet', 'Piccolo', 'Flute', 'Recorder', 'ClavinovaPanFlu', 'Bottle Blow', 'Shakuhachi', 'Whistle', 'Ocarina', 'Square Wave', 'Saw Wave', 'Calliope Lead', 'Chiffer Lead', 'Charang', 'Solo Vox', 'Fifth Sawtooth Wave', 'Bass & Lead', 'Fantasia', 'Warm Pad', 'Polysynth', 'Space Voice', 'Bowed Glass', 'Metal Pad', 'Halo Pad', 'Sweep Pad', 'Ice Rain', 'Soundtrack', 'Crystal', 'Atmosphere', 'Brightness', 'Goblin', 'Echo Drops', 'Star Theme', 'Sitar', 'Banjo', 'Shamisen', 'Koto', 'Kalimba', 'BagPipe', 'Fiddle', 'Shenai', 'Tinker Bell', 'Agogo', 'Steel Drums', 'Woodblock', 'Taiko Drum', 'Melodic Tom', 'Synth Drum', 'Reverse Cymbal', 'Fret Noise', 'Breath Noise', 'Sea Shore', 'Bird Tweet', 'Telephone', 'Helicopter', 'Applause', 'Gun Shot']
```



### Play notes, chords, pieces and midi files

You can use `play_note` function of the sf2 loader to play a note with specified pitch using current track, soundfont id, bank number and preset number. The note could be a strings representing a pitch (for example, `C5`) or a musicpy note instance. If you want to play the note by another instrument, you need to change current preset (and other program parameters if needed) before you use `play_note` function, the same goes for other play functions.

```python
loader.play_note(note_name,
                 duration=2,
                 decay=1,
                 volume=100,
                 track=0,
                 start_time=0,
                 sample_width=2,
                 channels=2,
                 frame_rate=44100,
                 name=None,
                 format='wav',
                 other_effects=None,
                 bpm=80)

# note_name: the name of the note, i.e. C5, D5, C (if the octave number
# is not specified, then the default octave number is 4), or musicpy note instance

# duration: the duration of the note in seconds

# decay: the decay time of the note in seconds

# volume: the volume of the note in midi velocity from 0 - 127

# track: the track to play the note

# start_time: the start time of the note in seconds

# sample_width: the sample width of the rendered audio

# channels: the number of channels of the rendered audio

#  frame_rate: the frame rate of the rendered audio

# name: the file name of the exported audio file, this is only used in export_note function

# format: the audio file format of the exported audio file, this is only used in export_note function

# other_effects: audio effects you want to add to the rendered audio

# bpm: the BPM of the note


# examples
loader.play_note('C5') # play a note C5 using current instrument

# you will hear a note C5 playing using current instrument

loader < 25 # change to another instrument at preset number 25

loader.play_note('C5') # play a note C5 using the instrument we have changed to

# you will hear a note C5 playing using a new instrument

loader.play_note('D') # play a note without octave number specified, will play the note D4

loader.play_note(sf.mp.N('C5')) # play a note using musicpy note structure

loader.play_note('C5', duration=3) # play a note C5 for 3 seconds
```



You can use `play_chord` function of the sf2 loader to play a chord using current track, soundfont id, bank number and preset number. The chord must be a musicpy chord instance.

```python
loader.play_chord(current_chord,
                  decay=0.5,
                  track=0,
                  start_time=0,
                  piece_start_time=0,
                  sample_width=2,
                  channels=2,
                  frame_rate=44100,
                  name=None,
                  format='wav',
                  bpm=80,
                  fixed_decay=False,
                  other_effects=None,
                  pan=None,
                  volume=None)

# current_chord: musicpy chord instance

# decay: the decay time unit in seconds, each note's decay time will be calculated
# with decay * duration of the note, or if fixed_decay is True, this decay time
# will be applied to every note, this decay time could also be a list of each note's
# decay time

# track - bpm: same as play_note

# piece_start_time: this is used when dealing with a musicpy piece instance, you won't need to set this generally

# fixed_decay: if this is set to True, the decay time will be applied to every note

# other_effects: same as play_note

# pan: the pan effects you want to add to the rendered audio

# volume: the volume effects you want to add to the rendered audio

# the pan and volume effects are corresponding to the midi CC messages


# examples
loader.play_chord(sf.mp.C('C')) # play a C major chord starts at C4 (default when
# no octave number is specified)

loader.play_chord(sf.mp.C('Cmaj7', 5)) # play a Cmaj7 chord starts at C5
```



You can use `play_piece` function of the sf2 loader to play a piece using current track and soundfont id. The piece must be a musicpy piece instance. Here piece means a piece of music with multiple individual tracks with different instruments on each of them (it is also ok if you want some or all of the tracks has the same instruments). You can custom which instrument you want the soundfont to play for each track by setting the `instruments_numbers` attribute of the piece instance, instrument of a track of the piece instance could be preset_num or [preset_num, bank_num, (track), (sfid)].

```python
loader.play_piece(current_chord,
                  decay=0.5,
                  track=0,
                  start_time=0,
                  sample_width=2,
                  channels=2,
                  frame_rate=44100,
                  name=None,
                  format='wav',
                  fixed_decay=False,
                  other_effects=None,
                  clear_program_change=True)

# current_chord: musicpy piece instance

# decay: the decay time for the tracks of the piece instance, which is musicpy chord
# instance, note that this decay time will be applied to every track

# track - other_effects: same as play_chord

# clear_program_change: when there are program change messages in the piece instance,
# the instruments are forced to change during rendering, so you cannot use the
# instrument you want to play, if you clear these messages, then you can specify
# which instruments you want to play


# examples

# construct a musicpy piece instance and play it using the sf2 loader
current_piece = sf.mp.P([sf.mp('C'), sf.mp.chord('A2')], [2, 35], tempo=150)
loader.play_piece(current_piece)

# read a midi file to a musicpy piece instance and play it using the sf2 loader
current_midi_file = sf.mp.read(midi_file_path, mode='all', to_piece=True, get_off_drums=False)
loader.play_piece(current_midi_file)
```



You can use `play_midi_file` function of the sf2 loader to play a midi file using current track and soundfont id. You can set the first parameter to the midi file path, and then the sf2 loader will read the midi file and analyze it into a musicpy piece instance, and then render it to audio data.

```python
loader.play_midi_file(current_chord,
                      decay=0.5,
                      track=0,
                      start_time=0,
                      sample_width=2,
                      channels=2,
                      frame_rate=44100,
                      name=None,
                      format='wav',
                      fixed_decay=False,
                      other_effects=None,
                      clear_program_change=True,
                      instruments=None,
                      **read_args)

# current_chord: the midi file path

# decay - clear_program_change: same as play_piece

# instruments: the list of the instruments you want to play, the sf2 loader
# will use this instrument list instead of the instrument settings in the midi file,
# note that this instruments list must be the same length as the number of tracks
# of the midi file

# **read_args: this is the keyword arguments for the musicpy read function


# examples

# play a midi file given a file path using current soundfont file
loader.play_midi_file(r'C:\Users\Administrator\Desktop\test.mid')

loader.change_soundfont('celeste2.sf2') # change to another loaded soundfont file

# play a midi file given a file path using another soundfont file
loader.play_midi_file(r'C:\Users\Administrator\Desktop\test.mid')

# you can also specify which track use which soundfont files in the instruments
# parameter by specifying the soundfont id
```



Note that by default the drum track of the midi file is ignored, if you want to include the drum track as well, you can add `get_off_drums=False` when you use `play_midi_file` function.

You can specify which bank and preset (including track and sfid) that each track of the midi file uses by setting the `instruments` parameter of the `play_midi_file` function.

This is sometimes very important, for example, if you want to correctly play the drum track of a midi file, you will firstly need to change the instrument of the drum track to the bank number that the soundfont file has drums instruments, which is usually 128 (the indexing is 0-based).

But here you may encounter a problem: how do I know which preset that each track of the midi file uses and how many tracks are there? I need to change the bank number for the instruments of some tracks of the midi file to correctly play what they are supposed to be.

No, you don't need to use a DAW, you can just use musicpy's `read` function to read the midi file as a piece instance, and then you can get the instruments list including the instrument names and instrument numbers for each track of the midi file.

```python
current_midi_file = sf.mp.read(midi_file_path, mode='all', to_piece=True, get_off_drums=False)

>>> current_midi_file.instruments_list
['Violin', 'Violin', 'String Ensemble 1', 'Acoustic Grand Piano', 'Oboe', 'Piccolo', 'Pizzicato Strings']

>>> current_midi_file.instruments_numbers
[41, 41, 49, 1, 69, 73, 46]

# usually the drum track is channel 9 (the indexing is 0-based),
# so you can check out the channel numbers of the midi file
>>> current_midi_file.channels
[0, 1, 2, 9, 3, 4, 5]

# we can see that the channel 9 is at the index of 3, so we can change
# the instrument of the drum track by changing the instrument number at the index of 3
current_midi_file.instruments_numbers[3] = [1, 128]

>>> current_midi_file.instruments_numbers
[41, 41, 49, [1, 128], 69, 73, 46]

# now you can copy this instruments numbers list to be the value of
# the instruments parameter of the play_midi_file function
loader.play_midi_file(midi_file_path, get_off_drums=False, instruments=[41, 41, 49, [1, 128], 69, 73, 46])

# when the rendering process is finished, you can hear the midi file playing with current soundfont files

# or you can use play_piece function since you have a piece instance by reading the midi file,
# and you don't need to specify instruments since the instrument numbers
# is an attribute of the piece instance
loader.play_piece(current_midi_file)

# you will hear the same thing as using play_midi_file function
```



### Export notes, chords, pieces and midi files

You can export notes, chords, pieces and midi files using loaded soundfont files in the sf2 loader using `export_note`, `export_chord`, `export_piece`, `export_midi_file` function of the sf2 loader.

All of the parameters of these export functions can refer to their corresponding play functions, except a parameter `get_audio`, if this parameter is set to True, then the export functions will return an AudioSegment instance (this is an audio instance in pydub) which contains raw audio data for further audio process. If this parameter is set to False (which is default), then the export functions will export the rendered audio data to an audio file with the file name and the audio file format you specify.

```python
# examples

# render a midi file with current soundfont files and export as a mp3 file 'test,mp3'
loader.export_midi_file(r'C:\Users\Administrator\Desktop\test.mid', name='test.mp3', format='mp3')
```



### Export sound modules

You can export sound modules of a specified instrument of the loaded soundfont files using `export_sound_modules` function of the sf2 loader.

You can specify the pitch range of the notes, the default is from A0 to C8, which is the most common 88 keys on the piano.

The duration of the notes is 6 seconds by default, you can set the duration of the notes in the function.

The format of the export audio files is wav by default, you can set the export audio file format in the function.

The exported audio file name of each note will be in the format `pitch.format` by default, where pitch is the note name such as `C5`, format is the audio file format you specify such as `wav`, so for example, the exported audio file names of notes will be like `C5.wav`, `C#5.wav`, `D5.wav`. You can custom the name format of each note with the parameter `name` in the function, it could either be a list of each note's name (without file extension) or a function to format each note's name (without file extension).

```python
loader.export_sound_modules(track=None,
                            sfid=None,
                            bank_num=None,
                            preset_num=None,
                            start='A0',
                            stop='C8',
                            duration=6,
                            decay=1,
                            volume=127,
                            sample_width=2,
                            channels=2,
                            frame_rate=44100,
                            format='wav',
                            folder_name='Untitled',
                            other_effects=None,
                            bpm=80,
                            name=None,
                            show_full_path=False)

# track, sfid, bank_num, preset_num: use which instrument to play, you can refer to
# program_select function

# start, stop: the pitch range, note that these must be strings representing pitches

# duration - format: refer to play_note function

# folder_name: the folder name of the exported sound modules

# other_effects: refer to play_note function, will be applied to each note

# bpm: refer to play_note function

# name: if not None, then set each note's file name with this parameter,
# this could be a list of each note's name (without file extension) or a function
# to format each note's name (without file extension),
# for example, ['C5', 'C#5' 'D5'], lambda s: f'piano{s}'

# show_full_path: when this function is running, it will print the export messages
# for each note, showing which soundfont file and which bank and preset
# you use to export which note, if this is set to True,
# then the file path of the soundfont file will be full path,
# otherwise the file path will be only the file name


# examples

# export notes from A0 to C8 of current instrument
loader.export_sound_modules()

# export notes from C5 to C6 of current instrument
loader.export_sound_modules(start='C5', stop='C6')

# export notes from A0 to C8 of current instrument of
# the loaded soundfont file with id 2
# (or you can change current soundfont file in advance)
loader.export_sound_modules(sfid=2)
```



### Audio effects

There is a `other_effects` parameter in the play and export functions, but how to use it?

This python package provides a class `effect`, which could store a type of audio effect, such as reverse, offset, fade in, fade out, ADSR envelope. You can use `effect` class to package an audio effect message and put it as an element in a list, the list could be used as the value of `other_effects` in the play and export functions.

```python
effect(effect, value=None)

# effect: the type of audio effect, could be one of 'reverse', 'offset', 'fade',
# 'adsr'

# value: the parameters of the audio effect, will be used in offset, fade and adsr,
# if there are multiple parameters, this could be a list or a tuple


# examples

# play a note C5 using current instrument with a reverse audio effect
loader.play_note('C5', other_effects=[effect('reverse')])

# export a note C5 using current instrument with a reverse audio effect
loader.export_note('C5', other_effects=[effect('reverse')])
```

For the parameters of each type of audio effects, please refer to the sampler module of musicpy, here is the [link](https://github.com/Rainbow-Dreamer/musicpy/wiki/musicpy-sampler-module#audio-mixing-and-editing) for the documentation of the audio effects.
