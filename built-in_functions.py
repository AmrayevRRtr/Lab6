ex1
from functools import reduce

mylist = list(map(int, input().split()))
def result(mylist):
    return reduce(lambda x, y: x*y, mylist)
res = result(mylist)
print(res)

ex2
text = input()
def count_upper_lower(text):
    res1 = sum(1 for char in text if char.isupper())
    res2 = sum(1 for char in text if char.islower())

    print("Number of uppercase letters: ", res1)
    print("Number of lowercase letters: ", res2)
count_upper_lower(text)

ex3
text = input()
list_text = []
pal = reversed(text)
pal_text = []
for i in text:
    list_text.append(i)
for x in pal:
    pal_text.append(x)
if pal_text == list_text:
    print("Palindrome!")
else:
    print("Unfortunately, no")

ex4
import math
import threading

num = int(input())
milli = float(input())
def delayed_sqrt(num, milli):
    seconds = milli/1000
    def sqrt():
        result = math.sqrt(num)
        print("Square root of", num, "after", milli, "milliseconds is", result)
    timer = threading.Timer(seconds, sqrt)
    timer.start()
delayed_sqrt(num, milli)


ex5
my_true_tuple = tuple((True, True, True))
my_false_tuple = tuple((True, True, True, False))
def is_true(mytuple):
    x = all(mytuple)
    print(x)
is_true(my_true_tuple)
is_true(my_false_tuple)