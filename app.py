from time import time
import streamlit as st
import os
from openai import OpenAI
import pandas as pd


# UI

st.set_page_config(page_title="Linkedin AI Post Creator", page_icon=":smiley:", layout="centered")
st.title("Linkedin AI Post Creator")
st.write("Upload excel file with the following columns: 'Audience', 'Topic', 'Pain Point', 'Goal' and get a Linkedin post created by AI.")

# API Key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("Please set the OPENAI_API_KEY environment variable.")
    st.stop()

client = OpenAI(api_key=api_key)

# File upload
uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])

def generate_post(row):

    prompt
    prompt = f"""
    You are a Linkedin personal branding expert. Create a Linkedin post based on the following information:

    audience: {row.Audience}
    topic: {row.Topic}
    pain point:  {row.Pain_Point}
    goal: {row.Goal}


   Rules: 
    - Hook the reader in the first 2 lines
    - Short paragraphs
    - Use emojis
    - Include 3 relevant hashtags at the end of the post
    - CTA at the end of the post. 
    """



    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content


if uploaded_file :
    df = pd.read_excel(uploaded_file)
    st.dataframe(df.head())
    
    if st.button("Generate LinkedIn Posts"):
        with st.spinner("Generating posts..."):
            df["LinkedIn Post"] = df.apply(generate_post, axis=1)
            time.sleep(1)  # Simulate processing time

        st.success("Posts generated!")
        st.dataframe(df)

        st.download_button(
            label="Download Excel with LinkedIn Posts",
            data=df.to_excel(index=False),
            file_name="linkedin_posts_output.xlsx"
        )

