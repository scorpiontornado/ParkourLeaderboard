with open("input.txt") as file:
  scores = []

  for line in file:
    line = line.rstrip() # remove all whitespace characters (newlines and spaces) from the end of each line
    print(line)