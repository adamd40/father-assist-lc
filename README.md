# Father Assist LC

A comprehensive database and analysis tool for Federal Circuit and Family Court of Australia (Division 2 Family Law) cases from 2021-2024, specifically designed to assist fathers navigating separation and family court proceedings.

## Project Overview

This project implements a Retrieval-Augmented Generation (RAG) system using LangChain and LangSmith as the core platform to analyze and provide insights from the entire Federal Circuit and Family Court of Australia (FedCFamC2F) case database from AustLII for the period 2021-2024. The goal is to create structured, searchable documents that can help fathers better understand and navigate the family court system during separation.

## Key Features

- Complete database of FedCFamC2F cases from 2021-2024
- Structured analysis of case outcomes and patterns
- Searchable documentation of common scenarios and outcomes
- Resources specifically tailored for fathers going through separation
- Insights into court procedures and decision-making patterns
- AI-powered question answering using RAG (Retrieval-Augmented Generation)

## Data Sources

- AustLII Federal Circuit and Family Court of Australia (Division 2 Family Law) database
- Cases from 2021 to 2024
- Full text of judgments and decisions

## Technical Implementation

This project leverages LangChain and LangSmith as the core RAG (Retrieval-Augmented Generation) platform:

- **RAG Architecture**:
  - Document ingestion and chunking
  - Vector embeddings for semantic search
  - Context-aware retrieval
  - LLM-powered response generation

- **Core Technologies**:
  - LangChain for RAG pipeline orchestration
  - LangSmith for monitoring, tracing, and evaluation
  - OpenAI for embeddings and response generation
  - Custom scraping tools for AustLII data collection
  - Vector database for efficient document retrieval

## Setup

1. Clone the repository:
```bash
git clone https://github.com/adamd40/father-assist-lc.git
cd father-assist-lc
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

- `data/`: Scraped case files and processed data


## Requirements

- Python 3.12+
- Jupyter Notebook
- LangChain
- OpenAI API access
- Web scraping tools
- Data processing libraries

## Usage

1. Start Jupyter Notebook:
```bash
jupyter notebook
```

2. Open `testing.ipynb` to run and test the application

## Contributing

We welcome contributions from:
- Legal professionals
- Data scientists
- Fathers who have been through the system
- Family law advocates

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Disclaimer

This project is for informational purposes only and does not constitute legal advice. Users should always consult with qualified legal professionals for specific legal matters.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 