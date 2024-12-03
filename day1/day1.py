# https://adventofcode.com/2024/day/1

import pandas as pd

def get_lines(filename: str):
    with open(filename, "r") as f:
      return [line.strip() for line in f.readlines() if line.strip()]

def get_left(lines):
   return [int(line.split()[0]) for line in lines]

def get_right(lines):
   return [int(line.split()[1]) for line in lines]

def get_sorted_lists(filename: str):
  lines = get_lines(filename)
  col1 = sorted(get_left(lines))
  col2 = sorted(get_right(lines))

  return (col1, col2)

def get_frequency_map(list: list[int]):
  frequencies = {} 
  for num in list:
    if num in frequencies:
      frequencies[num] = frequencies[num] + 1
    else:
      frequencies[num] = 1

  return frequencies 
   
def get_total_distance(filename: str):
  col1, col2 = get_sorted_lists(filename)
  diffs = [abs(col1[i] - col2[i]) for i in range(len(col1))]
  
  return sum(diffs)
  
def get_similarity_score(filename: str):
   col1, col2 = get_sorted_lists(filename)
   freq = get_frequency_map(col2)
   similarities = [num * freq[num] if freq.get(num) else 0 for num in col1]

   return sum(similarities)
   
if __name__ == "__main__":
  print(get_similarity_score("day1/input.txt"))