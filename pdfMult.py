import pymupdf
import streamlit as st
import streamlit.components.v1 as components
    
def main():
    uploadPdf = st.file_uploader('Selecione um ou mais arquivos PDF.', 
                                  type=['pdf'], 
                                  accept_multiple_files=True)
    if uploadPdf is not None:
        pass
                         
if __name__ == '__main__':
    with open(r'C:\Users\ACER\Documents\configuration.css') as f:
        css = f.read()
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True) 
    main()