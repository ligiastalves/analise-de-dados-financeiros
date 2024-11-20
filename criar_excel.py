import pandas as pd
import matplotlib.pyplot as plt

# Dados a serem salvos no Excel
dados = {
    'Data': ['2024-11-01', '2024-11-02', '2024-11-03', '2024-11-05', '2024-11-07',
             '2024-11-08', '2024-11-12', '2024-11-15', '2024-11-16', '2024-11-17'],
    'Categoria': ['Alimentação', 'Transporte', 'Lazer', 'Alimentação', 'Transporte',
                  'Lazer', 'Alimentação', 'Transporte', 'Lazer', 'Alimentação'],
    'Valores': [100.50, 50.00, 75.30, 80.70, 95.30, 52.45, 63.20, 47.80, 105.60, 28.10]
}

# Criar DataFrame com pandas
df = pd.DataFrame(dados)

# Salvar o DataFrame em um arquivo Excel
df.to_excel('dados_financeiros.xlsx', index=False)

# Processar dados - Total e Média
total = df['Valores'].sum()  # Soma dos valores
media = df['Valores'].mean()  # Média dos valores

# Exibir relatório no console
print(f"Relatório de Despesas:")
print(f"Total: R${total:.2f}")
print(f"Média: R${media:.2f}")

# Gerar gráfico
plt.figure(figsize=(10, 6))

# Gráfico de barras com categoria e valores
plt.bar(df['Data'], df['Valores'], color='skyblue')

# Adicionar título e rótulos
plt.title('Despesas por Data', fontsize=16)
plt.xlabel('Data', fontsize=12)
plt.ylabel('Valor (R$)', fontsize=12)

# Exibir o gráfico
plt.xticks(rotation=45, ha='right')  # Rotacionar as datas para melhor leitura
plt.tight_layout()  # Ajustar o layout
plt.show()
