# class Note:
#     def __init__(self):
#         self.channel = 0
#         self.note = 0
#         self.velocity = 0
#         self.tick = 0
#         self.type = True
# 
# 
#     def __init__(self, channel, note, velocity, tick, note_type):
#         self.channel = channel
#         self.note = note
#         self.velocity = velocity
#         self.tick = tick
#         self.type = note_type
# 
#     def set_channel(self,channel):
#         self.channel = channel
# 
#     def set_note(self,note):
#         self.note = note
# 
#     def set_velocity(self,velocity):
#         self.velocity = velocity
# 
#     def set_tick(self,tick):
#         self.tick = tick
# 
#     def set_type(self,type):
#         self.type = type
# 
# 
#     def display(self):
#         print("Note", self.channel, self.note, self.velocity, self.tick)
import random

from mido import Message, MetaMessage, MidiFile, MidiTrack
from rule import first_rule,macro_pitch_order,micro_pitch_order


rule = [[first_rule,1],[macro_pitch_order,1],[micro_pitch_order,1]]


class Feature_pool:

  def __init__(self, pool=[]):
    self.feature_pool = pool

  def new_feature(self, notes,tick):
    '''
    if it exists add to a feature if it not exist add it to a new feature object
    :param notes:  a list of note objects 
    :return: 
    '''
    name = [note.note for note in notes]
    # if note exist,add time to it or create a new note
    for item in self.feature_pool:
      if item.name == name:
        return item.add_phenotype(notes)
    # not exist , new note
    new_feature = Feature(notes,tick)
    self.feature_pool.append(new_feature)

  def show_pool(self):
    for item in self.feature_pool:
      print('feature:', item.name, 'count:', item.count)

  def give_pool(self, min_count):
    pool_list = []
    for item in self.feature_pool:
      if item.count >= min_count:
        pool_list.append(item)
    return pool_list

class Feature:
  def __init__(self, notes,tick):
    '''
    note is a list of note objects
    :param notes: 
    '''
    self.name = [note.note for note in notes]
    self.notes = notes
    self.phenotypes  = [notes]
    # self.duration =[[note.duration for note in notes]]
    # self.duration = notes
    self.tick = tick
    self.count = 1

  def add_phenotype(self, notes):
    # add count if new add  to list if exist add to list
    duration = [note.duration for note in notes]
    if duration not in self.phenotypes:
      self.count += 1
      return self.phenotypes.append(notes)
    self.count += 1
    return self.phenotypes.append(notes)

  def get_time(self, time):
    return time in self.time

  def get_note(self):
    return self.note

class Note:



  def __init__(self, channel=0, note=[-1], velocity=128, start_time=0, duration=100):
    '''
    with argument
    :param channel: 
    :param note: list[5,6] or [10] or [-1]
    :param velocity: 
    :param time: 
    :param note_type: 
    '''
    self.channel = channel
    self.note = note
    self.velocity = velocity
    self.start_time = start_time
    self.duration = duration

  def display(self):
    print("Note", self.channel, self.note, self.velocity, self.tick)

class Track:
    def __init__(self,feature_list=[]):
      self.feature_list = feature_list
      self.size = 0

    def feature_append(self, new_feature):
      self.feature_list.append(new_feature)
      self.size += 1

