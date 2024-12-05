import sys
sys.path.append("/home/alex/Code/aoc2024")

import utils.util as utils

def load_reports(filename: str):
  lines = utils.get_lines(filename)
  return [[int(token) for token in line.split()] for line in lines]

def is_safe(report: list[int]):
  for i in range(len(report)-1): 
    diff = report[i+1] - report[i]
    if abs(diff) < 1 or abs(diff) > 3:
      return False 
    if i > 0:
      previous_diff = report[i] - report[i-1]
      if previous_diff * diff < 0: 
        return False 
  
  return True

def safe_when_dampened(report: list[int]) -> bool:
  for i in range(len(report)):
    report_without_num = report[:i] + report[i+1:]
    if is_safe(report_without_num):
      return True 
  
  return False

def num_safe_reports_with_dampening(reports: list[list[int]]):
  return len(list(filter(safe_when_dampened, reports)))


def num_safe_reports(reports: list[list[int]]):
  return len(list(filter(is_safe, reports)))


if __name__ == "__main__":
  reports = load_reports("input.txt")
  print(num_safe_reports_with_dampening(reports))