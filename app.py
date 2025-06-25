from flask import Flask, render_template, request, jsonify
import ipl
import jugaad
import json
from difflib import get_close_matches
from team_aliases import team_aliases
from player_aliases import player_aliases

app = Flask(__name__)

def standardize_team(name):
    return team_aliases.get(name.strip().lower(), name)

def standardize_player(name):
    key = name.strip().lower()
    if key in player_aliases:
        return player_aliases[key]
    match = get_close_matches(key, [p.lower() for p in jugaad.player_names], n=1, cutoff=0.6)
    if match:
        index = [p.lower() for p in jugaad.player_names].index(match[0])
        return jugaad.player_names[index]
    return name

@app.route('/api/teams')
def teams():
    return jsonify(ipl.teamsAPI())

@app.route('/api/teamvteam')
def teamvteam():
    team1 = standardize_team(request.args.get('team1'))
    team2 = standardize_team(request.args.get('team2'))
    return jsonify(ipl.teamVteamAPI(team1, team2))

@app.route('/api/team-record')
def team_record():
    team_name = standardize_team(request.args.get('team'))
    return jugaad.teamAPI(team_name)

@app.route('/api/batting-record')
def batting_record():
    batsman_name = standardize_player(request.args.get('batsman'))
    return jugaad.batsmanAPI(batsman_name)

@app.route('/api/bowling-record')
def bowling_record():
    bowler_name = standardize_player(request.args.get('bowler'))
    return jugaad.bowlerAPI(bowler_name)

@app.route('/')
def home():
    try:
        teams = ipl.teamsAPI()['teams']
    except Exception:
        return render_template('index.html', error="Data loading failed", teams=[], result={}, player_stats=None, player_name=None)
    return render_template('index.html', teams=sorted(teams), result={}, player_stats=None, player_name=None)

@app.route('/teamvteam')
def team_vs_team():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    team1 = standardize_team(team1)
    team2 = standardize_team(team2)
    try:
        result = ipl.teamVteamAPI(team1, team2)
        teams = ipl.teamsAPI()['teams']
    except Exception:
        return render_template('index.html', error="Backend logic failed", teams=[], result={}, player_stats=None, player_name=None)
    return render_template('index.html', result=result, teams=sorted(teams), player_stats=None, player_name=None)

@app.route('/player', methods=['POST'])
def player_stats():
    player_name = request.form['player']
    role = request.form['role']
    try:
        corrected = standardize_player(player_name)
        if role == 'batsman':
            stats = json.loads(jugaad.batsmanAPI(corrected))
        else:
            stats = json.loads(jugaad.bowlerAPI(corrected))
        teams = ipl.teamsAPI()['teams']
    except Exception:
        return render_template('index.html', error="Player stats failed", teams=[], result={}, player_stats=None, player_name=None)
    return render_template('index.html', result={}, teams=sorted(teams), player_stats=stats, player_name=corrected)

if __name__ == '__main__':
    import os

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
    # app.run(debug=True)
