name1=input("enter your name:")
name2=input("enter his/her name:")
combine_name=name1+name2
lower_string=combine_name.lower()
t=lower_string.count('t')
r=lower_string.count('r')
u=lower_string.count('u')
e=lower_string.count('e')
true=t+r+u+e
l=lower_string.count('l')
o=lower_string.count('o')
v=lower_string.count('v')
e=lower_string.count('e')
love=l+o+v+e
true_love=int(str(true)+str(love))
if true_love < 10 and true_love > 90:
    print(f"your love score is {true_love}")
elif true_love >= 40  and true_love <= 50:
    print(f"your love score is {true_love}")
else:
    print(f"love score is {true_love}")