import random
import time

first_number = random.randrange(1, 3)
second_number = random.randrange(1, 3)
third_number = random.randrange(1, 3)

print("YOUR NUMBER: ")
time.sleep(2)
print(first_number)
time.sleep(2)
print(second_number)
time.sleep(2)
print(third_number)

time.sleep(1)
print("YOUR NUMBER is ", end="")
print(first_number, end="")
print(second_number, end="")
print(third_number)
#finish


