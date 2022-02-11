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

class Feature_pool:
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
    new_feature = Feature(note, time)
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

class Feature:
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

class Note:
  def __init__(self):
    self.channel = 0
    self.note = [-1]
    self.velocity = 0
    self.start_time = 0
    self.duration = 0


  def __init__(self, channel, note, velocity, start_time, duration):
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
    def __init__(self):
      self.note_list = []
      self.size = 0

    def note_append(self, new_note):
      self.note_list.append(new_note)
      self.size += 1

class Music:
    def __init__(self):
      self.track_list = []
      self.ticks_per_beat = 100

    def set_ticks_per_beat(self, ticks_per_beat):
      self.ticks_per_beat = ticks_per_beat

    def append_track(self, new_track):
      self.track_list.append(new_track)

    def display(self):
      for i in range(len(self.track_list)):
        print("Track:", i)
        print("Note      :", end="")
        for j in range(len(self.track_list[i].note_list)):
          print(self.track_list[i].note_list[j].note, end='\t')
        print("")
        print("Start Time:", end="")
        for j in range(len(self.track_list[i].note_list)):
          print(self.track_list[i].note_list[j].start_time, end='\t')
        print("")
        print("Duration  :", end="")
        for j in range(len(self.track_list[i].note_list)):
          print(self.track_list[i].note_list[j].duration, end='\t')
        print("")

        print("")

    # TODO
    """
    def save_midi(self,save_path = 'new_song.mid'):
        mid = MidiFile()
        for track_index in range(len(self.track_list)):

            track = MidiTrack()
            mid.tracks.append(track)
            # track.append(Message('program_change', program=12, time=0))
            for note_index in range(self.track_list[track_index].size):
                # print("有track",track_index)
                note = self.track_list[track_index].note_list[note_index]
                velocity = note.velocity
                note_note = note.note
                tick = note.tick
                channel = note.channel
                if note.type:
                    for i in note_note:
                        track.append(Message('note_on', channel=channel, note=i, velocity=velocity, time=tick))
                else:
                    for i in note_note:
                        track.append(Message('note_off', channel=channel, note=i, velocity=velocity, time=tick))
        track.append(MetaMessage('end_of_track', time=0))
        mid.ticks_per_beat=self.ticks_per_beat
        mid.save(save_path)
        """


if __name__ == "__main__":
    pass