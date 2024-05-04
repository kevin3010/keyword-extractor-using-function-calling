import streamlit as st
import pandas as pd
from utils import structured_llm


def extract_keywords(job_description, resume):

    job_description_keywords = structured_llm.invoke(
        f"Extract most important technical `Keywords` required for this job in JSON from following Job Description - {job_description}"
    )
    
    resume_keywords = structured_llm.invoke(
        f"Extract `Keywords` in JSON from following Resume - {resume}"
    )
    
    
    return job_description_keywords.Keywords, resume_keywords.Keywords

def highlight_words(word, resume_words):
    return '<span style="color:green;">' + word + '</span>' if word.replace(' ', '').replace(',', '').replace('.', '').replace('-','').lower() in resume_words else word
    
def main(): 
    st.title('Function Calling in Llama3')
    st.caption('powered by Langchain and Groq')
    st.subheader('LinkedIn Keywords extractor')

    job_description = st.text_area(label='Job Description',placeholder='Paste the job description here', height=200)
    resume = st.text_area(label='Resume',placeholder='Paste your resume here', height=200)

    button = st.button('Extract Keywords')

    st.subheader("Keywords")

    if button:

        jd_keywords, resume_words = extract_keywords(job_description, resume)
        resume_words = [ word.replace(' ', '').replace(',', '').replace('.', '').replace('-','').lower() for word in resume_words]
        jd_keywords = [highlight_words(word, resume_words) for word in jd_keywords]

        grid_size = 5
        grid = [jd_keywords[i:i+grid_size] for i in range(0, len(jd_keywords), grid_size)]

        with st.container(border=True):
            for row in grid:
                if len(row) < grid_size:
                    row += [''] * (grid_size - len(row))
                cols = st.columns(len(row))  # Create columns for each word in the row
                for col, word in zip(cols, row):
                    col.markdown(word, unsafe_allow_html=True)
                    
        st.caption('Green words are the ones that are present in your resume')
                    
if __name__ == '__main__':
    main()
            
                
