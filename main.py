import streamlit as st
import google.generativeai as genai
import os
# from dotenv import load_dotenv
from IPython.display import display
from IPython.display import Markdown
import textwrap

# load_dotenv()  # loading all the environment variables
from PIL import Image
import time

genai.configure(api_key='AIzaSyCCC9UN48NFIiTv4tTGb2SKR2HRHy93ZXk')


def get_gemini_response(input_prompt, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input_prompt, image[0]])
    return response.text


def input_image_setup(uploaded_file):
    # check if a file hasbeen uploaded

    if uploaded_file is not None:
        # read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


# initialize our streamlit app frontend

st.set_page_config(page_title="CalorieSense 🦾")

st.header("CalorieSense 🦾")

attention_message = st.empty()  # Create an empty space for the attention message

# Animate the attention message
for i in range(5):  # You can adjust the number of frames as needed
    attention_message.text(f"👈 Please go to the sidebar for instructions 👈")
    time.sleep(0.75)  # Adjust the sleep duration for the desired speed

# Clear the animated attention message
attention_message.empty()

# Add instructions and project details to the sidebar
with st.sidebar:
    st.markdown("<h2 style='color: #3366ff;'>Welcome to CalorieSense 🦾</h2>", unsafe_allow_html=True)

    st.write(
        "CalorieSense is a tool designed to analyze food images and provide calorie information for each item detected. "
        "It utilizes state-of-the-art Gemini LLM (Large Language Model) to predict calorie counts of each food item present in the picture, akin to a virtual nutritionist. "
        "Additionally, CalorieSense assesses the healthiness of the food items captured, providing users with valuable insights into their dietary choices. ")

    st.markdown("<h3 style='color: #3366ff;'>How to Use:</h3>", unsafe_allow_html=True)
    st.write("1.Drag and drop image here.")
    st.write("2.Click the 'Tell me about the total calories' button to get the results.")

    st.markdown("<h3 style='color: #3366ff;'>About Gemini:</h3>", unsafe_allow_html=True)
    st.markdown(
        "- Gemini is indeed a Large Language Model (LLM) developed by Google DeepMind. It was announced in December 2023 and is considered their most capable AI model yet. ")
    st.markdown(
        "- A family of three LLMs: Gemini Ultra, Pro, and Nano, each with different capabilities and resource requirements.")
    st.markdown(
        "- Trained on a massive dataset of text, code, images, audio, and video, making it multimodal, unlike earlier LLMs like LaMDA or PaLM 2. ")
    st.markdown(
        "- Capable of various tasks, including text generation, translation, question answering, code generation, and more.")

    # Add contact information at the end
    st.markdown("---")
    st.subheader("Contact Information:")
    st.write("For any inquiries or feedback, feel free to reach out:")
    st.write("📧 Email: [gokuldas127199544@gmail.com](mailto:gokuldas127199544@gmail.com)")
    st.write("📷 Instagram: [gokul_mundott](https://www.instagram.com/gokul_mundott/)")

import streamlit as st

st.markdown("<h6>Choose a food image....</h6>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the total calories")

input_prompt = """
You are a skilled medical practitioner specializing in image analysis for a prestigious healthcare institution. Your expertise is vital in detecting and diagnosing diseases or anomalies from medical images.

Your Responsibilities Include:

1. Image Examination: Conduct a thorough analysis of each medical image, focusing on identifying any abnormal findings or signs of disease.
2. Diagnostic Report: Document all observed anomalies or abnormalities in a structured format, providing detailed descriptions and relevant medical terminology.
3. Differential Diagnosis: Based on your analysis, propose potential differential diagnoses or likely conditions that may explain the observed abnormalities.
4. Treatment Recommendations: If applicable, suggest potential treatment options or interventions based on the diagnosed condition.
5. Prognosis Assessment: Assess the potential prognosis or expected outcomes associated with the identified condition, considering factors such as severity and treatment efficacy.

Please adhere to the following guidelines:
- Detailed Analysis: Ensure meticulous examination of all aspects of the medical image to avoid overlooking any relevant details.
- Clear Reporting: Present your findings and recommendations in a concise and organized manner, facilitating understanding by healthcare professionals.
- Clinical Justification: Support your diagnostic conclusions and treatment recommendations with evidence-based reasoning and medical literature.

Format for Diagnostic Report:
1. Identified Anomaly: Description of abnormal finding - Possible diagnosis or differential diagnosis
   - Clinical Justification: Explanation supporting the diagnostic conclusion

Additional Notes:
- When encountering images with unclear or ambiguous findings, indicate limitations in analysis due to image quality.
- Your insights are invaluable in guiding clinical decision-making and patient management. Proceed with your analysis, adhering to the outlined approach.

"""

if submit:
    if uploaded_file is None:
        warning_message = st.warning("No file uploaded. Please upload an image file before proceeding.")
        time.sleep(3)  # Display the warning for 3 seconds
        warning_message.empty()  # Clear the warning message

    else:
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(input_prompt, image_data)
        st.header("The Response is")
        st.write(to_markdown(response.text))