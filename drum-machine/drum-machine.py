import audioio
import touchio
import board
import time

from digitalio import DigitalInOut, Direction

bpm = 120

# Enable the speaker
spkrenable = DigitalInOut(board.SPEAKER_ENABLE)
spkrenable.direction = Direction.OUTPUT
spkrenable.value = True

# Make the A1 cap sense pads
touch1 = touchio.TouchIn(board.A1)

audiofiles = [
    'bd_tek.wav',
    'elec_hi_snare.wav',
    'elec_cymbal.wav',
    'elec_blip2.wav',
    'bd_zome.wav',
    'bass_hit_c.wav',
    'drum_cowbell.wav'
]

a = audioio.AudioOut(board.A0)

def play_file(filename):
    f = open(filename, "rb")
    wave = audioio.WaveFile(f)
    a.play(wave)
    time.sleep(bpm/960)  # sixteenthNote delay


while True:
    i = 0
    for i in range(7):
        if touch1:
            play_file(audiofiles[i])