class Music:
    def __init__(self,track_list=[]):
      self.track_list = track_list
      self.ticks_per_beat = 100
      self.fitness = 0

    def set_ticks_per_beat(self, ticks_per_beat):
      self.ticks_per_beat = ticks_per_beat

    def append_track(self, new_track):
      self.track_list.append(new_track)

    def display(self):
      for i in range(len(self.track_list)):
        print("Track:", i)

        print("Note      :", end="")
        for j in range(len(self.track_list[i].feature_list)):
          for k in self.track_list[i].feature_list[j]:
            for z in k:
              print(z.note, end=' ')
            print(" | ",end='')
        print("")

        print("Duration  :", end="")
        for j in range(len(self.track_list[i].feature_list)):
            for k in self.track_list[i].feature_list[j]:
                for z in k:
                    print(z.duration, end=' ')
                print(" | ", end='')
        print("")


        print("")
    
    def evaluate(self,rule_pool,choice):
      for rule in rule_pool:
        self.fitness += rule[0](self,choice) * rule[1]


    def save_midi(self,save_path = 'new_song.mid'):
        mid = MidiFile()
        for track_index in range(len(self.track_list)):

            track = MidiTrack()
            mid.tracks.append(track)
            # track.append(Message('program_change', program=12, time=0))
            for feature_index in range(len(self.track_list[track_index].feature_list)):
                # print("有track",track_index)
                for note_list in self.track_list[track_index].feature_list[feature_index]:
                    for note in note_list:
                        velocity = 127  #TODO shold be feature.velcoty
                        note_note = note.note
                        start_time = note.start_time
                        duration = note.duration
                        channel = 12
                        for i in note_note:
                            track.append(Message('note_on', channel=channel, note=i, velocity=velocity, time=0))
                        gap = duration
                        for i in note_note:
                            track.append(Message('note_off', channel=channel, note=i, velocity=velocity, time=gap))
                            gap = 0
        track.append(MetaMessage('end_of_track', time=0))
        mid.ticks_per_beat=self.ticks_per_beat
        mid.save(save_path)

'''
Crossover
'''


def one_pt_crossover(music_1, music_2, max_distance=4, length_limit=100):
    '''

    :param parent_1: individual 1
    :param parent_2: individual 1
    :param max_distance:  the distance between the crossover points on two individuals
    :param length_limit: the maximum length of path
    :return:
    '''

    # get length of parents
    parent_1 = music_1.track_list[0].feature_list
    parent_2 = music_2.track_list[0].feature_list
    length_1 = len(parent_1)
    length_2 = len(parent_2)
    shorter_length = min(length_1, length_2)

    if random.randint(0, 1):
        # 0.5 of probability the distance is positive
        distance = random.randint(0, max_distance)
    else:
        # 0.5 of probability the distance is positive
        distance = -1 * random.randint(0, max_distance)

    # the crossover point of parent 1
    point_1 = random.randint(1, shorter_length)
    # the crossover point of parent 2
    point_2 = point_1 + distance
    point_2 = max(min(length_2, point_2), 1)

    # get segments of parents cut by the crossover point
    segmentation_1_1 = parent_1[:point_1]
    segmentation_1_2 = parent_1[point_1:]

    segmentation_2_1 = parent_2[:point_2]
    segmentation_2_2 = parent_2[point_2:]

    offspring_1 = segmentation_1_1 + segmentation_2_2
    offspring_2 = segmentation_2_1 + segmentation_1_2

    # recombine to get new offspring, with maximum length limit length_limit
    offspring_1 = offspring_1[:length_limit]
    offspring_2 = offspring_2[:length_limit]

    music_1.track_list[0] = Track(offspring_1)
    music_2.track_list[0] = Track(offspring_2)

    return music_1.track_list[0], music_2.track_list[0]

'''
Mutation
'''

def reverse_mutation(music, track_index=0, feature_index=0):
    orig = music.track_list[track_index].feature_list[0][feature_index]
    #print(orig)
    orig.reverse()
    music.track_list[track_index].feature_list[0][feature_index] = orig
    return orig
def evaulation(pop,choice):
  '''
  alter the pool base on choice, by adding duplicate in it
  :param pool: 
  :param choice: 
  :return: 
  '''
  for item in pop:
    item.evaluate(rule,choice)
    print(item.fitness)

def feedmax(pop):
  '''
  TODO yapi
  返回2个分最高的
  
  :param pop: 
  :return: 
  '''
  pop = sorted(pop, key=lambda item: item.fitness, reverse=True)
  
  print(pop[0],pop[1])

def original(notes,tick):
  '''
  把原版变成一个个体，保留全部顺序
  输入原本音乐文件，
  尽量把pool里的feature带入形成一个feature 版的original TODO yapi
  :return: music 
  '''
  music_form = Music()
  for note in notes:
    music_form.track_list.append(note)
  print(music_form.track_list,'?????')    
  
        
    
  
  
  
  
if __name__ == "__main__":
  a= Music()
  b = Music()
  pop = [a,b]
  feedmax(pop)