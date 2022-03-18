


def first_rule(music):
  if music.fitness ==0:
    return 1
  else:
    return 
  
def micro_pitch_order(music1,music2):
  music1_str=""
  music2_str = ""
  for feature in music1.track_list[0].feature_list[0]:
    for note in feature:
      music1_str+=str()
  return 0

def macro_pitch_order(music1,music2):
  return levenshtein_feature(music1, music2)

def frequcncy(music):
  '''
  按照main词频获取fitness
  :param music: 
  :return: 
  '''
  return 0

def levenshtein(a, b):

  m = [[*range(len(a) + 1)] for _ in range(len(b) + 1)]
  for i in range(len(b) + 1):
    m[i][0] = i
  for i in range(1, len(b) + 1):
    for j in range(1, len(a) + 1):

      m[i][j] = min(m[i - 1][j] + 1, m[i][j - 1] + 1, m[i - 1][j - 1] + (b[i - 1] != a[j - 1]))
  return m[-1][-1]


def levenshtein_feature(music1, music2):
  a = music1.track_list[0].feature_list[0]
  b = music2.track_list[0].feature_list[0]
  m = [[*range(len(a) + 1)] for _ in range(len(b) + 1)]

  for i in range(len(b) + 1):
    m[i][0] = i

  for i in range(1, len(b) + 1):
    for j in range(1, len(a) + 1):

      aa = str([i.note for i in music2.track_list[0].feature_list[0][i - 1]])
      bb = str([i.note for i in music1.track_list[0].feature_list[0][j - 1]])
      m[i][j] = min(m[i - 1][j] + 1, m[i][j - 1] + 1, m[i - 1][j - 1] + (aa!=bb))
  print(aa)
  print(bb)
  result = m[-1][-1]
  print("result:",result)
  return result