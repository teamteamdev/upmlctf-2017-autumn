#!/usr/local/bin/python3

import sys
sys.setrecursionlimit(100000)

import random, time

timeout = 60
puzzles = 40

def calc(arr):
    stack = []
    for i in arr:
        if i == "+":
            stack.append(stack.pop() + stack.pop())
        elif i == "*":
            stack.append(stack.pop() * stack.pop())
        else:
            stack.append(i)
    return stack.pop()

def gen_tree(prob = 0, level = 1):
    action = random.choice(["+", "*"])
    
    go = random.uniform(0, 1)
    
    if level < 5 and go < prob ** level:
        a = gen_tree(prob, level + 1)
        b = gen_tree(prob, level + 1)
    else:
        a = [random.randint(1, 20)]
        b = [random.randint(1, 20)]
    
    return a + b + [action]
    
 
print("Hello! I'm telling my secrets only to really cool experts in math :) Solve my puzzles fast and go on!")
solved = 0
start = time.time()

for i in range(puzzles):
    puzzle = gen_tree((i + 1) / puzzles)
    print(' '.join(map(str, puzzle)))
    
    ans = input().strip()
    if time.time() - start > timeout:
        print("Time is out")
        break
    elif ans == str(calc(puzzle)):
        print("OK, you're awesome. Next:")
        solved += 1
    else:
        print("No, it's wrong")
        break


if solved == puzzles:
  print("Good job! Flag is uctfmysecretisinsidemath")
else:
  print("Sorry, you haven't completed the mission.")
