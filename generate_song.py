
# blues/12barblues_ms.mid


from mido.midifiles import MidiTrack
from mido import MidiFile
from mido import Message

with MidiFile() as mid:
    track = MidiTrack()
    mid.tracks.append(track)
    track.append(Message('program_change', program=12, time=0))
    track.append(Message('note_on', note=64, velocity=64, time=32))
    track.append(Message('note_off', note=64, velocity=0, time=60))

    track.append(Message('note_on', note=89, velocity=64, time=60))
    track.append(Message('note_off', note=89, velocity=0, time=200))

    track.append(Message('note_on', note=90, velocity=64, time=200))
    track.append(Message('note_off', note=90, velocity=0, time=400))

    track.append(Message('note_on', note=90, velocity=64, time=600))
    track.append(Message('note_off', note=90, velocity=0, time=800))

    track.append(Message('note_on', note=90, velocity=64, time=1000))
    track.append(Message('note_off', note=90, velocity=0, time=1200))

    mid.save('new_song.mid')
