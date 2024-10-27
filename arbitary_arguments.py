#def add(*numbers):
 #   c=0
  #  for i in numbers:
   #     c= c + i
    #print(f"Sum is {c}")
#add(1,2)
#add(2,54,9)
#def add(*numbers, name):
#    c=0
#    print(numbers)
#    print(name)
#    for i in numbers:
 #       c= c + i
 #   print(f"Sum is {c}")
#add(2,7,name="usha")
#def add(a,*numbers):
 #   c=0
  #  print("a =",a)
   # print(numbers)
    #for i in numbers:
     #   c+=i
    #print(f"sum is {c}")
#add(1,2,8)
#add(1,5,6,7,8,9)
#add(4,9,6,6.6)
#def info_person(*args,**kwargs):
 #   for key,value in kwargs.items():
  #      print(key,value)
   # print(args)
#info_person(1,2,name="usha",dept="cse")
#info_person(3,5,name="nisha",age=30,dept="ise")
def multiply(*numbers):
    c=1
    for i in numbers:
        c= c * i

    print(f"product is {c}")
multiply(2,3,-6,8)
