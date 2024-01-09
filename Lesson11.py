from ast import If
import collections
from math import factorial

#1
def fact(n):
    f = factorial(n)
    return f
    
print("Введите число:")
n = int(input())
sp = []
while n >= 1:
    sp.append(fact(n))
    n+= -1
    
print(sp)


#2
pets={}

def get_pet(pets, ID):
  if ID in pets.keys():
   return pets[ID] 
  else:
    False

def get_suffix(age):
  GG = "года"

  if age%10 == 0 or age%10 >5 or (age > 5 and age < 21): 
     GG = "лет"
  elif age%10 == 1:
     GG = "год"
  return GG

def pets_list(pets):
  for IDpets in pets:
    print(pets[IDpets])

def create(pets):
 
  if len(pets) > 0:
    last = collections.deque(pets, maxlen=1)[0]+1 
  else: last =1
   
  IDpets = {}
  
  print("введите имя питомца:")
  pitomets = input()
  
  slPit ={}

  print("введите вид питомца:")
  slPit["Вид питомца"] = input()
  print("введите возраст питомца:")
  slPit["Возраст питомца"] = int(input())
  print("введите имя владельца:")
  slPit["Имя владельца"] = input()

  IDpets[pitomets] = slPit
  pets[last] = IDpets

def read(pets):
  
  print("Введите ID питомца:")
  ID = int(input())

  slPr = get_pet(pets, ID)

  if slPr == False:
   print("питомец с ID " + str(ID) + " не определен")
   return
  
  pitomets = list(slPr.keys())[0]
  
  slPit = slPr[pitomets]

  keysPit = list(slPit.keys())

  ValuesPit = list(slPit.values())

  GG = get_suffix(ValuesPit[1])

  print("Это " + ValuesPit[0] + " по кличке " + pitomets + ". " + str(keysPit[1]) + ": " + str(ValuesPit[1]) + " " + GG + ". " +  str(keysPit[2]) + ": "+ str(ValuesPit[2]))

 #print(pets)

def update(pets):
  
  print("введите ID питомца:")
  ID = int(input()) 
  
  IDpets = get_pet(pets, ID)

  if IDpets == False:
   print("питомец с ID " + str(ID) + " не определен")
   return
  
  IDpets.clear()

  print("введите имя питомца:")
  pitomets = input()
  slPit ={}
  print("введите вид питомца:")
  slPit["Вид питомца"] = input()
  print("введите возраст питомца:")
  slPit["Возраст питомца"] = int(input())
  print("введите имя владельца:")
  slPit["Имя владельца"] = input()

  IDpets[pitomets] = slPit
  pets[ID] = IDpets

def delete(pets):
  
  print("введите ID питомца:")
  ID = int(input()) 
  
  IDpets = get_pet(pets, ID)

  if IDpets == False:
   print("питомец с ID " + str(ID) + " не определен")
   return
  else:
    pets.pop(ID)
    print("элемент удален")


while True:
 print("введите команду: create, update, read, delete, pets_list, stop")
 command = input()
 if command == "create":
  create(pets)
 elif command == "update":
  update(pets)
 elif command == "read":
  read(pets)
 elif command == "delete":
  delete(pets)
 elif command == "pets_list":
  pets_list(pets)
 elif command == "stop":
  break
 else:
  print("команда введена неверно")