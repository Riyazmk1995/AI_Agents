from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

class QueryResponder:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=os.getenv("GEMINI_API_KEY"))
        self.prompt = PromptTemplate(
            input_variables=["query", "documents"],
            template="Answer the following query based on the provided documents:\nQuery: {query}\nDocuments: {documents}"
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def respond(self, query, documents):
        response = self.chain.run(query=query, documents=documents)
        return {
            "query": query,
            "response": response
        }