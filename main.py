from util import *


from mido.midifiles import MidiTrack
from mido import MidiFile
from mido import Message


# get the list of all events
# events = mid.get_events()

# get the np array of piano roll image
# roll = mid.get_roll()

# draw piano roll by pyplot
# mid.draw_roll()




from feature_extraction import read_to_notes,containsPattern,compose
from util import Feature,Feature_pool




#read input 1
pop_num = 5
length =30
source1 = read_to_notes('2.mid')
#read input 2
source2 = read_to_notes('2.mid')
print(source2)
#init pool
feature_pool = Feature_pool()
#extract featurse

containsPattern(feature_pool, source1)
feature_pool.show_pool()


#initliazaiton
population = []
for i in range(pop_num):
    track = Track([compose(length, feature_pool)])
    music = Music([track])
    population.append(music)

population[0].display()

save_path = "my_music.mid"
population[0].save_midi(save_path)
mid2 = MidiFile(save_path)
# from midi_visualize import midi_visualize
# midi_visualize(save_path)


#loop of evoluation

#parent selection 

#crossover

#mutation




#end loop
#output

