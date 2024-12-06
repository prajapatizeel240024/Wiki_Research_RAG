# Wiki_Research_RAG

![image](https://github.com/user-attachments/assets/6b87892f-d210-4d4a-9e5b-a1a5c0472c46)

This project is a web-based application built using Streamlit, OpenAI GPT, and LangChain. The application provides interactive tools to query Wikipedia and ArXiv research papers. It maintains chat histories for each query, allowing users to interact effectively and track their conversations.

---

## Features

### 1. **User Interaction Layer**
- **User Input Options:**
  - **Search Wikipedia:** Allows users to input queries to retrieve summarized information from Wikipedia.
  - **Search ArXiv Papers:** Enables querying research papers from the ArXiv database.
- **Chat History:** Maintains a history of user queries and responses for each tool to provide context for ongoing conversations.

### 2. **Application Frontend (Streamlit)**
- **Streamlit Framework:** Serves as the user interface for the application. It includes:
  - Input fields for queries.
  - Navigation between "Search Wikipedia" and "Search ArXiv Papers."
  - Display of chat history and results.

### 3. **Core Processing Layer (OpenAI LLM)**
- **LLM (OpenAI GPT):** Processes user queries and interacts with external tools (LangChain agents) to perform tasks such as summarizing Wikipedia content or retrieving ArXiv papers.

### 4. **Tool Integration Layer (LangChain Agents)**
- **Agents Through LangChain Toolkit:**
  - **Wikipedia Agent:** Retrieves summarized data from Wikipedia.
  - **ArXiv Agent:** Searches and fetches research papers from ArXiv.

### 5. **Data Flow and Interactions**
- User inputs are processed through the Streamlit frontend and passed to the OpenAI LLM.
- The LLM routes the query to the appropriate agent using LangChain's toolkit.
- The agents fetch the required data and return it to the LLM for processing.
- The processed response is displayed on the Streamlit interface, and chat history is updated.

---

## Key Features

- **Modularity:** Separate modules for Wikipedia and ArXiv allow for future extensibility (e.g., adding more tools).
- **Integration:** Combines Streamlit for UI, OpenAI GPT for query processing, and LangChain for managing tools.
- **Chat History:** Tracks interactions to improve user experience and provide conversational context.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- [pip](https://pip.pypa.io/en/stable/)

### Clone the Repository
```bash
git clone https://github.com/your-username/interactive-search-tools.git
cd interactive-search-tools
```

### Install Dependencies
Install the required Python libraries from the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

---

## Configuration

### Set up Environment Variables
Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key
```

---

## How to Run

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
2. Open the link displayed in your terminal to access the web application.

---

## Project Structure

```
interactive-search-tools/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── .env                   # Environment file for API keys
├── README.md              # Project documentation
```

---

## Requirements

### `requirements.txt`
```plaintext
streamlit
python-dotenv
langchain
langchain-community
openai
faiss-cpu
```

---

## Future Enhancements

1. **Expand Data Sources:** Integrate additional tools or APIs for querying other datasets or resources.
2. **Unified Frontend:** Combine all tools into a single page using React for improved user experience.
3. **PDF Interaction:** Enhance capabilities to process larger PDF files beyond the current limit.
4. **Deployment:** Deploy the application for public use.
5. **Outlook Integration:** Add support for Outlook email data once permissions are obtained.

---

## License
[MIT License](LICENSE)
