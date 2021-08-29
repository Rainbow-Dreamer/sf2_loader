# sf2_loader
This is an easy-to-use soundfonts loader and audio renderer in python.

This is probably the most handy soundfont loader and renderer via pure programming at the time I am writing now (2021/8/29). This is a python package, it can load any soundfont files, including sf2 and sf3, you can listen to every preset in every bank in the soundfont files that are loaded using very simple syntax, export audio files for each note in a pitch range for any instruments in the soundfont files, export the whole piece of music as audio files with custom audio effects, and the loader could accpet loading as much soundfont files as you can. For more functionalities that this soundfont loader provides, please continue reading.

This sf2 loader is heavily combined with [musicpy](https://github.com/Rainbow-Dreamer/musicpy), which is one of my most popular project, focusing on music programming and music analysis and composition. If you have already learned how to use musicpy to build notes, chords and pieces, you can straightly pass them to the sf2 loader and let it play what you write. Besides of playing music with the loaded soundfonts files, I also write an audio renderer in the sf2 loader, which could render the audio from the loaded soundfont files with the input musicpy data structures and output as audio files, you can choose the output format, such as wav, mp3, ogg, and output file names, sample width, frame rate, channels and so on. In fact, this project borns with my attempt at making muscipy's sampler module being able to load soundfont files to play and export audio files.

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

You can use `play_chord` function of the sf2 loader to play a chord using current track, soundfont id, bank number and preset number. The chord must be a musicpy chord instance.

You can use `play_piece` function of the sf2 loader to play a piece using current track and soundfont id. The chord must be a musicpy piece instance. Here piece means a piece of music with multiple individual tracks with different instruments on each of them (it is also ok if you want some or all of the tracks has the same instruments). You can custom which instrument you want the soundfont to play for each track by setting the `instruments_numbers` attribute of the piece instance, instrument of a track of the piece instance could be preset_num or [preset_num, bank_num, (track), (sfid)].

You can use `play_midi_file` function of the sf2 loader to play a midi file using current track and soundfont id. You can set the first parameter to the midi file path, and then the sf2 loader will read the midi file and analyze it into a musicpy piece instance, and then render it to audio data.

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

# now you can copy this instruments numbers list to be the value of the instruments parameter of the play_midi_file function
loader.play_midi_file(midi_file_path, get_off_drums=False, instruments=[41, 41, 49, [1, 128], 69, 73, 46])

# when the rendering process is finished, you can hear the midi file playing with current soundfont files

# or you can use play_piece function since you have a piece instance by reading the midi file, and you don't need to specify instruments since the instrument numbers is an attribute of the piece instance
loader.play_piece(current_midi_file)

# you will hear the same thing as using play_midi_file function
```

