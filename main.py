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

# mid = MidiFile("blues/12barblues_ms.mid")
# mid = MidiFile("new_song.mid")

# get the list of all events
# events = mid.get_events()

# get the np array of piano roll image
# roll = mid.get_roll()

# draw piano roll by pyplot
# mid.draw_roll()




from feature_extraction import feature_pool,containsPattern,compose,read_to_notes


#read input 1

source1 = read_to_notes('2.mid')
#read input 2
source2 = read_to_notes('2.mid')

#init pool
feature_pool = feature_pool()

#extract featurse
#convert input1 and input2 to object


#feature extract
# feature_p = feature_pool()
# containsPattern(feature_p,star_note,star_time,3,5)
# min3_pool = feature_pool(feature_p.give_pool(3))
# # min3_pool.show_pool()
# # pool = make_pool(x)
# 
# x1 = compose(12,min3_pool)
# x2 =compose(12,min3_pool)
# x1.show_pool()
# x2.show_pool()
# play(x2)

#initliazaiton

#loop of evoluation

#parent selection 

#crossover

#mutation




#end loop
#output

