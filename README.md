A simple Flask website to display a leaderboard of the results of Westminster's Minecraft parkour competition for SACS' MakeOff

Currently hosted using repl. See:
  * https://replit.com/@NicholasLangfor/ParkourLeaderboard
  * https://ParkourLeaderboard.nicholaslangfor.repl.co

# Use 
The webstite only has one (root) directory/webpage, which displays a sorted list of people and their times (with the best times at the top)

# Input
The times are inputted manually into the file "readme.txt" in the format:
`[firstname] [lastname], [year], [house], [time minutes:seconds.milliseconds]`

E.g. if Nicholas Langford in Year 12 Westminster got a time of 1 minute, 47 seconds and 89 milliseconds, the following would be inputted into "input.txt":
`Nicholas Langford, 12, Westminster, 1:47.89`

Each entry is separated by a newline character ("enter" or "return" on a keyboard)
