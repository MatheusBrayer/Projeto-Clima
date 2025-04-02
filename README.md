# Projeto Clima

## Descrição
Este projeto realiza a extração de dados climáticos utilizando a API do OpenWeatherMap e os armazena em um banco de dados SQLite. O objetivo é permitir o registro e análise de condições meteorológicas ao longo do tempo.

## Tecnologias Utilizadas
- **Python**
- **SQLite**
- **Requests** (para consumo da API)
- **dotenv** (para gerenciamento de variáveis de ambiente)

## Instalação e Execução
1. Clone este repositório:
   ```bash
   git clone https://github.com/MatheusBrayer/Projeto-Clima.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd Projeto-Clima
   ```
3. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Configure a chave da API:
   - Crie um arquivo `.env` na raiz do projeto e adicione:
     ```
     CHAVE_API=sua_chave_aqui
     ```
6. Execute o projeto:
   ```bash
   python main.py
   ```

## Estrutura do Projeto
```
Projeto-Clima/
│── data/                # Banco de dados SQLite
│── src/                 # Código-fonte
│   ├── coleta.py        # Módulo de coleta de dados da API
│   ├── database.py      # Módulo de gerenciamento do banco de dados
│   ├── main.py          # Arquivo principal do projeto
│── .gitignore           # Arquivos a serem ignorados pelo Git
│── .env                 # Arquivo de variáveis de ambiente (NÃO COMMITAR)
│── requirements.txt     # Lista de dependências do projeto
│── README.md            # Documentação do projeto
```

## Melhorias Futuras
- Criar uma interface para visualização dos dados.
- Adicionar suporte para previsões climáticas.
- Exportação de dados para formatos como CSV ou JSON.

## Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para usar e modificar! 

