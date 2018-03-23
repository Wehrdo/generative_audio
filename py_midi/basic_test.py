import mido
import time

with mido.open_output('loopMIDI Port 1') as port:
    for i in range(60, 73):
        port.send(mido.Message('note_on', note=i, velocity=120))
        time.sleep(0.3)
        port.send(mido.Message('note_off', note=i))
