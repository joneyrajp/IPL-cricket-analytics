# 🏏 IPL 2024 Cricket Analytics

> A data analysis project exploring IPL 2024 match data using Python, Pandas, and Matplotlib.

---

## 📌 Project Overview

This project analyses the **Indian Premier League (IPL) 2024** season data to uncover:
- Which teams performed best
- How Sunrisers Hyderabad (SRH) performed across the season
- Whether winning the toss impacts match results
- Which players won the most Man of the Match awards
- Which venues produced the highest-scoring matches

---

## 📊 Key Findings

| Insight | Result |
|---|---|
| 🏆 IPL 2024 Champion | KKR (Kolkata Knight Riders) |
| 🥈 Runners-Up | SRH (Sunrisers Hyderabad) |
| 🟠 SRH Win % | ~67% in league stage |
| 🪙 Does toss help? | ~52% — barely matters! |
| 🎖️ Top Player of Match | Sunil Narine (KKR) |

---

## 📁 Project Structure

```
ipl-cricket-analytics/
│
├── data/
│   └── ipl_2024_matches.csv     ← Match dataset (66 matches)
│
├── charts/                       ← Auto-generated charts
│   ├── 1_team_wins.png
│   ├── 2_srh_performance.png
│   ├── 3_toss_analysis.png
│   ├── 4_player_of_match.png
│   └── 5_venue_analysis.png
│
├── analysis.py                   ← Main Python script
├── requirements.txt              ← Python libraries needed
└── README.md                     ← This file
```

---

## 📈 Charts Generated

### 1. Team Wins — IPL 2024
Bar chart showing total wins per team across league stage and playoffs.

### 2. SRH Performance Deep Dive
Pie chart (win/loss ratio) + line chart comparing SRH scores vs opponents across all matches.

### 3. Toss Analysis
Does winning the toss actually help? Breakdown of toss decisions (bat vs field).

### 4. Player of the Match Awards
Top 10 players with the most Man of the Match awards, highlighting SRH and KKR players.

### 5. Venue Analysis
Average total runs scored per venue — identifying the best batting-friendly grounds.

---

## 🛠️ Tools Used

| Tool | Purpose |
|---|---|
| Python 3 | Programming language |
| Pandas | Data loading and analysis |
| Matplotlib | Creating charts and graphs |

---

## 🚀 How to Run This Project

**Step 1 — Install Python**
Download from: https://www.python.org/downloads/

**Step 2 — Install required libraries**
```bash
pip install -r requirements.txt
```

**Step 3 — Run the analysis**
```bash
python analysis.py
```

Charts will be saved in the `charts/` folder automatically.

---

## 📂 Dataset

- **Source:** IPL 2024 season match results
- **Matches covered:** 66 (league stage + playoffs including final)
- **Fields:** match_id, date, teams, venue, toss details, winner, player of match, scores

---

## 👤 About

**Joney Raj** — Aspiring Data Analyst  
Skills: Python, SQL, Power BI, Data Analysis  
📍 Hyderabad, India

[![GitHub](https://img.shields.io/badge/GitHub-joneyraj-blue)](https://github.com/joneyraj)

---

*This project was created as part of my data analyst portfolio.*
