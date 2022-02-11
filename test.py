from mido.midifiles import MidiTrack
from mido import MidiFile
# from roll import MidiFile
from mido import Message
from midi_visualize import midi_visualize
from Music import Music
from Note import Note
from Track import Track

mid = MidiFile("blues/12barblues_ms.mid")
my_music = Music()
for i, track in enumerate(mid.tracks):
    # print('Track {}: {}'.format(i, track.name))
    new_track = Track()
    for msg in track:
        print(msg)
        if msg.type == "note_off" or msg.type == "note_on":
            channel = int(msg.channel)
            note = int(msg.note)
            velocity = int(msg.velocity)
            tick = int(msg.time)
            newNote = Note(channel,note,velocity,tick)
            new_track.note_append(newNote)

    my_music.append_track(new_track)

save_name = "my_music.mid"
my_music.save_midi(save_name)
midi_visualize(save_name)