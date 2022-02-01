from flask import Flask, render_template, request
app = Flask('app')

def to_millis(minutes, seconds, millis):
  millis_out = (minutes * 60 + seconds) *1000 + millis
  
  return millis_out

'''
[
  {"name": "[First] [Last]", "raw_time": "minutes:seconds.millis", "millis": integer}
]
'''

@app.route('/')
def home():
    leaderboard = []
    return render_template('home.html', leaderboard=leaderboard)

app.run(host='0.0.0.0', port=8080)