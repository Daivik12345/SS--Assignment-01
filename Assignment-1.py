#Qs 1
L = [11, 12, 13, 14]


L.append(50)
L.append(60)
print("After adding 50 and 60:", L)


L.remove(11)
L.remove(13)
print("After removing 11 and 13:", L)


L.sort()
print("Sorted in ascending order:", L)


L.sort(reverse=True)
print("Sorted in descending order:", L)


print("13 in L:", 13 in L)


print("Number of elements in L:", len(L))


print("Sum of all elements in L:", sum(L))

sum_odd = sum(x for x in L if x % 2 != 0)
print("Sum of all odd numbers in L:", sum_odd)


sum_even = sum(x for x in L if x % 2 == 0)
print("Sum of all even numbers in L:", sum_even)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

sum_prime = sum(x for x in L if is_prime(x))
print("Sum of all prime numbers in L:", sum_prime)


L.clear()
print("After clearing all elements:", L)


del L
try:
    print(L)
except NameError:
    print("L is deleted")  
    
#Qs 2
D = {1: 5.6, 2: 7.8, 3: 6.6, 4: 8.7, 5: 7.7}


D[8] = 8.8
print("After adding key=8:", D)


del D[2]
print("After removing key=2:", D)


print("Is key=6 present:", 6 in D)


print("Number of elements in D:", len(D))


print("Sum of all values in D:", sum(D.values()))


D[3] = 7.1
print("After updating key=3:", D)


D.clear()
print("After clearing the dictionary:", D)

#Qs 3
S1 = {10, 20, 30, 40, 50, 60}
S2 = {40, 50, 60, 70, 80, 90}


S1.add(55)
S1.add(66)
print("After adding 55 and 66:", S1)


S1.discard(10)
S1.discard(30)
print("After removing 10 and 30:", S1)


print("Is 40 present in S1:", 40 in S1)


print("Union of S1 and S2:", S1.union(S2))


print("Intersection of S1 and S2:", S1.intersection(S2))


print("S1 - S2:", S1.difference(S2))

#Qs 4

import random
import string


for _ in range(100):
    length = random.randint(6, 8)
    rand_str = ''.join(random.choices(string.ascii_letters, k=length))
    print(rand_str)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [n for n in range(600, 801) if is_prime(n)]
print("Prime numbers between 600 and 800:", primes)


divisibles = [n for n in range(100, 1001) if n % 7 == 0 and n % 9 == 0]
print("Numbers between 100 and 1000 divisible by 7 and 9:", divisibles)


#Qs 5

import random


list1 = [random.randint(10, 30) for _ in range(10)]
list2 = [random.randint(10, 30) for _ in range(10)]

print("List1:", list1)
print("List2:", list2)


common = set(list1).intersection(list2)
print("Common numbers:", common)


unique = set(list1).symmetric_difference(list2)
print("Unique numbers:", unique)


print("Minimum in list1:", min(list1))
print("Minimum in list2:", min(list2))


print("Maximum in list1:", max(list1))
print("Maximum in list2:", max(list2))


print("Sum of list1:", sum(list1))
print("Sum of list2:", sum(list2))
print("Total sum:", sum(list1) + sum(list2))


#Qs 6

import random


random_numbers = [random.randint(100, 900) for _ in range(100)]


odd_numbers = [num for num in random_numbers if num % 2 != 0]
print("Odd numbers:", odd_numbers)


even_numbers = [num for num in random_numbers if num % 2 == 0]
print("Even numbers:", even_numbers)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = [num for num in random_numbers if is_prime(num)]
print("Prime numbers:", prime_numbers)


#Qs 7

D = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}

with open("output.txt", "w") as file:
    for key, value in D.items():
        file.write(f"{key}, {value} ")


#Qs 8

L = ["One", "Two", "Three", "Four", "Five"]

with open("output.txt", "w") as file:
    for item in L:
        file.write(f"{item}, {len(item)} ")


#Qs 9

import random
import string

with open("output.txt", "w") as file:
    for _ in range(100):
        length = random.randint(10, 15)
        rand_str = ''.join(random.choices(string.ascii_letters, k=length))
        file.write(rand_str + "\n")


#Qs 10

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

with open("output.txt", "w") as file:
    for num in range(600, 801):
        if is_prime(num):
            file.write(f"{num}\n")


#Qs 11

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

with open("output.txt", "w") as file:
    for num in range(600, 801):
        if is_prime(num):
            file.write(f"{num}\n")









    
    
