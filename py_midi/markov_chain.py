import time
import numpy as np
import mido
from mido import MidiFile

mid = MidiFile("../../midi_files/melodies/Melody 001.mid")

bpm = 120

# print(mid.tracks)
track = None
for test_track in mid.tracks:
    if hasattr(test_track, 'name') and 'Guitar' in test_track.name:
        print(test_track.name)
        track = test_track
        break

print(mido.get_output_names())
# port = mido.open_output('loopMIDI Port 1')


# with mido.open_output('loopMIDI Port 1') as port:

occurrence_mat = np.zeros((128, 128))

last_note = None
for msg in track:
    if not msg.is_meta:
        # sleep_time = (msg.time * 60 / bpm) / mid.ticks_per_beat
        sleep_time = mido.tick2second(msg.time, mid.ticks_per_beat, mido.bpm2tempo(bpm))
        if msg.type == 'note_on' and msg.velocity != 0:
            new_note = msg.note
            if last_note is not None:
                occurrence_mat[last_note][new_note] += 1
            last_note = new_note

prob_mat = occurrence_mat / np.sum(occurrence_mat, axis=1)
print(prob_mat)