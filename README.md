# Vehicle Insights — Sprint 5

Dashboard web interativo para explorar anúncios de veículos usados, desenvolvido com Python, Streamlit, Pandas e Plotly.

## Funcionalidades
- Indicadores com quantidade de anúncios, preço mediano e quilometragem mediana.
- Filtros por tipo de veículo e condição.
- Histograma interativo dos preços.
- Gráfico de dispersão entre quilometragem e preço.
- Pré-visualização dos dados.

## Estrutura
```text
.
├── app.py
├── vehicles_us.csv
├── requirements.txt
├── README.md
├── .gitignore
├── .streamlit/
│   └── config.toml
└── notebooks/
    └── EDA.ipynb
```

## Ambiente local
```bash
python -m venv vehicles_env
```
Ativar no Windows:
```bash
vehicles_env\Scripts\activate
```
Ativar no macOS/Linux:
```bash
source vehicles_env/bin/activate
```
Instalar dependências e iniciar:
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Publicar no Render
Crie um serviço **Web Service** ligado ao repositório GitHub e configure:

- **Build Command:** `pip install --upgrade pip && pip install -r requirements.txt`
- **Start Command:** `streamlit run app.py`

O ficheiro `.streamlit/config.toml` configura o Streamlit para a porta 10000.

Depois da publicação, acrescente aqui o URL público do serviço:
`URL do Render: (adicionar depois da implantação)`

## Sobre os dados — importante
O ficheiro `vehicles_us.csv` incluído nesta versão é um **conjunto de dados demonstrativo sintético**, criado para permitir executar e testar o dashboard. Não é o CSV oficial fornecido pela TripleTen. Para a entrega final, substitua-o pelo ficheiro oficial `vehicles_us.csv` disponibilizado na plataforma do curso, mantendo o mesmo nome e colocando-o na raiz do projeto. O dashboard espera, entre outras, as colunas `price` e `odometer`.

## Aplicação publicada

Aceder ao dashboard:
https://sprint5-dashboard-4h6a.onrender.com

## Repositório GitHub

https://github.com/afonsoc369/sprint5-dashboard