# Análise Financeira Python

Este projeto tem como objetivo realizar a análise de dados financeiros a partir de um arquivo Excel, processando informações como despesas, categorias e valores. Utilizando a biblioteca **Pandas** para manipulação dos dados, **Matplotlib** para geração de gráficos e **Python** para automação de todo o processo, o script oferece uma visão detalhada das despesas, com a possibilidade de filtrar valores específicos, gerar relatórios e gráficos de análise.

## Funcionalidades

- **Leitura de dados**: O script lê dados de um arquivo Excel (.xlsx) contendo informações de despesas, como data, categoria e valor.
- **Análise de dados**: Utiliza a biblioteca **Pandas** para calcular o total e a média dos valores por categoria.
- **Relatório de resultados**: Gera um relatório com os totais e médias das despesas por categoria.
- **Filtros de dados**: Permite filtrar as despesas por valores, para focar apenas em dados específicos.
- **Visualização gráfica**: Gera gráficos de barras e pizza com a distribuição das despesas por categoria, utilizando a biblioteca **Matplotlib**.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para automação e processamento de dados.
- **Pandas**: Biblioteca usada para manipulação e análise de dados.
- **Matplotlib**: Biblioteca utilizada para criação de gráficos de visualização.
- **OpenPyXL**: Biblioteca para leitura e escrita de arquivos Excel (.xlsx).

## Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/ligiastalves/analise-de-dados-financeiros.git
   
2. Instale as dependências necessárias:

    ```bash
    pip install pandas matplotlib openpyxl

3. Coloque seu arquivo Excel de dados na mesma pasta do script ou modifique o caminho no script para apontar para o local correto.

4. Execute o script:

    ```bash
    python criar_excel.py
    
5. CAso queira aplicar filtro   
    ```bash
    python criar_excel_filtro.py

6. O script irá carregar os dados de uma planilha Excel, aplicar o filtro desejado, calcular o total e a média, gerar um relatório no console e um gráfico de barras com os dados filtrados.

## Possíveis Melhorias Futuras
- Adicionar mais opções de filtragem, como por data ou categoria.
- Melhorar a interface do usuário, permitindo interações dinâmicas.
- Incluir a possibilidade de gerar diferentes tipos de gráficos (pizza, linha, etc.).
- Adicionar a opção de salvar o relatório gerado em formato PDF ou CSV.

## Contribuindo
Se você quiser contribuir para o projeto, siga as etapas:

- Faça um fork deste repositório.
- Crie uma branch para a sua alteração (git checkout -b feature/nova-funcionalidade).
- Commit suas alterações (git commit -am 'Adiciona nova funcionalidade').
- Faça o push para a branch (git push origin feature/nova-funcionalidade).
- Abra um pull request.

## Resultado esperado
![script_sem_filtro](https://github.com/user-attachments/assets/f0b2ed40-e883-48aa-98e8-46a6032296f5)

![script_com_filtro](https://github.com/user-attachments/assets/411c90ec-e08c-44cd-9308-9fee75da452e)
