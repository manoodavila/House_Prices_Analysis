# House_Prices_Analysis.py

# Importa bibliotecas necessárias para manipulação de dados e modelagem
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# Define o caminho para o arquivo de treinamento
iowa_file_path = '../input/train.csv'

# Carrega os dados de treinamento
home_data = pd.read_csv(iowa_file_path)

# Separa a variável alvo (preço de venda) das características (features)
y = home_data.SalePrice

# Define as características a serem usadas para a modelagem
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

# Seleciona as colunas correspondentes às características e exibe uma amostra dos dados
X = home_data[features]
print(X.head())

# Divide os dados em conjuntos de treinamento e validação
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# Cria e treina o modelo de Random Forest com os dados de treinamento
rf_model = RandomForestRegressor(random_state=1)
rf_model.fit(train_X, train_y)

# Faz previsões no conjunto de validação e calcula o erro absoluto médio (MAE)
rf_val_predictions = rf_model.predict(val_X)
rf_val_mae = mean_absolute_error(rf_val_predictions, val_y)

# Exibe o MAE do modelo de Random Forest no conjunto de validação
print("Validation MAE for Random Forest Model: {:,.0f}".format(rf_val_mae))

# Cria um novo modelo de Random Forest e o treina com todos os dados de treinamento
rf_model_on_full_data = RandomForestRegressor(random_state=1)
rf_model_on_full_data.fit(X, y)

# Define o caminho para o arquivo de teste
test_data_path = '../input/test.csv'

# Carrega os dados de teste
test_data = pd.read_csv(test_data_path)

# Cria um conjunto de dados de teste com as mesmas características usadas para treinamento
test_X = test_data[features]

# Faz previsões para o conjunto de dados de teste
test_preds = rf_model_on_full_data.predict(test_X)

# Cria um DataFrame com os IDs dos passageiros e as previsões de preços
output = pd.DataFrame({'Id': test_data.Id,
                       'SalePrice': test_preds})

# Salva as previsões em um arquivo CSV para submissão
output.to_csv('submission.csv', index=False)

print("Submission file 'submission.csv' has been created successfully.")
