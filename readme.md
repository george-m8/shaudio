# shAudio
Audio to visual project for Shaun. 

## Prerequesits:
- portaudio

## To Do:
- Latency is too high, work on fix
    - Currently trying to send every audio frame at a fairly high sample rate
        - Lower sample rate (breaks frequency values creating NaN values)
        - Send samples x times per second instead
- Uses externally hosted P5.js library, need to store locally for offline usage.
- Currently showing P5 canvas in a web file.
    - In future will create those canvases in some sort of app so that nice transition can be created
        - Create transitions using webGL
- Audio input is really jumpy, would be nice to smooth out somehow.
- EQ is a bit dodgy, mid and high signals are basically not seen, low signal more or less acts as a level indicator. Sure I can tweak values.
- EQ is ugly as fuck.
- Thought this would be a cool effect: https://editor.p5js.org/unicornCoder/sketches/oTpDwu-r0
    - Modify radius with one of our values
    - Store of cool words to use?
- Would like to create some sort of a beat value. Would a lowpass eq do the job?
- Normalise values that are output
- I've created an audio effects script with intention of applying effects like a compressor and more. Not working currently, makes the numbers SO BIG.

## How to run:
- Install portaudio (think theres a brew)
- Create venv
- Install requirements.txt (some in here atm that aren't required so feel free to install what you need)
- Go to localhost:8000 to see an eq based off of your mic.