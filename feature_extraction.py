import random

class feature_pool:
  def __init__(self,pool = []):
    self.feature_pool = pool
  def new_feature(self,note,time):
    # if note exist,add time to it or create a new note
    for item in self.feature_pool:

      if item.note == note:
        return item.add_time(time)
    # not exist , new note 
    new_feature = feature(note,time)
    self.feature_pool.append(new_feature)
  def show_pool(self):
    for item in self.feature_pool:
      print('feature:',item.note,"  time:",item.time,'count:',len(item.time))
  def give_pool(self,min_count):
    pool_list = []
    for item in self.feature_pool:
      if item.count >= min_count:
        pool_list.append(item)
    return pool_list
        
        
    
    
class feature:
  def __init__(self,note,time):
    self.note = note
    self.duration = len(note)
    self.time = [time]
    self.count = 1
  def add_time(self,time):
    #if exist add count if new add  to list
    if time not in self.time:
      self.time.append(time)
    self.count +=1
    return self.time.append(time)
  def get_time(self,time):
    return time in self.time
  def get_note(self):
    return self.note

import pandas as pd

def containsPattern(feature_pool,note,time,low=3,up=5):
    for m in range (low,up+1):
      i = 0
      while i < len(note)-m+1:
          p = tuple(note[i:i+m])
          # new_feature = feature(note[i:i+m],time[i:i+m])
          feature_pool.new_feature(note[i:i+m],time[i:i+m])
          # features_list.append(new_feature)
          # if p * k == arr[i:i+m*k]:
          #     return features
          i += 1
      
    # feature_pool.show_pool()
    # return dict(result)
def make_pool(feature_dict,min_number=2):
  pool = []
  for item in feature_dict:
    if feature_dict[item] >= min_number:
      for i in range(feature_dict[item]):
        pool.append(list(item))
        
  return pool
def compose(duraiton, pool):
  cur = 0
  track = feature_pool([])
  track.show_pool()
  while cur< duraiton:
    x = random.choice(pool.feature_pool)
    track.feature_pool.append(x)
    
    cur += x.duration
  return track

def play(track):
  note = []
  time = []
  for item in track.feature_pool:
    note+=item.note
    time+=random.choice(item.time)
  
  print (note)
  print(time)
  
smk_note = [5, 7, 8,-1, 5, 7, 9, 8,-1, 5, 7, 8,-1, 7, 5]
smk_time = [1, 1, 2,1, 1, 1, 1, 2,1, 1, 1, 2,1, 1, 4]
smk_note = [5, 7, 8,-1, 5, 7, 9, 8,-1, 5, 7, 8,-1, 7, 5]+[5, 7, 8,-1, 5, 7, 9, 8,-1, 5, 7, 8,-1, 7, 5]
smk_time = [1, 1, 2,1, 1, 1, 1, 2,1, 1, 1, 2,1, 1, 4]+[1, 1, 2,1, 1, 1, 1, 2,1, 1, 1, 2,1, 1, 4]
# feature_p = feature_pool()
# containsPattern(feature_p,smk_note,smk_time,3,5)
# min3_pool = feature_pool(feature_p.give_pool(3))
# # min3_pool.show_pool()
# # pool = make_pool(x)
# 
# x1 = compose(12,min3_pool)
# x2 =compose(12,min3_pool)
# x1.show_pool()
# x2.show_pool()
# play(x2)
# print(compose(12,min3_pool))

star_note = [1,1,5,5,6,6,5,-1,4,4,3,3,2,2,1,-1,5,5,4,4,3,3,2,-1,5,5,4,4,3,3,2,-1]+[1,1,5,5,6,6,5,-1,4,4,3,3,2,2,1,-1,5,5,4,4,3,3,2,-1,5,5,4,4,3,3,2,-1]
star_time = [1,1,1,1,1,1,2,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1]+[1,1,1,1,1,1,2,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1]
feature_p = feature_pool()
containsPattern(feature_p,star_note,star_time,3,5)
min3_pool = feature_pool(feature_p.give_pool(3))
# min3_pool.show_pool()
# pool = make_pool(x)

x1 = compose(12,min3_pool)
x2 =compose(12,min3_pool)
x1.show_pool()
x2.show_pool()
play(x2)




# star_note = [1,1,5,5,6,6,5,-1,4,4,3,3,2,2,1,-1,5,5,4,4,3,3,2,-1,5,5,4,4,3,3,2,-1]
# star_time = [1,1,1,1,1,1,2,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1]
# [4, 4, 3, 3, 4, 3, 3, 2, -1, 4, 4, 3, 3, 2]
# [1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1]
# [-1, 5, 5, 4, 4, 3, 3, 4, 3, 3, 2, -1]
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1]