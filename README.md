# Tentativa de Implementar e comparar duas arvores de classificação. (SOU SAPEQUINHA)

Arvores escolhidas foram a DecisionTreeRegressor e a RandomForest.

 Analize feita sobe o dataset Analyzing Student Academic Trends encontrado no kaggle sobre o link https://www.kaggle.com/datasets/saadaliyaseen/analyzing-student-academic-trends?resource=download. Busca entender e analizar como os habitos de estudantes impactam em suas notas e aprovação.

RandomForest Result:

OOB R^2: 0.7331
Train MSE: 1.5872
Test  MSE: 10.5765
Test   R² score: 0.8007
Test MAE: 2.8800


DecisionTreeRegressor Result:

Train MSE: 0.0000
Test  MSE: 17.9560
Test  MAE: 3.5900
Test  R²:  0.6645



Train MSE: O RandomForest demonstrou um pequeno erro de 1.5872, demonstrando q o overfitting foi evitado. No Caso do DecisionTreeRegressor, ocorreu overfitting pois o MSE foi igual a 0.0000, nesse caso o RandomForest é superior por ter maior capacidade de generalização.

Test MSE: O RandomForest demonstrou um erro de 10.5765 ao ser exposto a novos dados. No caso do DecisionTreeRegressor, o erro é de 17.9560, demonstrando qe ao reeber dados novos, o RandomForest costuma errar menos em suas predições.

Test MAE:O erro médio do RandomForest é 2.8800, ja o do DecisionTreeRegressor é de 3.5900. Mostra que o erro médio do RandomForest é Menor.

Test R²: A Variância do RandomForest é 0,80 ou 80%, Ja a variância do DecisionTreeRegressor é de 0.6645. Mostra que a Variância do RandomForest abrange mais que a do DecisionTreeRegressor.

Nesse Dataset a escolha do RandomForest é claramente superior em todas as métricas.







