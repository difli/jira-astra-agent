# JIRA-Astra-Agent

## Overview

**JIRA-Astra-Agent** is a smart agent-powered application designed for managing and interacting with JIRA data stored in an Astra DB collection. The agent enables querying, similarity searches, and data ingestion, leveraging state-of-the-art tools like [LangChain](https://python.langchain.com/docs/introduction/), [LangGraph](https://langchain-ai.github.io/langgraph/), [Astra DB](https://astra.datastax.com/), and [OpenAI](https://platform.openai.com/api-keys).

---

## Features

- Query JIRA issues using parameters like issue ID, issue key, project key, or status.
- Perform vector-based similarity searches to find issues similar to a specified issue.
- Ingest filtered JIRA issue data into Astra DB with structured metadata.
- Utilize LangChain and LangGraph for intelligent workflows and tool integration.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/difli/jira-astra-agent.git
   cd jira-astra-agent
   ```

2. Set up a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   Create a `.env` file in the root directory with the following variables:
   ```env
   ASTRA_DB_APPLICATION_TOKEN=your_astra_db_token
   ASTRA_DB_API_ENDPOINT=your_astra_db_endpoint
   ASTRA_COLLECTION_NAME=your_collection_name
   OPENAI_API_KEY=your_openai_api_key
   ```

5. Ingesting Data
   The `ingest_filtered_issues.py` script ingests JIRA issue data into Astra DB.

   1. Run the script:
      ```bash
      python ingest_filtered_issues.py
      ```

   The script reads all JSON files ending with `_filtered.json` in folder `filtered_issue_data`, extracts the `id` field as the document ID, and inserts the data into Astra DB.

---

## Usage

### Running the Agent
The agent provides an interactive CLI for querying JIRA data.

```bash
python app.py
```

#### Example Queries
- **Query an issue by key:**  
  *"What is the status of issue TES-10?"*
  
- **Find similar issues:**  
  *"Which issues are similar to TES-10?"*

- **Query issues in a project:**  
  *"What are the issues in project TES?"*

---

## Project Structure

```plaintext
JIRA-Astra-Agent/
├── app.py                          # Main CLI application
├── agents/
│   ├── agent.py                    # Agent implementation
│   ├── tools/
│   │   ├── json_query.py           # Tool for querying Astra DB
│   │   ├── find_similar_issues.py  # Tool for finding similar issues
├── filtered_issue_data/            # Directory for storing filtered JIRA issue JSON files
├── ingest_filtered_issues.py       # Script to ingest filtered JSON data into Astra DB
├── requirements.txt                # Python dependencies
├── .env                            # Environment variables (not included in the repo)
└── README.md                       # Project documentation
```

---

## Tools and Technologies

- **Python**: Core programming language.
- **Astra DB**: The [best hybrid vector database](https://www.datastax.com/resources/report/forrester-wave-names-datastax-leader-vector-databases). Used for storing JIRA data.
- **LangChain**: Framework for integrating tools and building intelligent workflows.
- **LangGraph**: State-based framework for orchestrating complex workflows with tools and memory.
- **OpenAI**: Provides GPT-4 capabilities for query processing.
- **dotenv**: Manages environment variables.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push the branch:
   ```bash
   git push origin feature-name
   ```
5. Create a Pull Request on the main repository.

---

## Support

If you encounter any issues or have questions, feel free to open an issue on the repository or contact the maintainer.