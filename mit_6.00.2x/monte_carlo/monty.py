#!/usr/bin/env python

import random

def choose_car_doors(doors, num_cars):
  # Put cars behind random doors
  while doors.count('c') < num_cars:
    random_door = random.choice(range(len(doors)))
    if doors[random_door] not in ['c', 'x']:
      doors[random_door] = 'c'
  #print("In choose_car_doors, doors = %s" % doors)
  return doors

def remove_random_goat_door(doors):
  starting_num_goats = doors.count('g')
  while doors.count('g') == starting_num_goats:
    random_door = random.choice(range(len(doors)))
    # look for a door with a goat and remove it
    if doors[random_door] == 'g':
      doors[random_door] = 'o'
  #print("In remove_random_gost_door, doors = %s" % doors)
  return doors

def run_sim(num_doors, num_cars, numTrials):
  num_cars_found = 0
  for n in range(numTrials):
    # Initialize doors with goats
    doors = [ 'g' for x in range(num_doors) ]
    # Then pick doors to put cars behind
    doors_with_cars = choose_car_doors(doors, num_cars)
    # contestant picks one at random
    doors[random.choice(range(len(doors)))] = 'x'
    #print("After picking random door, doors = %s" % doors)
    doors_with_one_removed = remove_random_goat_door(doors_with_cars)
    # truly remove picked and random_goat_door from list
    doors_with_one_removed.pop(doors_with_one_removed.index('x'))
    #print doors_with_one_removed
    doors_with_one_removed.pop(doors_with_one_removed.index('o'))
    second_random_choice = random.choice(range(len(doors_with_one_removed)))
    if doors_with_one_removed[second_random_choice] == 'c':
      num_cars_found += 1
  return num_cars_found/float(numTrials)


trial_sims = 10000
trial_params = [ (3,1), (4,2) ]

for trial_index in range(len(trial_params)):
    trial = trial_params[trial_index]
    doors, cars = trial_params[trial_index]
    print("Odds for %i doors and %i cars = %06f" % (
                 doors, cars, run_sim(doors, cars, trial_sims)
     ))
