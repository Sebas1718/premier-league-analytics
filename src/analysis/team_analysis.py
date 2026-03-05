# Team Performance Analysis Module

## Overview
This module provides functions to analyze the performance of football teams based on various metrics. It can evaluate teams' statistics, such as wins, losses, draws, goals scored, and goals conceded.

## Functions

### 1. analyze_team_performance(team_data)
   - **Description**: Analyzes the performance of a specific team over a season.
   - **Parameters**: 
     - `team_data`: A dictionary containing the team's match results, goals scored, and goals conceded.
   - **Returns**: A summary of the team's performance including win percentage, average goals scored, and average goals conceded.

### Example:
```python
team_data = {
    'matches': 38,
    'wins': 20,
    'losses': 10,
    'draws': 8,
    'goals_scored': 70,
    'goals_conceded': 40
}
performance_summary = analyze_team_performance(team_data)
print(performance_summary)
```

### 2. compare_teams(team1_data, team2_data)
   - **Description**: Compares the performance of two teams.
   - **Parameters**: 
     - `team1_data`: A dictionary containing the first team's statistics.
     - `team2_data`: A dictionary containing the second team's statistics.
   - **Returns**: A comparison summary highlighting which team performed better in various aspects.

### Example:
```python
team1_data = {'wins': 20, 'losses': 10, 'draws': 8, 'goals_scored': 70, 'goals_conceded': 40}
team2_data = {'wins': 18, 'losses': 12, 'draws': 8, 'goals_scored': 65, 'goals_conceded': 42}
comparison_summary = compare_teams(team1_data, team2_data)
print(comparison_summary)
```

### 3. generate_performance_report(team_data)
   - **Description**: Generates a detailed performance report for a team.
   - **Parameters**: 
     - `team_data`: A dictionary containing the team's statistics.
   - **Returns**: A formatted string containing the performance report.

### Example:
```python
team_data = {'wins': 20, 'losses': 10, 'draws': 8, 'goals_scored': 70, 'goals_conceded': 40}
report = generate_performance_report(team_data)
print(report)
```

## Usage
Import this module in your project and use the functions provided to analyze team performances effectively.