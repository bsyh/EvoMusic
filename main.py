import mido

# blues/12barblues_ms.mid


from mido.midifiles import MidiTrack
from roll import MidiFile
from mido import Message

# with MidiFile() as mid:
#     track = MidiTrack()
#     mid.tracks.append(track)
#     track.append(Message('program_change', program=12, time=0))
#     track.append(Message('note_on', note=64, velocity=64, time=32))
#     track.append(Message('note_off', note=64, velocity=127, time=60))
#
#     track.append(Message('note_on', note=89, velocity=64, time=60))
#     track.append(Message('note_off', note=89, velocity=127, time=200))
#
#     track.append(Message('note_on', note=90, velocity=64, time=200))
#     track.append(Message('note_off', note=90, velocity=127, time=3000))
#
#     track.append(Message('note_off', note=64, velocity=127, time=3200))
#
#     mid.save('new_song.mid')

mid = MidiFile("blues/12barblues_ms.mid")
# mid = MidiFile("new_song.mid")

# get the list of all events
# events = mid.get_events()

# get the np array of piano roll image
roll = mid.get_roll()

# draw piano roll by pyplot
mid.draw_roll()

#read input 1
#read input 2

#convert input1 and input2 to object

#feature extract

#initliazaiton

#loop of evoluation


#output

