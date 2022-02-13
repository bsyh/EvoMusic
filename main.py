from util import *
from midi_visualize import midi_visualize

from mido.midifiles import MidiTrack
from mido import MidiFile
from mido import Message


# get the list of all events
# events = mid.get_events()

# get the np array of piano roll image
# roll = mid.get_roll()

# draw piano roll by pyplot
# mid.draw_roll()



# provide choice

from feature_extraction import read_to_notes,containsPattern,compose
from util import Feature,Feature_pool

#read input 1
pop_num = 5
length =30
save_path = '/choices'
source1,tick1 = read_to_notes('2.mid')

#read input 2
source2,tick2 = read_to_notes('2.mid')
print(source2)

#init pool
feature_pool = Feature_pool()

#extract featurse

containsPattern(feature_pool, source1,tick1)
feature_pool.show_pool()


#initliazaiton
population = []
for i in range(pop_num):
    track = Track([compose(length, feature_pool)])
    music = Music([track])
    population.append(music)

population[0].display()

population[0].ticks_per_beat = 480
save_path = "my_music.mid"
population[0].save_midi(save_path)
mid2 = MidiFile(save_path)

midi_visualize(save_path)


#loop of evoluation

#parent selection 

#crossover
population[0].display()
population[1].display()
print("Cross-over:")
one_pt_crossover(population[0],population[1])
#mutation
population[0].display()
population[1].display()
print("Reverse mutated:")
reverse_mutation(population[0],track_index=0,feature_index=0)
reverse_mutation(population[1],track_index=0,feature_index=0)
population[0].display()
population[1].display()



inloop = True
while True:
  # output 1，2 TODO switch to evaluated best as competcotr
  population[0].save_midi(save_path)
  population[1].save_midi(save_path)

  # receive choice
  desicion = input('I prefer___,anything else for roll')  #reroll to provide another set of choice

  if int(desicion) == 1:
    #give 1 more weighs
    print('1 is better')
    break
  elif int(desicion) == 2:
    #give 2more weighs
    print('2 is better')

    break

#modify evaulation



#end loop


#output final result

