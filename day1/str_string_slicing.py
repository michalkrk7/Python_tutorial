selfish = "01234567"
          #01234567 -> liczenie w pythonie od 0 

# [start:stop:stepover] -> slicing (wycinanie fragmentu tekstu)

print(selfish[0]) # 0

print(selfish[0:2]) # 01

print(selfish[0:8:2]) # 0246 -> co drugi znak

print(selfish[1:5]) # 1234 -> od 1 do 5

print(selfish[:5]) # 01234 -> od początku do 5

print(selfish[::1]) # 01234567 -> od początku do końca

print(selfish[::2]) # 0246 -> co drugi znak

print(selfish[-1]) # 7 -> ostatni znak

print(selfish[-2]) # 6 -> przedostatni znak 

print(selfish[::-1]) # 76543210 -> od końca do początku