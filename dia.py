import streamlit as st
# import google.generativeai as genai
from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from langchain_groq import ChatGroq



st.set_page_config(page_title='Disease Analysis')


safety_settings=[
                 {
                     "category": "HARM_CATEGORY_HARASSMENT",
                     "threshold": "BLOCK_ONLY_HIGH"
                 },
                 {
                     "category": "HARM_CATEGORY_HATE_SPEECH",
                     "threshold": "BLOCK_ONLY_HIGH"
                 },
                 {
                     "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                     "threshold": "BLOCK_ONLY_HIGH"
                 },
                 {
                     "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                     "threshold": "BLOCK_ONLY_HIGH"
                 },
             ]

system_prompt="""
As a highly skilled medical practitioner specializing in disease symptoms analysis, you are tasked with examining disease symptoms for a renowned hospital. Your expertise is crucial in identifying any anomalies, diseases, or health issues that may be present in the disease symptoms.

Your Responsibilities include:

1. Detailed Analysis: Thoroughly analyze each disease symptoms, focusing on identifying any abnormal findings.
2. Findings Report: Document all observed anomalies or signs of disease. Clearly articulate these findings in a structured format.
3. Recommendations and Next Steps: Based on your analysis, suggest potential next steps, including further tests or treatments as applicable.
4. Treatment Suggestions: If appropriate, recommend possible treatment options or interventions.

Important Notes:

1. Scope of Response: Only respond if the symptoms pertains to human health issues.
2. Clarity of symptoms: In cases where the symptoms quality impedes clear analysis, note that certain aspects are 'Unable to be determined based on the provided symptom'.
2. Disclaimer: Accompany your analysis with the disclaimer: "Consult with a Doctor before making any decisions", only if symptoms pertains to human health issues .

3.Your insights are invaluable in guiding clinical decisions. Please proceed with the analysis, adhering to the structured approach outlined above.

Please provide me an output response with these 4 headings Detailed Analysis, Findings Report, Recommendations and Next Steps, Treatment Suggestions

symptoms:\n {symptoms}?\n
"""





st.title('Disease Diagnose')

txt = st.text_area(
    "Symptoms to analyze",

    )

submit=st.button('Diagnose...')

if submit:

    # llm = GoogleGenerativeAI(model="gemini-pro", google_api_key='AIzaSyCCC9UN48NFIiTv4tTGb2SKR2HRHy93ZXk')
    llm=ChatGroq(model_name="llama3-8b-8192", groq_api_key="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")

    prompt = PromptTemplate.from_template(system_prompt)

    chain = prompt | llm



    if chain:
      st.title('Analysis: ')
      ans = chain.invoke({"symptoms": txt})

      if hasattr(ans, "content"): 
          st.write(ans.content)
      else:
          st.write(ans) 








