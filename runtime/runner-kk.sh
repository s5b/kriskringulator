#!/usr/bin/env bash
# This is the Kris Kringle runner, for the Begg generations.
# (The first line declaration allows the script to use the latest bash on macOS.)
#
# The generations are defined in the 'participants' associative array.
# The actual participants are defined in the participants file. See participants.example
# to see how to define the participants.
#
# The results are created in a directory structure that is suffixed with the year,
# which is provided as an argument to the script. Examplw: 2019
#
# Running example: ./runner_kk.sh 2019
# - will create the output directories under './data/kk-2019/...'
#

declare -A participants
source ./participants


# Location of the script to do the matching.
APP=../src/main/python/kk.py

# Definitions for the output.
OUTPUT_DIR=./data
PREFIX='kk-'

if [[ $# -lt 1 ]] ; then
  echo "Usage: ${0} year"
  exit 1
fi

YEAR=${1}

for key in ${!participants[*]}; do
   output="${OUTPUT_DIR}/${PREFIX}${YEAR}/${key}"
   echo "Generating into '${output}' for ${participants[${key}]}."
  ${APP} ${output} ${participants[${key}]}
done


