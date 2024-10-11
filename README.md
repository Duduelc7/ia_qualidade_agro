# Cálculo Automático da Qualidade Geral de Sementes Usando IA 🌱🤖

Este projeto utiliza **Inteligência Artificial (IA)** para automatizar o cálculo da **Qualidade Geral** de sementes a partir de resultados de testes laboratoriais como Germinação, Vigor, Pureza, Viabilidade (Tetrazólio) e Umidade. O modelo de IA foi treinado usando o algoritmo **Random Forest Regressor**, que obteve um **Erro Médio Absoluto (MAE)** de 0.26 e um **Coeficiente de Determinação (R²)** de 1.00, o que demonstra alta precisão.

## 📋 Descrição do Projeto

O objetivo deste projeto é calcular automaticamente a qualidade geral de lotes de sementes com base nos seguintes testes:
- **Germinação (%)**
- **Vigor (%)**
- **Pureza (%)**
- **Viabilidade (%)** (Tetrazólio)
- **Umidade (%)**

Esses testes são combinados em um modelo de aprendizado supervisionado para prever a **Qualidade Geral (%)** de novos lotes de sementes.

## 🚀 Funcionalidades
- Geração de uma base de dados fictícia com 20.000 registros de lotes de sementes.
- Treinamento de um modelo de IA baseado em **RandomForestRegressor**.
- Avaliação do modelo com **MAE** e **R²**.
- Previsões automáticas de **Qualidade Geral** para novos lotes de sementes.


## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada.
- **pandas**: Para manipulação e análise de dados.
- **scikit-learn**: Para criar e treinar o modelo de IA.
- **RandomForestRegressor**: Algoritmo de aprendizado supervisionado utilizado para a regressão.
- **Jupyter Notebook** (opcional): Para experimentação e visualização de dados.

## 📊 Desempenho do Modelo

- **Erro Médio Absoluto (MAE)**: `0.26`
- **Coeficiente de Determinação (R²)**: `1.00`

## ⚙️ Como Rodar o Projeto

### 1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
