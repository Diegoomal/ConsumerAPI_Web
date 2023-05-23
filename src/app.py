import streamlit as st
from PIL import Image
import os
import ebeer

def main():
    st.set_page_config(page_title="Envio de Imagem", page_icon=None, layout="centered", initial_sidebar_state="auto")

    st.title("Envio de Imagem")

    uploaded_file = None

    uploaded_file = st.file_uploader("Escolha uma imagem para enviar", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        uploaded_image = Image.open(uploaded_file)
        st.success("Imagem enviada com sucesso!")

    if st.button("Descobrir rótulo") and uploaded_image is not None:
        st.image(uploaded_image, caption="Imagem enviada", use_column_width=True)

        uploaded_image.save('src/upload/img.jpg')

        n_pos = ebeer.BeerClassifier().predict('src/upload/img.jpg')

        st.text(ebeer.labels_index[n_pos]["name"])

if __name__ == "__main__":
    main()
