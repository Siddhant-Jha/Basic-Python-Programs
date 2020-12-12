from math import sqrt

print("Welcome To Pythagorus Solver App")
base = float(input("Enter The Base Of The Right Angle Triangle:\t"))
height = float(input("Enter The Height Of The Right Angle Triangle:\t"))
hypo = sqrt(base**2 + height**2)

hypo = round(hypo,2)

print("Base Of The Triangle Is:\t"+ str(base))
print("Height Of The Triangle Is:\t"+ str(height))
print("Hence, Hypo Of The Triangle Is:\t"+ str(hypo))