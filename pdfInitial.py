import streamlit as st

def main():
    with st.expander(label='Sobre este aplicativo', expanded=False, icon="📍"):
        st.write('Esta ferramenta trabalha basicamente com pdf simples.')

if __name__ == '__main__':
    with open('configuration.css') as f:
        css = f.read()
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True) 
    main()


