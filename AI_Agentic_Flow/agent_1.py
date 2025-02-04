from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

class DocumentSummarizer:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=os.getenv("GEMINI_API_KEY"))
        self.summary_prompt = PromptTemplate(
            input_variables=["document"],
            template="Summarize the following document in one paragraph:\n{document}"
        )
        self.keyword_prompt = PromptTemplate(
            input_variables=["document"],
            template="Extract the top 10 keywords from the following document:\n{document}"
        )
        self.summary_chain = LLMChain(llm=self.llm, prompt=self.summary_prompt)
        self.keyword_chain = LLMChain(llm=self.llm, prompt=self.keyword_prompt)

    def process(self, document):
        summary = self.summary_chain.run(document)
        keywords = self.keyword_chain.run(document)
        return {
            "document_summary": summary,
            "keywords": keywords.split(", ")
        }