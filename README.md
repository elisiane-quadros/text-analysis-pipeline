# Text Analysis Pipeline

Este projeto implementa um pipeline modular de Processamento de Linguagem Natural (NLP) para análise de textos não estruturados, passando por múltiplas etapas como classificação, extração de entidades e sumarização.

O foco do projeto é demonstrar boas práticas de engenharia aplicadas a sistemas de IA, utilizando modelos open-source e uma arquitetura extensível.

---

## 🎯 Problema

Em cenários reais, textos brutos precisam ser processados em diferentes etapas antes de serem utilizados para análise, automação ou apoio à tomada de decisão.

Este projeto aborda esse problema ao:

- Separar tarefas complexas de NLP em módulos independentes
- Orquestrar o fluxo de execução de forma explícita e controlada
- Evitar dependência de APIs pagas, utilizando modelos open-source

---

## 🏗️ Visão Geral da Arquitetura

O pipeline segue um fluxo baseado em grafo, onde cada etapa representa um passo do processamento:

Texto de entrada
↓
Classificação de texto
↓
Extração de entidades
↓
Sumarização
↓
Saída estruturada

Cada etapa é implementada de forma isolada e conectada por um workflow central.

---

## 🧠 Tecnologias Utilizadas

- Python
- Hugging Face Transformers (modelos open-source de NLP)
- LangGraph (orquestração baseada em grafos)
- Mermaid (visualização de workflows)

---

## 📁 Estrutura do Projeto

src/
├── pipeline/
│ ├── classification.py
│ ├── entity_extraction.py
│ └── summarization.py
│
├── graph/
│ └── workflow.py

---

## ▶️ Como Executar

O projeto está em desenvolvimento. As instruções para execução local serão adicionadas nos próximos passos.

---

## 👩‍💻 Autora

**Elisiane Quadros**  
AI Engineer / NLP
