import random

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


  def __init__(self, channel=0, note=[-1], velocity=0, start_time=0, duration=0):
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
    print("Note", self.channel, self.note, self.velocity, self.start_time, self.duration)

class Track:
    def __init__(self,note_list=[]):
      self.note_list = note_list
      self.size = 0

    def note_append(self, new_note):
      self.note_list.append(new_note)
      self.size += 1

class Music:
    def __init__(self,track_list=[]):
      self.track_list = track_list
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
def one_pt_crossover(music_1, music_2, max_distance=4, length_limit=100):
    '''

    :param parent_1: individual 1
    :param parent_2: individual 1
    :param max_distance:  the distance between the crossover points on two individuals
    :param length_limit: the maximum length of path
    :return:
    '''

    # get length of parents
    parent_1 = music_1.track_list[0].note_list
    parent_2 = music_2.track_list[0].note_list
    length_1 = len(parent_1)
    length_2 = len(parent_2)
    shorter_length = min(length_1,length_2)


    if random.randint(0,1):
        # 0.5 of probability the distance is positive
        distance = random.randint(0,max_distance)
    else:
        # 0.5 of probability the distance is positive
        distance = -1 * random.randint(0,max_distance)

    # the crossover point of parent 1
    point_1 = random.randint(0, shorter_length)
    # the crossover point of parent 2
    point_2 = point_1 + distance
    point_2 = max(min(length_2,point_2),0)

    # get segments of parents cut by the crossover point
    segmentation_1_1 = parent_1[:point_1]
    segmentation_1_2 = parent_1[point_1:]

    segmentation_2_1 = parent_2[:point_2]
    segmentation_2_2 = parent_2[point_2:]

    offspring_1 = segmentation_1_1+segmentation_2_2
    offspring_2 = segmentation_2_1+segmentation_1_2

    # recombine to get new offspring, with maximum length limit length_limit
    offspring_1 = offspring_1[:length_limit]
    offspring_2 = offspring_2[:length_limit]

    music_1.track_list[0] = Track(offspring_1)
    music_2.track_list[0] = Track(offspring_2)

    return music_1.track_list[0], music_2.track_list[0]

if __name__ == "__main__":
    # test one_pt_crossover()
    music_1 = Music([])
    track_1 = Track([])
    music_1.append_track(track_1)


    music_2 = Music([])
    track_2 = Track([])
    music_2.append_track(track_2)


    for i in range(10):
      track_1.note_append(Note(0,[i],0,0,0))


    for i in range(10):
      track_2.note_append(Note(0, [i+100], 0, 0, 0))

    print("music_1")
    music_1.display()
    print("music_2")
    music_2.display()

    one_pt_crossover(music_1,music_2)

    print("music_1")
    music_1.display()
    print("music_2")
    music_2.display()







    pass


