def eat(breakfast, lunch, dinner='カレー', *desserts):
  print('朝は{}を食べました。'.format(breakfast))
  print('昼は{}を食べました。'.format(lunch))
  print('夜は{}を食べました。'.format(dinner))
  for d in desserts:
    print('おやつに{}を食べました。'.format(d))

eat('トースト', 'パスタ', 'カレー', 'アイス', 'チョコ', 'パフェ')

def eat1(**kwargs):
  for key in kwargs:
    print('{}に{}を食べました。'.format(key, kwargs[key]))

eat1(朝食='納豆', 遅めの昼食='パスタ', 夕方のおやつ='カレーパン')
