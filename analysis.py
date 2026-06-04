# ============================================================
#   IPL 2024 CRICKET ANALYTICS
#   Author: Joney Raj
#   Description: Analysing IPL 2024 match data using Python
# ============================================================

# --- STEP 1: Import libraries (tools we need) ---
# pandas  → for reading and working with data (like Excel in Python)
# matplotlib → for creating charts and graphs
# os → for creating folders on your computer

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

# --- STEP 2: Create a folder to save our charts ---
os.makedirs('charts', exist_ok=True)
print("=" * 50)
print("   IPL 2024 CRICKET ANALYTICS - by Joney Raj")
print("=" * 50)

# --- STEP 3: Load the data ---
# pd.read_csv() reads our CSV file and turns it into a "DataFrame"
# A DataFrame is like a table with rows and columns
df = pd.read_csv('data/ipl_2024_matches.csv')

# Show basic info about the dataset
print(f"\n📋 Dataset loaded successfully!")
print(f"   Total matches in dataset : {len(df)}")
print(f"   Total columns (fields)   : {len(df.columns)}")
print(f"\n📌 Column names:")
for col in df.columns:
    print(f"   → {col}")

# ============================================================
# ANALYSIS 1: How many matches did each team win?
# ============================================================
print("\n" + "=" * 50)
print("  ANALYSIS 1: TEAM WINS")
print("=" * 50)

# value_counts() counts how many times each team appears in 'winner' column
team_wins = df['winner'].value_counts()
print("\nWins per team:")
print(team_wins.to_string())

# Create bar chart
fig, ax = plt.subplots(figsize=(12, 6))

# Sort wins from highest to lowest for a cleaner look
colors = ['#F4A21C' if team == 'SRH' else '#3B75AF' for team in team_wins.index]
bars = ax.bar(team_wins.index, team_wins.values, color=colors, edgecolor='white', linewidth=0.8)

# Add number labels on top of each bar
for bar, val in zip(bars, team_wins.values):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.2,
            str(val), ha='center', va='bottom', fontsize=11, fontweight='bold')

