# Housing Prices Prediction

Este projeto visa prever os preços de venda de casas usando um modelo de machine learning. O modelo é treinado utilizando o conjunto de dados de treinamento fornecido e as previsões são geradas para o conjunto de dados de teste. O código usa um modelo RandomForestRegressor para fazer as previsões.

## Descrição

O código realiza as seguintes etapas para prever os preços das casas:

1. **Importação das Bibliotecas Necessárias:**
   - O código importa bibliotecas essenciais para a análise de dados e modelagem, incluindo pandas para manipulação de dados, scikit-learn para construção e avaliação do modelo, e `RandomForestRegressor` para a modelagem preditiva.

2. **Configuração do Ambiente e Caminhos dos Arquivos:**
   - Inicialmente, o código configura o ambiente para garantir que os arquivos de entrada estejam no local correto. Ele cria links simbólicos para os arquivos de dados de treino e teste, se necessário.

3. **Carregamento e Preparação dos Dados:**
   - O conjunto de dados de treinamento é carregado e a variável alvo (preço de venda das casas) é separada das características (features). As características utilizadas são especificadas em uma lista, e o conjunto de dados é dividido em dados de treinamento e validação para avaliar o modelo.

4. **Treinamento e Avaliação do Modelo:**
   - Um modelo de Random Forest é treinado usando o conjunto de dados de treinamento. A avaliação do modelo é feita usando um conjunto de validação para calcular o erro absoluto médio (MAE). Esse valor ajuda a entender a precisão do modelo na previsão dos preços de venda.

5. **Treinamento Final e Geração de Previsões:**
   - Após a validação inicial, um novo modelo de Random Forest é treinado usando todos os dados de treinamento disponíveis. Esse modelo é então usado para prever os preços das casas no conjunto de dados de teste.

6. **Geração do Arquivo de Submissão:**
   - As previsões geradas são salvas em um arquivo CSV no formato exigido para a competição Kaggle. Este arquivo pode ser submetido para avaliação no leaderboard da competição.

## Instruções

1. **Clone o Repositório:**
    ```bash
    git clone https://github.com/seu-usuario/housing-prices-prediction.git
    cd housing-prices-prediction
    ```

2. **Instale as Dependências:**
    ```bash
    pip install pandas scikit-learn
    ```

3. **Prepare os Dados:**
   - Baixe os arquivos `train.csv` e `test.csv` do [Kaggle Housing Prices Dataset](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data) e coloque-os na pasta `data/`.

4. **Execute o Script de Análise:**
    ```bash
    python housing_prices_analysis.py
    ```

5. **Verifique a Saída:**
   - O arquivo `submission.csv` será gerado na raiz do diretório com as previsões para o conjunto de dados de teste.

## Detalhamento do Código

O script `housing_prices_analysis.py` é dividido nas seguintes seções:

### 1. Importação das Bibliotecas

Importa bibliotecas necessárias para a análise e modelagem.

### 2. Configuração do Ambiente

Prepara os caminhos dos arquivos de dados para garantir que o código funcione corretamente no ambiente de execução.

### 3. Carregamento dos Dados

Lê os dados de treinamento e define as características (features) a serem usadas para a modelagem. A variável alvo é separada.

### 4. Treinamento e Avaliação do Modelo

Treina um modelo de RandomForestRegressor com os dados de treinamento e avalia a performance usando um conjunto de validação. Calcula o erro absoluto médio (MAE) para medir a precisão do modelo.

### 5. Treinamento Final e Previsão

Treina um modelo de RandomForestRegressor com todos os dados de treinamento e faz previsões para o conjunto de dados de teste.

### 6. Geração do Arquivo de Submissão

Cria um arquivo CSV com as previsões no formato requerido para a competição e o salva como `submission.csv`.

## Contribuições

Sinta-se à vontade para abrir issues e enviar pull requests com melhorias ou correções.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Referências

- [Kaggle Housing Prices Dataset](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data)
- [Introdução ao Machine Learning - Curso](https://www.kaggle.com/learn/intro-to-machine-learning)
