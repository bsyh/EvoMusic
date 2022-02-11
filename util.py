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

class feature_pool:
  def __init__(self):
    self.feature_pool = []
  def __init__(self, pool):
    self.feature_pool = pool

  def new_feature(self, note, time):
    # if note exist,add time to it or create a new note
    for item in self.feature_pool:
      if item.note == note:
        return item.add_time(time)
    # not exist , new note 
    new_feature = feature(note, time)
    self.feature_pool.append(new_feature)

  def show_pool(self):
    for item in self.feature_pool:
      print('feature:', item.note, "  time:", item.time, 'count:', len(item.time))

  def give_pool(self, min_count):
    pool_list = []
    for item in self.feature_pool:
      if item.count >= min_count:
        pool_list.append(item)
    return pool_list


class feature:
  def __init__(self, notes):
    '''
    note is a list of note objects
    :param notes: 
    '''
    self.name = (note.note for note in notes)
    self.notes = notes
    # self.duration = notes
    # self.time = [time]
    # self.count = 1

  def add_phenotype(self, notes):
    # if exist add count if new add  to list
    time = (note.time for note in notes)
    if time not in self.time:
      self.time.append(time)
    self.count += 1
    return self.time.append(time)

  def get_time(self, time):
    return time in self.time

  def get_note(self):
    return self.note


class note:
  def __init__(self):
    self.channel = 0
    self.note = [-1]
    self.velocity = 0
    self.time = 0
    self.duration = 0
    self.type = True

  def __init__(self, channel, note, velocity, time, duration,note_type=True):
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
    self.time = time
    self.duration = duration

    self.type = note_type

  def set_channel(self, channel):
    self.channel = channel

  def set_note(self, note):
    self.note = note

  def set_velocity(self, velocity):
    self.velocity = velocity

  def set_tick(self, tick):
    self.tick = tick

  def set_type(self, type):
    self.type = type

  def display(self):
    print("Note", self.channel, self.note, self.velocity, self.tick)

if __name__ == "__main__":
    note1 = Note(13,40,80,100,True)
    note1.display()