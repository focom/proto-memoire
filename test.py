# Author: Pierre Valentin
# Date: 2018/11/05 

def main ():
  n3=0
  n7=0
  n37=0
  e3 = int(input("D3 = "))
  e7 = int(input("D7 = "))
  e37 = int(input ("D37 = "))
  number = 0

  while (not loopCondition(e3,e7,e37,n3,n7,n37)):
    number = number +1
    print(number, end="")
    if ((number % 3)==0):
      print (" D3", end="")
      n3 = n3 + 1
    if ((number % 7) == 0 ):
      print (" D7", end="")
      n7 = n7 + 1
    if ((number % 37 )==0):
      print (" D37", end="")
      n37 = n37 + 1
    print ('\n')
  print("DONE")
   


def loopCondition (e3,e7,e37,n3,n7,n37):
  if (e3 <= n3 and e7 <= n7 and e37 <= n37):
    return True
  else:
    return False 

main()