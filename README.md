# 🏏 IPL Analytics API Dashboard

This is a full-stack Flask web application that analyzes IPL (Indian Premier League) cricket data from 2008–2022. It provides clean API endpoints and a dynamic frontend dashboard to compare teams and analyze player performance in real-time.

🔗 **Live App:** [https://web-production-b0099.up.railway.app](https://web-production-b0099.up.railway.app)

## 📊 Features

- ✅ Team vs Team win/loss head-to-head analysis
- ✅ Batting and Bowling record lookup by player name
- ✅ Fuzzy name matching for teams & players (e.g. "msd", "mumbai", "rcb")
- ✅ Bootstrap-powered responsive UI
- ✅ Hosted for free on Railway

## 🧠 Tech Stack

- Python, Flask, Pandas
- HTML, Bootstrap 5, Jinja2
- Hosted on Railway
- Data Source: IPL Ball-by-Ball & Match Dataset (2008–2022)

## 📁 API Endpoints

| Route                            | Description                             |
|----------------------------------|-----------------------------------------|
| `/api/teams`                     | Returns all IPL teams                   |
| `/api/teamvteam?team1=X&team2=Y` | Head-to-head results                    |
| `/api/batting-record?batsman=X`  | Batting stats for player X              |
| `/api/bowling-record?bowler=X`   | Bowling stats for player X              |

## 🖼️ UI Preview

![Player Stats Page](https://github.com/Singhrahul2511/ipl-analytics-api-dashboard/blob/main/Screenshot%202025-06-26%20031951.png)

![Player Stats Page](https://github.com/Singhrahul2511/ipl-analytics-api-dashboard/blob/main/Screenshot%202025-06-26%20032010.png)


![Player Stats Page](https://github.com/Singhrahul2511/ipl-analytics-api-dashboard/blob/main/Screenshot%202025-06-26%20032100.png)

![Player Stats Page](https://github.com/Singhrahul2511/ipl-analytics-api-dashboard/blob/main/Screenshot%202025-06-26%20032110.png)


---

## ✨ How to Use

1. Enter team names or player nicknames (e.g., `mi`, `msd`)
2. View real-time stats
3. Easily deployable to Railway

---


---

## 🙋‍♂️ Author

**Rahul Kumar**  
🔗 [LinkedIn](https://www.linkedin.com/in/rahul-kumar-8ab740268)  
💻 [GitHub](https://github.com/Singhrahul2511)

---

⭐ If you like this project, give it a star and share!


🔗 **Chatgpt:** [https://chatgpt.com/share/686b8432-59b0-8002-9f58-69c4d228841f)
