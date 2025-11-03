"""
Programa principal da regressão linear simples.
Lê um arquivo CSV com os dados, treina o modelo e mostra os resultados.
"""

import os
from models.SimpleLinearRegression import SimpleLinearRegression


def ler_csv(caminho):
    """
    Lê um arquivo CSV com duas colunas (X e Y) e retorna duas listas.

    Args:
        caminho (str): Caminho do arquivo CSV.

    Returns:
        tuple[list[float], list[float]]: Listas com valores de X e Y.
    """
    X, y = [], []
    with open(caminho, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()[1:]  # Ignora o cabeçalho
        for linha in linhas:
            partes = linha.strip().split(",")
            X.append(float(partes[0]))
            y.append(float(partes[1]))
    return X, y


if __name__ == "__main__":
    # Define o caminho do arquivo CSV
    base_dir = os.path.dirname(os.path.abspath(__file__))
    caminho_csv = os.path.join(base_dir, "../data/dados_estudo.csv")

    # 1️⃣ Ler os dados do arquivo
    X, y = ler_csv(caminho_csv)

    # 2️⃣ Criar e treinar o modelo
    model = SimpleLinearRegression()
    model.fit(X, y)

    # 3️⃣ Fazer previsões e calcular o R²
    y_pred = model.predict(X)
    r2 = model.r2_score(y, y_pred)

    # 4️⃣ Mostrar os resultados
    print("=" * 45)
    print(" REGRESSÃO LINEAR SIMPLES - RESULTADOS ")
    print("=" * 45)
    print(f"Intercepto (b0): {model.b0:.4f}")
    print(f"Inclinação (b1): {model.b1:.4f}")
    print(f"Coeficiente de determinação (R²): {r2:.4f}")
    print("=" * 45)
