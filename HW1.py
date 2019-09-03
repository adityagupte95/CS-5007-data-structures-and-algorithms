#   HW1 Assignment 
#   Author: Aditya Gupte
#   Save this file as FIRSTNAME-LASTNAME-HW1.py


import math
#   -------
#   Part 1:
#   -------

print("Part 1")

#   Let the following variables be defined with the following
#   values

a = 5.0
b = 2.5
c = 9.0

#   1a: (write expression in place of the zero in the next line)
expr_1a = (4*a*b) + (b*c)
print("The value of expression 1a is", expr_1a)

#   1b: (write expression in place of the zero in the next line)
expr_1b = b**3
print("The value of expression 1b is", expr_1b)

#   1c: (write expression in place of the zero in the next line)
expr_1c = math.sqrt(b*a)
print("The value of expression 1c is", expr_1c)

#   1d: (write expression in place of the zero in the next line)
expr_1d = (a*c + b*a)/(b*c)
print("The value of expression 1d is", expr_1d)

#   1e: (write expression in place of the zero in the next line)
expr_1e = a**2 - b**4 +2*a*b
print("The value of expression 1e is", expr_1e, "\n")

#   -------
#   Part 2:
#   -------

print("Part 2")

#   2a: (write expression in place of the zero in the next line)
expr_2a = (8//6)*6 
print("The value of expression 2a is", expr_2a)

#   2b: (write expression in place of the zero in the next line)
expr_2b = (8/6)*6
print("The value of expression 2b is", expr_2b)

#   Write here your comment (max. two sentences)
# "//" operator in python is the division operator where the answer
# is floored ie. rounded to the nearest smallest integer hence 8//6 =1
#"/" is normal floating point division. hence 8/6= 1.333333....
#
#
#
#
#
#



#   -------
#   Part 3:
#   -------

print("\nPart 3")

#   Let the following variables be defined with the following
#   values

a = True
b = False
c = False

#   3a: (write expression in place of the True in the next line)
expr_3a = a and (b or c)
print("The value of expression 3a is", expr_3a)

#   3b: (write expression in place of the True in the next line)
expr_3b = not a or (b or c)
print("The value of expression 3b is", expr_3b)

#   3c: (write expression in place of the True in the next line)
expr_3c = (a and b )or (not c)
print("The value of expression 3c is", expr_3c)

#   3d: (write expression in place of the True in the next line)
expr_3d = not a or (not b or (not c))
print("The value of expression 3d is", expr_3d)

#   -------
#   Part 4:
#   -------

print("\nPart 4")

#   1) Write here your windChill function.

def WindChill(temp, vel):
    windchill = 13.13 + 0.621 * temp-12.1 *vel**0.15 + 0.3967*temp*vel**0.16
    print ("At",temp,"and",vel,"kph winds , it feels like ",windchill)





#   Call here your windChill function with arguments -20 for T and 30 for V. 
WindChill(-20,30)




#   2) Write here your windChill2 function.
def WindChill2(temp, vel):
    windchill = 13.13 + 0.621 * temp-12.1 *vel**0.15 + 0.3967*temp*vel**0.16
    return windchill







#   Call here your windChill2 function with arguments -20 for T and 30 for V.
#   Print the result of this call. 
answer = WindChill2(-20 ,30)
print("At -20 and 30 kph winds , it feels like ", answer)






#   -------
#   Part 5:
#   -------

print("\nPart 5")

#   List here the 5 errors in the Python function euc
#1) the two parameters of the function euc() have same names "y1 and
# y1",using y2 while calculating gamma will lead to an unresolved
# #reference

#2)lambda is a keyword in python and cannot be used as a variable
# name

#3) return statement needs to be indented and be under the
# function definition

#4) do not use the floored division"1//2", use "1/2"

#5)print("result") will lead to just printing the word result
#the correct way is print(result), this will display the value of
# result


#   Write correcly the function, the call of this function and
#   the print statement:
def euc(x1,y1,x2,y2):
    lmda = (x1-x2)**2
    gamma = (y1-y2)**2
    return (lmda+gamma)**(1/2)


result = euc(1,3,2,7)
print("result= ",result )













#   ------------
#   Extra credit
#   ------------

print("\nExtra credit")

def myFct(value):
    if(value==1):
        return value
    else:
        return value+myFct(value-1)

res=myFct(3)
print(res)
#   Write here your comment: the function implements the summation
#   function. If given a number it adds up all the natural numbers
#   equal and less than the the number given as the argument.
#
#
#
#

#   Write here a simpler function, doing the same without
#   if/else statements and without re-calling myFct

def myFct2(value):
    # Write here the code of the function in place of the print('TODO')
    return (value*(value+1)/2)

res=myFct2(4)
print(res)
# END
