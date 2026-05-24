  # Text Analysis Pipeline

Pipeline modular de Processamento de Linguagem Natural (NLP) desenvolvido para transformar textos não estruturados em informações organizadas por meio de múltiplas etapas de análise.

O projeto demonstra a aplicação de boas práticas de engenharia de software em sistemas de IA, utilizando modelos open-source para classificação de texto, extração de entidades e sumarização, com uma arquitetura extensível baseada em workflows.


## 🎯 Objetivo

Em cenários reais, grandes volumes de texto precisam ser processados antes de serem utilizados para análise, automação ou apoio à tomada de decisão.

Este projeto aborda esse desafio por meio de um pipeline estruturado que:

- Classifica automaticamente conteúdos textuais.
- Identifica entidades relevantes presentes no texto.
- Gera resumos concisos das informações processadas.
- Organiza o fluxo de execução de forma modular e escalável.
- Utiliza exclusivamente modelos open-source, sem dependência de APIs pagas.


## 🏗️ Arquitetura

O pipeline foi projetado utilizando uma abordagem baseada em workflow, onde cada etapa possui responsabilidade única e pode evoluir independentemente.

### Fluxo de Processamento

```text
Texto de Entrada
        │
        ▼
Classificação
        │
        ▼
Extração de Entidades
        │
        ▼
Sumarização
        │
        ▼
Saída Estruturada
```

Cada módulo é desacoplado e coordenado por uma camada de orquestração responsável pelo fluxo de execução.


## 📂 Estrutura do Projeto

```text
src/
│
├── config/
│   ├── logging.py
│   └── settings.py
│
├── data/
│   └── sample_texts.txt
│
├── graph/
│   └── workflow.py
│
├── notebooks/
│   └── exploration.ipynb
│
├── pipeline/
│   ├── classification.py
│   ├── entity_extraction.py
│   ├── summarization.py
│   └── orchestrator.py
│
├── schemas/
│   └── analysis.py
│
└── README.md
```


## ⚙️ Componentes Principais

### Classification

Responsável pela categorização inicial do conteúdo textual, permitindo identificar o contexto principal do documento.

### Entity Extraction

Extrai entidades relevantes presentes no texto, como pessoas, organizações, locais ou outros elementos de interesse.

### Summarization

Produz versões resumidas do conteúdo original, preservando as informações mais importantes.

### Orchestrator

Coordena a execução das etapas do pipeline, garantindo o fluxo correto entre os módulos de processamento.

### Workflow

Define a estrutura do pipeline utilizando uma abordagem baseada em grafos para orquestração das tarefas.


## 🧠 Tecnologias Utilizadas

- Python
- Hugging Face Transformers
- LangGraph
- Jupyter Notebook
- Mermaid
- NLP (Natural Language Processing)


## 🚀 Possíveis Aplicações

- Análise automatizada de documentos
- Classificação de notícias e conteúdos textuais
- Sistemas de monitoramento de informações
- Apoio à tomada de decisão baseada em texto
- Processamento de relatórios corporativos
- Pipelines para aplicações de IA Generativa


## ▶️ Como Executar

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/text-analysis-pipeline.git
```

Acesse o diretório:

```bash
cd text-analysis-pipeline
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o pipeline:

```bash
python src/pipeline/orchestrator.py
```


## 📈 Próximas Evoluções

- Integração com modelos LLMs
- Persistência de resultados em banco de dados
- Interface Web para execução do pipeline
- Monitoramento e métricas de execução
- Integração com sistemas de RAG


## 👩‍💻 Autora

**Elisiane Quadros**

Desenvolvedora Python | IA, Machine Learning, Automação e Dados

- LinkedIn: https://linkedin.com/in/elisiane-quadros
- GitHub: https://github.com/elisiane-quadros
