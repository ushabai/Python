import math
def paint_calculation(height, width, cover):
    area= height * width
    no_of_cans= math.ceil(area/cover)
    print(f"You will need {no_of_cans} cans of paint")
h = int(input("enter the height of wall in meters:\n"))
w = int(input("enter the height of wall in meters:\n"))
coverage = 7
paint_calculation(width=w,height=h,cover=coverage)