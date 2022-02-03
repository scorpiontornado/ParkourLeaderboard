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

def process_time(time):
  """ Return minutes, seconds, millis from a string in the form minutes:seconds.millis """
  minutes, seconds_millis = time.split(":")
  seconds, millis = seconds_millis.split(".")

  return minutes, seconds, millis

def to_millis(minutes, seconds, millis):
  """ Convert minutes, seconds, millis to millis """
  millis_out = (int(minutes) * 60 + int(seconds)) *1000 + int(millis)
  
  return millis_out

def best_time(person):
  times = person["times"]

  times_sorted = times.sort(key=lambda time: to_millis(process_time(time)))

  return times_sorted[0] # Return the best time
  
people = input_data()
print(people)
people_sorted = people.sort(key=lambda person: to_millis(best_time(person)))
print(people_sorted)