print(type('josh'))
name = 'josh'
print(name)
print(type(['josh', 'leezche', 'graphittie']))
names = ['josh', 'leezche', 'graphittie']
print(names)

print(len(names))
# 환경변수에 추가
names.append('LC')
print(names)
# len = length
print(len(names))
# [] 안의 숫자는 컨테이너 안의 순번 (0이 제일 앞)
del(names[0])
print(names)