ax.set_title('IPL 2024 — Team Wins (League Stage + Playoffs)', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Team', fontsize=13)
ax.set_ylabel('Number of Wins', fontsize=13)
ax.set_ylim(0, max(team_wins.values) + 2)
ax.tick_params(axis='x', rotation=30)
ax.grid(axis='y', alpha=0.3, linestyle='--')

# Add legend to highlight SRH
srh_patch = mpatches.Patch(color='#F4A21C', label='SRH (Sunrisers Hyderabad)')
other_patch = mpatches.Patch(color='#3B75AF', label='Other Teams')
ax.legend(handles=[srh_patch, other_patch], fontsize=10)

plt.tight_layout()
plt.savefig('charts/1_team_wins.png', dpi=150, bbox_inches='tight')
plt.close()
print("\n✅ Chart saved: charts/1_team_wins.png")


# ============================================================
# ANALYSIS 2: SRH Performance Deep Dive
# ============================================================
print("\n" + "=" * 50)
print("  ANALYSIS 2: SRH PERFORMANCE")
print("=" * 50)

# Filter only SRH matches (where SRH is either team1 or team2)
srh_matches = df[(df['team1'] == 'SRH') | (df['team2'] == 'SRH')].copy()

# Check if SRH won each match
srh_matches['srh_won'] = srh_matches['winner'] == 'SRH'
srh_wins   = srh_matches['srh_won'].sum()
srh_losses = len(srh_matches) - srh_wins
win_pct    = round((srh_wins / len(srh_matches)) * 100, 1)

print(f"\n🟠 SRH Stats:")
print(f"   Matches played : {len(srh_matches)}")
print(f"   Wins           : {srh_wins}")
print(f"   Losses         : {srh_losses}")
print(f"   Win %          : {win_pct}%")

# Pie chart for SRH win/loss
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle('SRH (Sunrisers Hyderabad) — IPL 2024 Performance', fontsize=16, fontweight='bold')

# Left: Win/Loss pie
axes[0].pie(
    [srh_wins, srh_losses],
    labels=[f'Wins\n({srh_wins})', f'Losses\n({srh_losses})'],
    colors=['#F4A21C', '#2C2C2C'],
    autopct='%1.1f%%',
    startangle=140,
    textprops={'fontsize': 12}
)
axes[0].set_title('Win / Loss Ratio', fontsize=13, fontweight='bold')

# Right: Scores in SRH matches
srh_scores = srh_matches[['team1', 'team2', 'team1_score', 'team2_score', 'winner']].copy()
srh_match_labels = [f"M{i+1}" for i in range(len(srh_scores))]
srh_own_scores = []
srh_opp_scores = []
for _, row in srh_scores.iterrows():
    if row['team1'] == 'SRH':
        srh_own_scores.append(row['team1_score'])
        srh_opp_scores.append(row['team2_score'])
    else:
        srh_own_scores.append(row['team2_score'])
        srh_opp_scores.append(row['team1_score'])

x = range(len(srh_match_labels))
axes[1].plot(srh_match_labels, srh_own_scores, marker='o', color='#F4A21C',
             linewidth=2, markersize=6, label='SRH Score')
axes[1].plot(srh_match_labels, srh_opp_scores, marker='s', color='#2C2C2C',
             linewidth=2, markersize=6, label='Opponent Score')
axes[1].fill_between(srh_match_labels, srh_own_scores, srh_opp_scores, alpha=0.15, color='#F4A21C')
axes[1].set_title('SRH vs Opponent Scores Per Match', fontsize=13, fontweight='bold')
axes[1].set_xlabel('Match Number')
axes[1].set_ylabel('Total Runs')
axes[1].legend(fontsize=10)
axes[1].tick_params(axis='x', rotation=45)
axes[1].grid(alpha=0.3, linestyle='--')

plt.tight_layout()
plt.savefig('charts/2_srh_performance.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Chart saved: charts/2_srh_performance.png")


# ============================================================
# ANALYSIS 3: Toss Analysis
# ============================================================
print("\n" + "=" * 50)
print("  ANALYSIS 3: TOSS ANALYSIS")
print("=" * 50)

# Did winning the toss help you win the match?
df['toss_match_winner'] = df['toss_winner'] == df['winner']
toss_win_rate = round(df['toss_match_winner'].mean() * 100, 1)
print(f"\n🪙 Toss Stats:")
print(f"   Toss winner also won match: {toss_win_rate}% of the time")

toss_decision_counts = df['toss_decision'].value_counts()
print(f"\n   Teams chose to bat first  : {toss_decision_counts.get('bat', 0)} times")
print(f"   Teams chose to field first: {toss_decision_counts.get('field', 0)} times")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle('IPL 2024 — Toss Analysis', fontsize=16, fontweight='bold')

# Left: Did winning toss = winning match?
toss_outcome = ['Toss + Match Won', 'Toss Won, Match Lost']
toss_vals    = [df['toss_match_winner'].sum(), (~df['toss_match_winner']).sum()]
axes[0].pie(toss_vals, labels=toss_outcome, autopct='%1.1f%%',
            colors=['#27AE60', '#E74C3C'], startangle=90, textprops={'fontsize': 11})
axes[0].set_title('Does Winning Toss Help?', fontsize=12, fontweight='bold')

# Right: Bat vs Field decision
axes[1].pie(toss_decision_counts.values, labels=toss_decision_counts.index,
            autopct='%1.1f%%', colors=['#3B75AF', '#F4A21C'],
            startangle=90, textprops={'fontsize': 11})
axes[1].set_title('Toss Decision: Bat vs Field', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('charts/3_toss_analysis.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Chart saved: charts/3_toss_analysis.png")


# ============================================================
# ANALYSIS 4: Top Player of the Match Awards
# ============================================================
print("\n" + "=" * 50)
print("  ANALYSIS 4: PLAYER OF THE MATCH AWARDS")
print("=" * 50)

pom = df['player_of_match'].value_counts().head(10)
print("\n🏆 Top 10 Players (Man of the Match):")
print(pom.to_string())

fig, ax = plt.subplots(figsize=(12, 6))
colors_pom = ['#F4A21C' if p in ['Travis Head', 'Abhishek Sharma',
               'Heinrich Klaasen', 'Pat Cummins'] else
              '#8E44AD' if p in ['Sunil Narine', 'Rinku Singh',
               'Venkatesh Iyer', 'Mitchell Starc', 'Ramandeep Singh'] else
              '#3B75AF' for p in pom.index]

bars = ax.barh(pom.index[::-1], pom.values[::-1], color=colors_pom[::-1],
               edgecolor='white', linewidth=0.8)
for bar, val in zip(bars, pom.values[::-1]):
    ax.text(bar.get_width() + 0.05, bar.get_y() + bar.get_height() / 2,
            str(val), va='center', fontsize=11, fontweight='bold')

ax.set_title('IPL 2024 — Top 10 Player of the Match Awards', fontsize=15, fontweight='bold', pad=15)
ax.set_xlabel('Number of Awards', fontsize=12)
ax.set_xlim(0, pom.values.max() + 1)
ax.grid(axis='x', alpha=0.3, linestyle='--')

srh_p  = mpatches.Patch(color='#F4A21C', label='SRH Players')
kkr_p  = mpatches.Patch(color='#8E44AD', label='KKR Players')
rest_p = mpatches.Patch(color='#3B75AF', label='Other Teams')
ax.legend(handles=[srh_p, kkr_p, rest_p], fontsize=10, loc='lower right')

plt.tight_layout()
plt.savefig('charts/4_player_of_match.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Chart saved: charts/4_player_of_match.png")


# ============================================================
# ANALYSIS 5: Venue — Highest Scoring Grounds
# ============================================================
print("\n" + "=" * 50)
print("  ANALYSIS 5: VENUE ANALYSIS")
print("=" * 50)

df['total_runs'] = df['team1_score'] + df['team2_score']
venue_avg = df.groupby('venue')['total_runs'].mean().sort_values(ascending=False)
print("\n🏟️  Average Total Runs per Venue:")
print(venue_avg.round(1).to_string())

fig, ax = plt.subplots(figsize=(12, 7))
venue_labels = [v.split(' ')[0] + '\n' + ' '.join(v.split(' ')[1:]) for v in venue_avg.index]
bars = ax.bar(venue_labels, venue_avg.values, color='#2980B9', edgecolor='white', linewidth=0.8)

for bar, val in zip(bars, venue_avg.values):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1,
            f'{val:.0f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

ax.set_title('IPL 2024 — Average Total Runs per Venue\n(Higher = Better Batting Ground)',
             fontsize=14, fontweight='bold', pad=15)
ax.set_ylabel('Average Total Runs (Both Teams)', fontsize=12)
ax.set_ylim(0, venue_avg.max() + 30)
ax.tick_params(axis='x', labelsize=8)
ax.grid(axis='y', alpha=0.3, linestyle='--')
plt.tight_layout()
plt.savefig('charts/5_venue_analysis.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Chart saved: charts/5_venue_analysis.png")


# ============================================================
# FINAL SUMMARY
# ============================================================
print("\n" + "=" * 50)
print("  PROJECT COMPLETE! SUMMARY")
print("=" * 50)
champion = df['winner'].value_counts().index[0]
runner   = df['winner'].value_counts().index[1]
print(f"\n🏆 IPL 2024 Champion     : {champion}")
print(f"🥈  Runner Up            : {runner}")
print(f"🟠 SRH Win %             : {win_pct}%")
print(f"🪙 Toss → Win rate       : {toss_win_rate}%")
print(f"\n📊 5 charts saved in: charts/ folder")
print("\n✅ All done! Upload the charts/ folder to GitHub.")
print("=" * 50)
