# Regressão Linear Simples

Este projeto mostra de forma simples como funciona a **regressão linear simples**, 
um método usado para encontrar uma relação entre duas variáveis.

## 📘 O que o projeto faz

- Lê dados de um arquivo CSV (valores de X e Y);
- Treina um modelo de regressão linear;
- Mostra os resultados do modelo (inclinação, intercepto e R²).

## 🧠 Como usar

1. Coloque os dados no arquivo `data/dados_estudo.csv`.
2. Execute o arquivo principal:
   ```bash
   python src/main.py
   ```
3. Veja o resultado direto no terminal.

## 📂 Estrutura do projeto

```
regressao_linear_simples/
│
├── data/
│   └── dados_estudo.csv       # Base de dados usada no treino
├── src/
│   ├── main.py                # Programa principal
│   └── models/
│       └── SimpleLinearRegression.py  # Classe com os cálculos da regressão
└── caderno/                   # Materiais de apoio
```

## ✨ Autor
Projeto adaptado por Évillyn, com foco em deixar o código simples e fácil de entender.
