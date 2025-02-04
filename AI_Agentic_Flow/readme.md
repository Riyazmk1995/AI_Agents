# AI AgentFlow

## Overview
AI AgentFlow is a modular system of AI agents designed to perform specific tasks efficiently. The system features a Manager Agent that oversees task assignment, selects the most suitable agent(s), and provides comprehensive responses. It integrates modern open-source frameworks, a backend API, and a user-friendly frontend interface built with Streamlit.

## Features
- **Modular AI Agent System**: Each agent performs a distinct task.
- **Manager Agent**: Analyzes input and delegates tasks to appropriate agents.
- **Document Summarization & Keyword Extraction**.
- **Query Resolution based on Provided Documents**.
- **Real-time Web Data Fetching**.
- **Streamlit Frontend** for user interaction.
- **FastAPI Backend** for API handling.
- **Dockerized Deployment** for environment consistency.

## Architecture
### Agents
1. **Document Summarizer & Keyword Extractor** (Agent 1)
   - Uses LangChain & Gemini API for summarization.
2. **Query Responder** (Agent 2)
   - Uses LangChain & Gemini API to answer document-based queries.
3. **Internet-Connected Agent** (Agent 3)
   - Fetches real-time data using SerpAPI.
4. **Manager Agent** (Agent 4)
   - Determines the appropriate agent(s) for a given user query.

## Tech Stack
- **LangChain** - AI agent framework
- **Google Gemini API** - LLM for text processing
- **SerpAPI** - Fetches real-time web information
- **FastAPI** - Backend API
- **Streamlit** - Frontend UI
- **Docker** - Containerization

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Docker (optional, for containerized deployment)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/ai-agentflow.git
   cd ai-agentflow
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
   ```
3. Start the Streamlit frontend:
   ```sh
   streamlit run app/frontend.py
   ```

## Docker Deployment
To run the application in a Docker container:
```sh
docker-compose up --build
```

## Usage
1. Open the Streamlit UI.
2. Upload documents or enter a query.
3. The Manager Agent assigns the task to the appropriate agent.
4. The response is displayed on the UI.

## Workflow
1. **User Input**: User provides a query and/or documents via Streamlit UI.
2. **Manager Agent Analysis**: Determines the best-suited agent(s) for the task.
3. **Agent Execution**:
   - **Agent 1**: Summarizes documents & extracts keywords.
   - **Agent 2**: Responds to queries based on provided documents.
   - **Agent 3**: Fetches real-time data from the web.
4. **Response Consolidation**: Manager Agent compiles the results.
5. **Output to User**: Response displayed on the Streamlit frontend.



## Contributing
Contributions are welcome! Feel free to submit a pull request or raise an issue.

## License
This project is licensed under the MIT License.

---

**Author**: Riyaz Khorasi 
**Email**: riyazkhorasi@gmail.com
