import mido
#TODO 修改代码
'''
https://www.bilibili.com/read/cv9432479'''
def midi_read(filename):
  mid = mido.MidiFile(filename)  # 返回midi对象
  print(mid)
  tick= mid.ticks_per_beat
  hang = 0  # 行
  lie = 0  # 列
  note_list_in = []  # 先初步建立一个序列，用于存储一行音符数据。
  note_list_ex = []  # 先初步建立一个序列，用于存储整个音符数据。
  # 存储时间的序列
  time_list = []
  action_last = 0  # 上轮动作状态，0 表示没有按下； 1 表示按下；
  action = 0  # 本轮动作状态， 0 表示没有按下； 1 表示按下；
  for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
      print(msg)
      # 说明是按下了action就置1
      if msg.type == "note_on" and msg.velocity!=0:
        action = 1
        # 连着两个都按下了,就是和弦,在这个序列中添加一个音符.
        if action == action_last:
          note_list_in.append(msg.note)
        # 如果上轮没有按下,本轮按下了.
        # 就要开启新的一个序列.
        if action != action_last:
          hang = hang + 1
          if hang != 1:
            # 开启新的一行前，先要保存数据到外面层。
            # 保存上次的序列,加入到二维中(就是外层中)
            note_list_ex.append(note_list_in)
            # print("hang=",hang-1,"   ",note_list_in)
          # 要清空内部序列，以便存入新一行的数据。
          note_list_in = []
          note_list_in.append(msg.note)

      '''
      只有在松开 note_off 的时候才会有时间参数.
      '''
      # 第三种情况,上面是按下的两种情况.
      # 下面就是松开的两种情况.
      if msg.type == "note_off" or (msg.type == "note_on" and int(msg.velocity)==0):
        action = 0
        if action == action_last:
          pass
        if action != action_last:
          time_list.append(msg.time)
      action_last = action

  note_list_ex_sort = []
  for note_list_in in note_list_ex:
    note_list_in_set = set(note_list_in)  # 把序列转换成集合,目的是为了去除里面重复的元素.
    note_list_in = list(note_list_in_set)  # 去重后,把集合转换成序列.
    note_list_in = sorted(note_list_in)  # 排序
    note_list_ex_sort.append(note_list_in)  # 排完序后的二维音符序列.

  for i in note_list_ex_sort:
    print(i)
    
  return [note_list_ex_sort, time_list],tick

