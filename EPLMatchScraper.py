import pandas as pd

#Pulls Match data table from fbref website
df = pd.read_html('https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures', attrs=({'id':'sched_2023-2024_9_1'}))[0]
df = df.dropna(subset=['Wk'])

#exports data to excel and csv
df.to_excel('PremierLeagueFixtures24-23.xlsx', index=False)
df.to_csv('PremierLeagueFixtures24-23.csv')