import pandas as pd
import numpy as np
import random

def calcular_qualidade_geral(germinacao, vigor, pureza, viabilidade, umidade):
    peso_germinacao = 0.4
    peso_vigor = 0.2
    peso_pureza = 0.2
    peso_viabilidade = 0.1
    peso_umidade = 0.1

    qualidade_geral = (germinacao * peso_germinacao) + (vigor * peso_vigor) + \
                      (pureza * peso_pureza) + (viabilidade * peso_viabilidade) + \
                      (umidade * peso_umidade)
    
    return qualidade_geral

def gerar_valores_fakes():
    germinacao = random.randint(60, 100)  # 60 a 100% para germinação
    vigor = random.randint(60, 100)       # 60 a 100% para vigor
    pureza = random.randint(70, 100)      # 70 a 100% para pureza
    viabilidade = random.randint(60, 100) # 60 a 100% para viabilidade (Tetrazólio)
    umidade = random.randint(10, 15)      # 10 a 15% para umidade
    return germinacao, vigor, pureza, viabilidade, umidade

def gerar_base_dados_fake(n):
    data = []

    for i in range(n):
        germinacao, vigor, pureza, viabilidade, umidade = gerar_valores_fakes()

        qualidade_geral = calcular_qualidade_geral(germinacao, vigor, pureza, viabilidade, umidade)

        data.append({
            'ID': i+1,
            'Semente': 'Soja',
            'Germinação (%)': germinacao,
            'Vigor (%)': vigor,
            'Pureza (%)': pureza,
            'Viabilidade (%)': viabilidade,
            'Umidade (%)': umidade,
            'Qualidade Geral (%)': qualidade_geral
        })

    df = pd.DataFrame(data)

    return df

df_fake = gerar_base_dados_fake(20000)

print(df_fake.head())

df_fake.to_csv(r'C:\Users\eduardo.cordeiro\Desktop\AI sementes\data\base_sementes_fake.csv', index=False)

