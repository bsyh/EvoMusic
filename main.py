from util import Track,Music,one_pt_crossover,reverse_mutation,evaluation,feedmax
from midi_visualize import midi_visualize
import shutil
import os
from mido.midifiles import MidiTrack
from mido import MidiFile
from mido import Message

# get the list of all events
# events = mid.get_events()

# get the np array of piano roll image
# roll = mid.get_roll()

# draw piano roll by pyplot
# mid.draw_roll()
from rule_weight import set_weight, read_weight


# provide choice

from feature_extraction import read_to_notes,containsPattern,compose
from util import Feature,Feature_pool,original

weight = read_weight()
dir = 'choices'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))
#read input 1
pop_num = 500
length =30
source1,tick1 = read_to_notes('12barblues_ms.mid')
org = original(source1, tick1) 
#read input 2
source2,tick2 = read_to_notes('12barblues_ms.mid')

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
for item in population:# TODO
  item.ticks_per_beat = tick1
save_path = "choices/1.mid"
population[0].save_midi(save_path)
mid2 = MidiFile(save_path)

# midi_visualize(save_path)


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
counter = 0
while inloop:
  # output 1，2 TODO switch to evaluated best as competcotr
  a,b= feedmax(population)
  counter +=1
  a.save_midi("choices/my_music1.mid")
  counter +=1
  b.save_midi("choices/my_music2.mid")

  # population[2].save_midi("choices/my_music3.mid")



  # receive choice
  desicion = input('I prefer___,\"s\" to stop,\"r\" roll')  #reroll to provide another set of choice
  
  if desicion == '1':
    #give 1 more weighs
    print('1 is better')
    desicion =a
    
  elif desicion == '2':
    #give 2more weighs
    print('2 is better')
    desicion =b
    
  elif desicion == 's':
    #stop loop
    inloop = False
    # output final result
    # modify evaulation
    fitness_list_1 = evaluation(population, desicion, weight)
    # weight = [1, 0, 1]
    # fitness_list_2=evaluation(population,org,weight)
    fitness_list = []
    for i in range(len(fitness_list_1)):
      # fitness_list.append(fitness_list_1[i]+fitness_list_2[i])
      fitness_list.append(fitness_list_1[i])
    final, secondbest = feedmax(population)
    final.save_midi("choices/final.mid")
    inloop = False
    break
    
  elif desicion == 'r':
    #roll again
    #stop loop
    pass
  else:
    print('wrong input')

  # set_weight([1, 4, 1])
  weight = read_weight()

  fitness_list_1 = evaluation(population, desicion, weight)
  # set_weight([1, 0, 0.01])
  weight = read_weight()

  # fitness_list_2=evaluation(population,org,weight)
  fitness_list = []
  for i in range(len(fitness_list_1)):
    # fitness_list.append(fitness_list_1[i]*0+fitness_list_2[i])
    fitness_list.append(fitness_list_1[i] * 0)

  best_index = fitness_list.index(min(fitness_list))
  population[best_index].save_midi("choices/worst_2.mid")
  # print(best_index)
  # print(max(fitness_list))
  # print(min(fitness_list))



