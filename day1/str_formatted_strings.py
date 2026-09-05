# formatted strings (f-strings) 

name = "John"
age = 36

print("hi " + name + ". You are " + str(age) + " years old.") # hi John. You are 36 years old.

print(f"hi {name}. You are {age} years old.") # hi John. You are 36 years old. -> f-string (formatted string) uzywając {}

print("hi {1}. You are {0} years old.".format(name, age)) # hi 36. You are John years old. NIE POTRZEBNE f LEPSZE 