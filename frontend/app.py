
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    try:
        response = requests.get('http://127.0.0.1:5000/api/teams')
        response.raise_for_status()
        teams = response.json()['teams']
    except requests.exceptions.RequestException:
        return render_template('index.html', error="Backend API not responding.", teams=[], result={})

    return render_template('index.html', teams=sorted(teams), result={}, player_stats=None, player_name=None)

@app.route('/teamvteam')
def team_vs_team():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')

    try:
        result = requests.get(f'http://127.0.0.1:5000/api/teamvteam?team1={team1}&team2={team2}').json()
        teams = requests.get('http://127.0.0.1:5000/api/teams').json()['teams']
    except requests.exceptions.RequestException:
        return render_template('index.html', error="Backend API not responding.", teams=[], result={}, player_stats=None, player_name=None)

    return render_template('index.html', result=result, teams=sorted(teams), player_stats=None, player_name=None)

@app.route('/player', methods=['POST'])
def player_stats():
    player_name = request.form['player']
    role = request.form['role']
    api_url = f"http://127.0.0.1:5000/api/batting-record?batsman={player_name}" if role == 'batsman' else f"http://127.0.0.1:5000/api/bowling-record?bowler={player_name}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        player_stats = response.json()
        teams = requests.get('http://127.0.0.1:5000/api/teams').json()['teams']
    except requests.exceptions.RequestException:
        return render_template('index.html', error="Backend API not responding.", teams=[], result={}, player_stats=None, player_name=None)

    return render_template('index.html', result={}, teams=sorted(teams), player_stats=player_stats, player_name=player_name)

app.run(debug=True, port=7000)
