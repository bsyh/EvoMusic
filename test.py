from util import *
from rule import *

from feature_extraction import read_to_notes, containsPattern, compose
from util import Feature, Feature_pool

# read input 1
pop_num = 5
length = 30
source1, tick1 = read_to_notes('2.mid')

# read input 2
source2, tick2 = read_to_notes('2.mid')

# init pool
feature_pool = Feature_pool()

# extract featurse

containsPattern(feature_pool, source1, tick1)
feature_pool.show_pool()

# initliazaiton
population = []
for i in range(pop_num):
    track = Track([compose(length, feature_pool)])
    music = Music([track])
    population.append(music)

n=0
for item in population:  # TODO
    item.ticks_per_beat = tick1
    save_path = "choices/"+str(n)+".mid"
    population[n].save_midi(save_path)
    n+=1


original=population[0]
n=0
for item in population:
    print(n)
    macro = macro_pitch_order(original,item)
    micro = micro_pitch_order(original,item)
    print("macro:",macro)
    print("micro:",micro)
    fitness = macro*4 + micro
    print("fitness:", fitness)
    n += 1
# a="abcdefg"
# b="zzzzzzzzzz"
# print(levenshtein(a, b))