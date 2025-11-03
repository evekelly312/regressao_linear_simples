"""
Módulo com a classe que realiza a Regressão Linear Simples.

A regressão linear simples é usada para encontrar a melhor linha
que representa a relação entre duas variáveis (X e Y).
"""

class SimpleLinearRegression:
    """Classe para realizar regressão linear simples."""

    def __init__(self):
        self.b0 = 0  # Intercepto
        self.b1 = 0  # Inclinação

    def fit(self, X, y):
        """Treina o modelo com os dados de entrada (X, y)."""
        n = len(X)
        media_x = sum(X) / n
        media_y = sum(y) / n

        num = sum((X[i] - media_x) * (y[i] - media_y) for i in range(n))
        den = sum((X[i] - media_x) ** 2 for i in range(n))

        self.b1 = num / den
        self.b0 = media_y - self.b1 * media_x

    def predict(self, X):
        """Faz previsões com base nos valores de X."""
        return [self.b0 + self.b1 * x for x in X]

    def r2_score(self, y_true, y_pred):
        """Calcula o R², que mostra o quão bom o modelo é."""
        media_y = sum(y_true) / len(y_true)
        ss_total = sum((yi - media_y) ** 2 for yi in y_true)
        ss_res = sum((y_true[i] - y_pred[i]) ** 2 for i in range(len(y_true)))
        return 1 - (ss_res / ss_total)
