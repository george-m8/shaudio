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