import streamlit as st
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Título de la aplicación
st.title("Extracción de Texto de Imágenes (OCR)")

# Instrucciones
st.write("Sube una imagen y extrae el texto de su contenido.")

# Subir imagen
uploaded_file = st.file_uploader("Elige una imagen", type=["png", "jpg", "jpeg", "bmp", "tiff", "gif"])

if uploaded_file is not None:
    # Abrir la imagen
    image = Image.open(uploaded_file)

    # Mostrar la imagen subida
    st.image(image, caption="Imagen Subida", use_column_width=True)

    # Botón para extraer el texto
    if st.button("Extraer Texto"):
        # Convertir la imagen a texto usando OCR
        extracted_text = pytesseract.image_to_string(image)
        
        # Mostrar el texto extraído
        st.subheader("Texto Extraído:")
        st.text_area("Resultado", extracted_text, height=300)

        # Opcional: Guardar el texto extraído en un archivo de texto
        st.download_button(
            label="Descargar Texto Extraído",
            data=extracted_text,
            file_name="extracted_text.txt",
            mime="text/plain"
        )
else:
    st.error("Por favor, sube una imagen primero.")