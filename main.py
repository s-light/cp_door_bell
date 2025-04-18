# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
CircuitPython single MP3 playback example for Raspberry Pi Pico.
Plays a single MP3 once.
"""
import time
import board
import audiobusio
import audiomp3
import audiocore
import digitalio

btn1 = digitalio.DigitalInOut(board.A3)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP

print("audio ready.")




audio = audiobusio.I2SOut(board.A2, board.A1, board.A0)

# filename = "music/test_loop.wav"
filename = "music/614431__bingopro__sound-effect-pro-trimed 11kHz64kbps.mp3"
# filename = "music/185487__mika55__wiodubstep-loop005.mp3"

if (filename.endswith('.wav')):
    print("wav file")
    audio_data = audiocore.WaveFile(open(filename, "rb"))
elif (filename.endswith('.mp3')):
    print("mp3")
    audio_data = audiomp3.MP3Decoder(open(filename, "rb"))
else:
    print("unknown")
    audio_data = False
print("audio ready.")

def play_bell():
    # Update to True loop playback. False plays once.
    LOOP = True
    print("Playing audio_data")
    audio_data.file = open(filename, "rb")
    audio.play(audio_data, loop=LOOP)
    while audio.playing:
        pass
        time.sleep(1)
    print("Done playing!")
    audio.stop()


while True:
    if not btn1.value:  # button 1 pressed
        play_bell()
    
