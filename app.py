import streamlit as st
from pathlib import Path
import google.generativeai as genai


st.set_page_config(page_title='Skin Disease Analysis')


genai.configure(api_key='AIzaSyCCC9UN48NFIiTv4tTGb2SKR2HRHy93ZXk')

generation_config={
    'temperature':0.4,
    'top_p':1,
    'top_k':32,
    'max_output_tokens':4096,
}


safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]


# system_prompt="""
# As a highly skilled medical practitioner specializing in image analysis, you are tasked with examining medical images for a renowned hospital. Your expertise is crucial in identifying any anomalies, diseases, or health issues that may be present in the images.
#
# Your Responsibilities include:
#
# 1. Detailed Analysis: Thoroughly analyze each image, focusing on identifying any abnormal findings.
# 2. Findings Report: Document all observed anomalies or signs of disease. Clearly articulate these findings in a structured format.
# 3. Recommendations and Next Steps: Based on your analysis, suggest potential next steps, including further tests or treatments as applicable.
# 4. Treatment Suggestions: If appropriate, recommend possible treatment options or interventions.
#
# Important Notes:
#
# 1. Scope of Response: Only respond if the image pertains to human health issues.
# 2. Clarity of Image: In cases where the image quality impedes clear analysis, note that certain aspects are 'Unable to be determined based on the provided image'.
# 3. Disclaimer: Accompany your analysis with the disclaimer: "Consult with a Doctor before making any decisions.
#
# 4.Your insights are invaluable in guiding clinical decisions. Please proceed with the analysis, adhering to the structured approach outlined above.
#
# Please provide me an output response with these 4 headings Detailed Analysis, Findings Report, Recommendations and Next Steps, Treatment Suggestions
# """


system_prompt="""
As a highly skilled medical practitioner specializing in image analysis, you are tasked with examining medical images for a renowned hospital. Your expertise is crucial in identifying any anomalies, diseases, or health issues that may be present in the images.

Your Responsibilities include:

1. Detailed Analysis: Thoroughly analyze each image, focusing on identifying any abnormal findings.
2. Findings Report: Document all observed anomalies or signs of disease. Clearly articulate these findings in a structured format.
3. Recommendations and Next Steps: Based on your analysis, suggest potential next steps, including further tests.
# 4. Treatment Suggestions: If appropriate, recommend possible treatment options or interventions.

Important Notes:

1. Scope of Response: Only respond if the image pertains to human health issues.
2. Clarity of Image: In cases where the image quality impedes clear analysis, note that certain aspects are 'Unable to be determined based on the provided image'.
3. Disclaimer: Accompany your analysis with the disclaimer: "Consult with a Doctor before making any decisions.

4.Your insights are invaluable in guiding clinical decisions. Please proceed with the analysis, adhering to the structured approach outlined above.

Please provide me an output response with these 4 headings Detailed Analysis, Findings Report, Recommendations and Next Steps, Treatment Suggestions
"""


# system_prompt="""
#
# As a highly skilled image analyst, you are tasked with examining a medical image for a renowned hospital. Your expertise is crucial in identifying any potential abnormalities or areas of concern within the image.
#
# Focus on:
#
# * Detailed Analysis: Thoroughly analyze the image, focusing on identifying any abnormalities or areas that might require further investigation.
# * Findings Report: Document all observed abnormalities or areas of concern.
#
# Important Notes:
#
# 1. Scope of Response: Only analyze the image and identify potential issues.
# 2. Clarity of Image: In cases where the image quality impedes clear analysis, note that certain aspects are 'Unable to be determined based on the provided image'.
# 3. Disclaimer: This analysis is for informational purposes only and should not be used for medical diagnosis or treatment decisions. Consult with a Doctor before making any decisions.
#
# Please provide a detailed analysis of the image, highlighting any areas that might need further investigation.
#
# """

model=genai.GenerativeModel(model_name='gemini-pro-vision',
                            generation_config=generation_config,
                            safety_settings=safety_settings)




st.title('Medical Assistant')
uploaded_file=st.file_uploader('Upload the Image ',type=['png','jpg','jpeg'])

if uploaded_file:
    st.image(uploaded_file,width=300, caption='Image')
    print('uploaded')

submit=st.button('Analyse...')

if submit:
    print('submit')
    image_data=uploaded_file.getvalue()

    image_parts=[
        {
            'mime_type': 'image/jpeg',
            'data': image_data
        },
    ]


    prompt_parts=[
        image_parts[0],
        system_prompt,
    ]

    response=model.generate_content([system_prompt,image_parts[0]])
    print(response.prompt_feedback)
    if response:
        st.title('Analysis: ')
        st.write(response.text)

    # try:
    #     response = model.generate_content(prompt_parts)
    #     if response:
    #         # Check for prompt_feedback existence
    #         if hasattr(response, 'prompt_feedback'):
    #             feedback = response.prompt_feedback
    #             st.error(f"The prompt was blocked. Feedback: {feedback}")
    #         else:
    #             st.write(response.text)  # If no feedback attribute, proceed with text
    # except Exception as e:
    #     st.error(f"An error occurred: {e}")





