## Till now we have succesfully built GenAI project
## now lets convert this projetc into application so that end users can use it !
## Like when u Enter Job posting URL  , u will get Entire Mail which u can send it to acquire projects from Nike !

## & thats what Model deployment is !

## So From Data Collection to Data cleaning to RAG to Building RAG , we ahve actually used Jupyter Notebook
## bcz Jupyter NOtebook is quite interactive & easy to use !

## Now when it comes to building applications or model deployment , 
## you may have to write some dashboarding script, or deubg some program !

## So in general, for all these tasks, it's a good idea to use some Python centric IDS's like :
## Iu can use of the IDE that u know off : VS code , PYCharm , Spyder IDE !


## U can launch Anaconda Navigator & Anaconda itself have Spyder & Pycharm !
## we are going to Spyder to write deployment code !

## So this is the UI of Spyder IDE.

## Over here.
## You can actually think of writing your Python codeto build applications !

## And this bottom right area is extremely important.
## This is a console which u can use : let's say hey I want to install some package, or
## If I want to run some test snippet, or I want to some debug some program..
## That's where you can leverage your console feature.

## so lets write code

## we will be streamlit package to actuallly create such apllication !


## this will be the simple flow to build appliactions !
## By the way , we have used simialar flow in Jupyter ntoebook even to built project !

## It means we have to write same code + some basic modifications in existing code !






# ============================================================
# COLD EMAIL GENERATOR 

import chromadb
import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate ## to write prompt


from langchain_core.output_parsers import JsonOutputParser

json_parser = JsonOutputParser()


# Load API key 





# load vector store so that u can fetch relevant portfolio link !
def load_vectorstore():
    client = chromadb.PersistentClient(path="vectorstore")
    return client.get_collection(name="portfolio")

collection = load_vectorstore()


# ---- PAGE SETUP ----
st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
st.title("📧 Cold Email Generator")

# ---- USER INPUT ----
url_input = st.text_input("Enter a Job Posting URL:", 
                          value="https://careers.nike.com/retail-associate-seas-nike-pasadena/job/R-783632")
submit_button = st.button("Generate Email")

# ---- MAIN LOGIC (runs when button is clicked) ----
if submit_button:

    # ========== STEP 1: SCRAPE WEBSITE ==========
    try:
        loader = WebBaseLoader([url_input])
        page_data = loader.load().pop().page_content
    except:
        st.error("Failed to load website. Please check the URL.")
        st.stop()
        
        
        
    # ========== STEP 2: LLM SETUP ==========
    llm = ChatGroq(
        temperature = 0,
        groq_api_key = api_key,
        model_name = "llama-3.3-70b-versatile"
    )

    # ========== STEP 3: EXTRACT JOB DETAILS using LLM ==========
    prompt_extract = PromptTemplate.from_template(
    """
    
    
    ### Scraped Text from website :
    {page_data}
    
    ###Instructions:
    The scraped text is from the Careers page of Nike
    Your Job is to extract job postings & return them in JSON Format containing following keys :
    "role" , "experience" , "skills" and "description"
    
    Only return the valid JSON
    No ```
    ### valid JSON in key:value (NO PREAMBLE)
    
    
    
    
    
    
    """
    
    
    )
    chain = prompt_extract | llm
    response = chain.invoke({"page_data" : page_data})

    job_text = response.content
    json_response = json_parser.parse(response.content)



    # Step 5: Query Vector DB
    portfolio_links = collection.query(
        query_texts = json_response["skills"],
        n_results=2
    ).get("metadatas", [])
    
    
        
    # Step 6: Ask LLM to write the cold email
    st.info("Writing cold email...")
    email_prompt = f"""
    Here is a job description:
    {job_text}
    

    ### Instructions :
        
    You are **Saurabh** , a BDE at **Accenture**
    Deloitte is an AI & Software Consulting company that helps businesses automate their processes.
    Your Job is to write a cold email to the client regarding the job mentioned above describing capability of **Accenture**
    in fulfilling their needs  , also add the most relevant ones from the following links sto showcase Accenture's portfolio :
    {portfolio_links}

    Do not write explanation. Only the email.
    Remember , You are **Saurabh** , a BDE at **Accenture**
    Do not provide a preamble

    ### EMAIl( NO PREAMBLE)
    """
    email_response = llm.invoke(email_prompt)
    email_text = email_response.content

    # Step 7: Show the result
    st.success("Email generated!")
    st.markdown(email_text)
    
    
    