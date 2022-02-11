from mido.midifiles import MidiTrack
from mido import MidiFile
# from roll import MidiFile
from mido import Message
from midi_visualize import midi_visualize
from util import Music,Note,Track


mid = MidiFile("12barblues_ms.mid")
my_music = Music()
my_music.set_ticks_per_beat(mid.ticks_per_beat)
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    new_track = Track()
    for msg in track:
        print(msg)
        if msg.type == "note_off" or msg.type == "note_on":
            channel = int(msg.channel)
            note = [int(msg.note)]
            velocity = int(msg.velocity)
            tick = int(msg.time)
            if msg.type == "note_off":
                newNote = Note(channel,note,velocity,tick,False)
            else:
                newNote = Note(channel,note,velocity,tick,True)

            new_track.note_append(newNote)


    my_music.append_track(new_track)


my_music.display()

save_name = "my_music.mid"
# my_music.save_midi(save_name)
# midi_visualize(save_name)


# mid = MidiFile(save_name)
# my_music = Music()
# print(save_name)
# for i, track in enumerate(mid.tracks):
#     print('Track {}: {}'.format(i, track.name))
#     new_track = Track()
#     for msg in track:
#         print(msg)
