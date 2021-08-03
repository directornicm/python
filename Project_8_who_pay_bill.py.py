#who will pay the bill today
import random

name_string = input("Give the names of the group seperated by ,\n")
name_list = name_string.split(",")

print(name_list)

l = len(name_list)
bill_index = random.randint(0,l-1) # as both boundry points included and subscripts starts from 0, l will be out of range
person_will_pay = name_list[bill_index]
print(f"{person_will_pay} is going to buy meal today!")
# the above 4 line code can be replaced by the following two lines - use of choice function of random module
person_will_pay = random.choice(name_list)
print(f"{person_will_pay} is going to buy meal today!")