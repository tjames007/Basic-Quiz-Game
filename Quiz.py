#!/usr/bin/bash

import time

print("Welcome to my Quiz!")

time.sleep(1)

# Check if user wants to play
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Awesome! Let's play! :)")
score = 0

time.sleep(1)

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct! Great Job!')
    score += 1
else:
    print("Incorrect! Need to study this one more!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct! Great Job!')
    score += 1
else:
    print("Incorrect! Need to study this one more!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct! Great Job!')
    score += 1
else:
    print("Incorrect! Need to study this one more!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print('Correct! Great job!')
    score += 1
else:
    print("Incorrect! Need to study this one more!")

print("Loading Results")

time.sleep(1)

print("You got " + str(score) + "/4 questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
