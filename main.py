from flask import Flask, render_template, request
app = Flask('app')

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
  

'''
Old data structure:
[
  {"name": "[First] [Last]", "raw_time": "minutes:seconds.millis", "millis": integer}
]

New data structure:

OPTION 1 - only store the best time, and update each time a better one is found
[
  {
    "name": "[First] [Last]",
    "year": integer,
    "house": String,
    "raw_time": "minutes:seconds.millis",
    "millis": integer
  }
]

OPTION 2 - calculate the best time (in millis) for each person/dictionary
[
  {
    "name": "[First] [Last]",
    "year": integer,
    "house": String,
    "raw_times": ["minutes:seconds.millis"],      
    "best_millis": integer
  }
]

OPTION 3 - only store raw times, and sort using a function as a key which converts times to millis and then returns the best time
[
  {
    "name": "[First] [Last]",
    "year": integer,
    "house": String,
    "times": ["minutes:seconds.millis"],
  }
]

Option 3 seems the cleanest, given that the millis are only used for sorting and not for display
'''

@app.route('/')
def home():
    leaderboard = []
    return render_template('home.html', leaderboard=leaderboard)

app.run(host='0.0.0.0', port=8080)