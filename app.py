import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import spacy

def predict(text: str):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    # Get the pronoun
    target_list = [ token.text for token in doc if token.tag_=="NNP" ]
    return target_list

def main():
    image_path = "./sp_global.png"
    image = Image.open(image_path)
    st.image(image, use_column_width=True)

    st.title("AI engineering group is awesome")

    st.header("Find pronoun")
    user_input = st.text_area("Please type some words.")

    if st.button("Submit"):
        output = predict(str(user_input))
        output_text = " ".join(output)
        st.markdown(
            f"<h3 style='text-align: center; color: black;'>{output_text}</h3>",
            unsafe_allow_html=True)

if __name__ == "__main__":
    main()




