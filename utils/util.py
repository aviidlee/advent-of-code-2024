def get_lines(filename: str):
    with open(filename, "r") as f:
      return [line.strip() for line in f.readlines() if line.strip()]