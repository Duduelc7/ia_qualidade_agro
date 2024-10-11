import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


df_fake_20k = pd.read_csv(r'C:\Users\eduardo.cordeiro\Desktop\AI sementes\data\base_sementes_fake.csv')
df = df_fake_20k

X = df[['Germinação (%)', 'Vigor (%)', 'Pureza (%)', 'Viabilidade (%)', 'Umidade (%)']]
y = df['Qualidade Geral (%)']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = RandomForestRegressor(n_estimators=100, random_state=42)

modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Erro Médio Absoluto (MAE): {mae:.2f}')
print(f'Coeficiente de Determinação (R²): {r2:.2f}')

novos_dados = pd.DataFrame({
    'Germinação (%)': [90, 75],
    'Vigor (%)': [80, 70],
    'Pureza (%)': [85, 90],
    'Viabilidade (%)': [88, 85],
    'Umidade (%)': [12, 13]
})

qualidade_prevista = modelo.predict(novos_dados)

print(f'Qualidade Geral Prevista para novos dados: {qualidade_prevista}')
