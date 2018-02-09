from mido import MidiFile

mid = MidiFile("../../music_datasets/AFoggyD.MID")

# print(mid.tracks)
track = None
for test_track in mid.tracks:
    if hasattr(test_track, 'name') and 'Jazz Bass' in test_track.name:
        print(test_track.name)
        track = test_track
print(track)