import pandas as pd

anos_validos = [2018, 2022]
colunas_dropar = ['Attendance', 'Officials', 'Referee', 'Venue', 'Notes', 'Host', 'Score', 'home_own_goal', 'away_own_goal', 'home_penalty_miss_long', 'away_penalty_miss_long', 'home_penalty_shootout_goal_long', 'away_penalty_shootout_goal_long', 'home_penalty_shootout_miss_long', 'away_penalty_shootout_miss_long', 'home_goal_long', 'away_goal_long', 'home_yellow_card_long', 'away_yellow_card_long', 'home_substitute_in_long', 'away_substitute_in_long']
colunas_ranking_dropar = ['previous_points', 'previous_rank', 'rated_matches']
nomes_selecoes = {'IR Iran':'Iran', 'USA':'United States', 'Korea Republic':'South Korea'}
colunas_nomenclatura_arrumar = {'Runner-Up':'runner_up', 'TopScorrer':'top_scorer', 'AttendanceAvg':'attendance_avg'}

def limpar_partida(df:pd.DataFrame):
    df_limpo = df[df['Year'].isin(anos_validos)]
    return df_limpo


def remover_colunas_desnecessarias(df:pd.DataFrame):
    df_limpo = df.drop(columns=colunas_dropar)
    return df_limpo

def converter_pra_datetime(df:pd.DataFrame):
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def juntar_rankings(df1:pd.DataFrame, df2:pd.DataFrame):
    df1['year'] = 2022
    df2['year'] = 2026
    df_geral = pd.concat([df1,df2])
    return df_geral

def remover_colunas_ranking(df:pd.DataFrame):
    df_limpo = df.drop(columns=colunas_ranking_dropar)
    return df_limpo

def arrumar_nomes_selecoes(df:pd.DataFrame):
    df['team'] = df['team'].replace(nomes_selecoes)
    return df

def anos_valido_copa(df:pd.DataFrame):
    df_limpo = df[df['Year'].isin(anos_validos)]
    return df_limpo

def arrumar_nomeclatura(df:pd.DataFrame):
    df_limpo = df.rename(columns=colunas_nomenclatura_arrumar)
    return df_limpo

def padronizar_colunas(df:pd.DataFrame):
    df.columns = df.columns.astype(str).str.lower()
    return df
