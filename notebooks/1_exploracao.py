import pandas as pd


'''matches_caminho = "C:/copa-challenger/data/raw/matches_1930_2022.csv"
df_matches = pd.read_csv(matches_caminho)

print("Primeiras 5 linhas dataset")
print(df_matches.head(5))

print("Infos Dataset Matches")
print(df_matches.info())

print("Nome das selecoes MAtches")
print(df_matches['home_team'])
'''

'''world_cup ="C:/copa-challenger/data/raw/world_cup.csv"
df_world_cup = pd.read_csv(world_cup)

print("5 Linhas DF World Cup")
print(df_world_cup.head())

print("Info world cup")
print(df_world_cup.info())
'''


ranking2026 = "C:/copa-challenger/data/raw/fifa_ranking_2026-06-08.csv"
df_ranking2026 = pd.read_csv(ranking2026)

print("Top 5 Ranking 2026")
print(df_ranking2026.head())

ranking2022 = "C:/copa-challenger/data/raw/fifa_ranking_2022-10-06.csv"
df_ranking2022 = pd.read_csv(ranking2022)

print("Top 5 Ranking 2022")
print(df_ranking2022.head())

print("Info selecao em ranking")

print(df_ranking2022[df_ranking2022['team_code'] == 'USA'])