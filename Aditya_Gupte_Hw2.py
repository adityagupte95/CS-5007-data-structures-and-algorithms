#   HW2 Assignment
#   Author: Aditya Gupte
#   Save this file as FIRSTNAME-LASTNAME-HW1.py


import math
#   -------
#   Part 1:
#   -------

print("Part 1a")

def rectangle(a,b):
    for k in range(b):
        for j in range(2):
            for i in range(a):
                print('*', end='')
            print(' ', end='')
        print('\n',end='')
rectangle(4,6)

print("\nPart 1b")

def triangle(n):
  for i in range (n+1):
    flag=0
    for j in range(2*i-1):
      for k in range(n-i):
        if flag==0:

          print(' ', end='')
        else:
          break;
      flag=1
      print('*',end='')
    print ('\n',end='')

triangle(6)




#   -------
#   Part 2:
#   -------
print("\n\nPart 2.1")

def clean1(lst):
    lstcpy=lst
    cleanlst=set(lstcpy)
    print(list(cleanlst))

al = [1, 2, 3, 4, 4, 4, 5, 1, 2, 1, 5]
print("before cleaning a1", al)
print("cleaned al")
clean1(al)
print("after clean al",al)



#   -------
#   Part 3:
#   -------

print("\n\nPart 3")
def clean2(lst):

    temp =list(set(lst))
    lst.clear()
    for i in temp:
        lst.append(i)

al_2 = [1, 2, 3, 4, 4, 4, 5, 1, 2, 1, 5]
print("before cleaning a1", al_2)
clean2(al_2)
print("after clean al", al_2)


#   -------
#   Part 4:
#   -------

print("\n \nPart 4")
def fct(lst):
    temp=[i for i in lst if i>=0]
    ans=[i for i in temp if math.log2(i).is_integer()]
    return ans


print("the answer is ", fct([1, 2, 3, 4, 5, 16, 255, 256, -1, -2, 84]))



#   -------
#   Part 5:
#   -------

print("\n\nPart 5")


def taylor(x,n):
    ans=0
    for i in range(1, n+1):
        temp= (-1)**(i+1)
        ans= ans+(temp*(x**((2*i)-1)/math.factorial((2*i)-1)))
    return ans


x = math.pi/2
print(math.sin(x))
print(taylor(x, 7))

#   ------------
#   Extra credit
#   ------------

print("\nExtra credit")
def consecutives(lst):
    cnt=0
    finalcnt=0
    for i in range(len(lst)):
        if lst[i] == lst[i+1]:
            cnt = cnt+1
            if cnt > finalcnt:
                finalcnt = cnt
        else:
            cnt = 0

    return finalcnt

l1 = [1,1,1,3,3,4,4,4,4,4,3,1,7,3,3,4,4]
l2 = []
l3 = [1,2,1,1,2,1,1]

print(consecutives(l1))
print(consecutives(l2))
print(consecutives(l3))

