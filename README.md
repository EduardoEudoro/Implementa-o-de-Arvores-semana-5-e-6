# Tentativa de Implementar e comparar duas arvores de classificação.

Arvores escolhidas foram a DecisionTreeRegressor e a RandomForest.

Ao analizar o dataset Analyzing Student Academic Trends encontrado no kaggle sobre o link https://www.kaggle.com/datasets/saadaliyaseen/analyzing-student-academic-trends?resource=download, os resultados provam que o RandomForest performo melhor por conta de sua capacidade de generalização maior, evidenciado pelos R²scores, onde o R² score do RandomForest é 0.8007, atingindo 80% de variabilidade e o R² score DecisionTreeRegressor é 0.6645, adiquirindo 66% de Variabilidade.
O teste aplicado foi como as variaveis das colunas: 1(hours_studied), 2(sleep_hours), 3(attendence_percent), 4(previous_scores), afetam a coluna 5(exam_score).
