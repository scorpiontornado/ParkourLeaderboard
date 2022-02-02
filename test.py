def to_millis(minutes, seconds, millis):
  millis_out = (minutes * 60 + seconds) *1000 + millis
  
  return millis_out

def input_data(location="input.txt"):
  with open(location) as file:
    people = []
  
    for line in file:
      line = line.rstrip() # remove all whitespace characters (newlines and spaces) from the end of each line
      print(line)

      line = line.split(",") # FIXME: do i need to assign, or does it modify in-place?

      # Assign temporary variables for readability.         # Yes I could've used a dict for this
      temp_name = line[0]
      temp_year = line[1]
      temp_house = line[2] # TODO: use year codes instead of full house names to minimise errors?
      temp_time = line[3]
      
      # TODO: same name, different year/house?

      # Search through to see if person already exists (this is spaghetti code don't @ me)
      for person in people:
        if person["name"] == temp_name and person["year"] == temp_year and person["house"] == temp_house:
          # Append time to the person's times
          person["times"].append(temp_time)
          break
      else:
        # Create new person if person not found
        people.append(
          {
            "name": temp_name,
            "year": temp_year,
            "house": temp_house,
            "times": [temp_time]
          }
        )

  return people
  
people = input_data()

print(people)