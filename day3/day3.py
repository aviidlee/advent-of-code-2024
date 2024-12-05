import re
from enum import Enum, auto 
from __future__ import annotations

class Instruction(Enum):
  MULT = auto()
  DO = auto()
  DONT = auto()

  @staticmethod
  def get_instruction(instruction: str) -> Instruction:
    if 'mul' in instruction:
      return Instruction.MULT
    elif instruction == "do()":
      return Instruction.DO
    elif instruction == "don't()":
      return Instruction.DONT
    else:
      raise ValueError(f"Invalid Instruction {Instruction}")
    

def get_matches(input: str) -> list[str]:
  pattern = r'mul\(\d+,\d+\)'
  return re.findall(pattern, input)

def get_instructions(input:str) -> list[str]:
  pattern = r'mul\(\d+,\d+\)|don\'t\(\)|do\(\)'
  return re.findall(pattern, input)

def get_dos(instructions: list[str]) -> list[str]:
  multiply = []
  enabled = True 

  for instruction in instructions:
    inst = Instruction.get_instruction(instruction)
    match inst: 
      case Instruction.MULT:
        if enabled:
          multiply.append(instruction)
      case Instruction.DO:
        enabled = True 
      case Instruction.DONT:
        enabled = False 
      case _: 
        raise ValueError(f"Unknown instruction {inst}")

  return multiply

def multiply(input: list[str]) -> int:
  mul_pairs = parse(input)
  
  return sum([a*b for (a,b) in mul_pairs])
  

def parse(input: list[str]) -> list[tuple[int]]:
  pattern = r'(\d+),(\d+)'
  numbers = []
  for mul in input: 
    match = re.search(pattern, mul)
    numbers.append((int(match.group(1)), int(match.group(2))))
  
  return numbers

def get_solution_part1(raw_input: str) -> int: 
  matches = get_matches(raw_input)

  return multiply(matches)

def get_solution_part2(raw_input: str) -> int:
  instructions = get_instructions(raw_input)
  dos = get_dos(instructions)

  return multiply(dos)

if __name__ == "__main__":
  with open('input.txt', 'r') as file:
    content = file.read()
    print(get_solution_part2(content))
