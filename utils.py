from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List
from langchain_groq import ChatGroq
import streamlit as st



class JobDescription(BaseModel):
    Keywords: List[str] = Field(..., description="List of all keywords extracted from the job description")
    
# with open("job_description.txt", "r") as f:
#     job_description = f.read()
  
job_description = "C++ python "  
  
model = ChatGroq(groq_api_key = st.secrets["GROQ_API_KEY"] , model = 'llama3-70b-8192')
structured_llm = model.with_structured_output(JobDescription, method="json_mode")

if __name__ == '__main__':
    resp = structured_llm.invoke(f"Extract `Keywords` in JSON from following Job Description - {job_description}")

    print(resp.Keywords)
