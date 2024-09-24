Análise de Dados de Pilotos de Fórmula E
Descrição do Projeto
Este projeto tem como objetivo analisar e comparar o desempenho dos pilotos Nick De Vries e Edoardo Mortara nas temporadas de 2023 e 2024 da Fórmula E. Através de um fluxo de trabalho estruturado, o projeto realiza a leitura de dados, a verificação de consistência de voltas, a simulação de consumo de energia e a comparação de cenários de desempenho.

Sumário
Tecnologias Utilizadas
Estrutura do Projeto
Como Configurar o Ambiente
Execução do Projeto
Funções do Projeto
Resultados
Contribuição
Licença
Tecnologias Utilizadas
Python: Linguagem de programação principal.
Pandas: Para manipulação e análise de dados.
Matplotlib: Para visualização de dados.
NumPy: Para cálculos numéricos.
Jupyter Notebook: Para desenvolvimento interativo e documentação.
Estrutura do Projeto
bash
Copiar código
/analise_dados_f1
│
├── data/
│   └── dados.csv          # Arquivo CSV com dados de desempenho dos pilotos
│
├── src/
│   ├── __init__.py
│   ├── main.py            # Arquivo principal para execução do projeto
│   ├── ler_dados.py       # Função para ler e filtrar os dados
│   ├── consistencia_das_voltas.py # Função para verificar a consistência das voltas
│   ├── calcular_consumo_energia.py # Função para simular consumo de energia
│   └── plotar_graficos.py # Função para plotar gráficos
│
├── requirements.txt        # Dependências do projeto
└── README.md               # Este arquivo
Como Configurar o Ambiente
Clone o repositório:

bash
Copiar código
git clone https://github.com/seu_usuario/analise_dados_f1.git
cd analise_dados_f1
Crie um ambiente virtual (opcional, mas recomendado):

bash
Copiar código
python -m venv venv
source venv/bin/activate   # Para Linux/Mac
venv\Scripts\activate      # Para Windows
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Execução do Projeto
Para executar o projeto, basta rodar o arquivo principal main.py:

bash
Copiar código
python src/main.py
Este arquivo irá executar todo o fluxo de trabalho, desde a leitura dos dados até a exibição dos gráficos de comparação.

Funções do Projeto
Configuração: Define o caminho do arquivo CSV que contém os dados dos pilotos.

Carregamento dos Dados (ler_dados):

Lê o arquivo CSV.
Filtra os dados para Nick De Vries e Edoardo Mortara nas temporadas de 2023 e 2024.
Processamento de Consistência das Voltas (consistencia_das_voltas):

Converte os tempos de volta para segundos.
Calcula a diferença para a volta mais rápida.
Plota gráficos de comparação entre as voltas de 2023 e 2024.
Simulação de Consumo de Energia (calcular_consumo_energia):

Simula a velocidade e o consumo de energia por volta com base em parâmetros fornecidos.
Comparação de Cenários de Consumo:

Plota gráficos comparativos para diferentes cenários (Maior Gasto, Gasto Médio, Economia de Energia).
Execução Final (exec):

Coordena todas as etapas, gerando e exibindo os gráficos finais.
Resultados
Os resultados incluem gráficos de comparação das voltas dos pilotos nas temporadas de 2023 e 2024, bem como gráficos que mostram a simulação de consumo de energia sob diferentes cenários. Os gráficos ajudam a visualizar o desempenho dos pilotos e a tomar decisões informadas sobre estratégias de corrida.

Contribuição
Se você deseja contribuir para este projeto, siga estas etapas:

Faça um fork do projeto.
Crie uma nova branch para sua feature (git checkout -b feature/nome-da-feature).
Faça suas alterações e commit (git commit -m 'Adicionando uma nova feature').
Envie para o branch (git push origin feature/nome-da-feature).
Crie um pull request.
Licença
Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.
