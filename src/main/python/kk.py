#!/usr/local/bin/python3
"""
This is the KrisKringulator.

It is a script that uses python (2.7+) to create a set of files containing the
name of the person for whom a participant in the Kris Kringle needs to buy a
gift. That is, it creates a file named after the buyer, with the name of the
buyer's recipient inside the file.

Based on an algorithm mentioned by Ryan Sattler.

This is designed to preserve the anonymity of all receivers. Simply send the
resulting files to the names of the file.

To use the application, by example:

>>> python kk.py outcome peter fred joanne gary jane

This will generate the following files:
./outcome/fred.txt
./outcome/gary.txt
./outcome/jane.txt
./outcome/joanne.txt
./outcome/peter.txt

Note: outcome can be a path. The code will create all intervening directories
in the path. However, the path (leaf) most not pre-exist, or the script will
fail, with an error message.

"""


import sys
import random
import os


def create_gifting(result_dir, participant_from, participant_to):
    with open(os.path.join(result_dir, participant_from + '.txt'), 'wt') as f:
        f.write("%s buys for %s.\n" % (participant_from, participant_to))
        f.close()


def initialize_result_directory(result_dir):
    if os.path.exists(result_dir):
        print("The result directory must not already exist:", result_dir)
        exit()
    os.makedirs(result_dir)


if len(sys.argv) < 3 :
    print("Usage:", sys.argv[0], "result_directory participant1 participant2 ...")
    exit(1)

result_dir = sys.argv[1]
initialize_result_directory(result_dir)

participants = sys.argv[2:]

random.shuffle(participants)

for index in range(0, len(participants) - 1):
    create_gifting(result_dir, participants[index], participants[index + 1])
create_gifting(result_dir, participants[len(participants) - 1], participants[0])
