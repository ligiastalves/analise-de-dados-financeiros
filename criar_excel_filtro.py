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

# Filtro para valores acima de 60
filtro = df['Valores'] > 60  # Altere o valor aqui conforme necessário

# Aplicar o filtro ao DataFrame
df_filtrado = df[filtro]

# Salvar o DataFrame filtrado em um arquivo Excel
df_filtrado.to_excel('dados_financeiros_filtrados.xlsx', index=False)

# Processar dados - Total e Média dos dados filtrados
total_filtrado = df_filtrado['Valores'].sum()  # Soma dos valores filtrados
media_filtrado = df_filtrado['Valores'].mean()  # Média dos valores filtrados

# Exibir relatório no console
print(f"Relatório de Despesas (Filtrados):")
print(f"Total (Valores > 60): R${total_filtrado:.2f}")
print(f"Média (Valores > 60): R${media_filtrado:.2f}")

# Gerar gráfico dos dados filtrados
plt.figure(figsize=(10, 6))

# Gráfico de barras com categoria e valores filtrados
plt.bar(df_filtrado['Data'], df_filtrado['Valores'], color='salmon')

# Adicionar título e rótulos
plt.title('Despesas Filtradas por Data', fontsize=16)
plt.xlabel('Data', fontsize=12)
plt.ylabel('Valor (R$)', fontsize=12)

# Exibir o gráfico
plt.xticks(rotation=45, ha='right')  # Rotacionar as datas para melhor leitura
plt.tight_layout()  # Ajustar o layout
plt.show()
