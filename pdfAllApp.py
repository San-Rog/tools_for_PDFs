import streamlit as st

def main():
    dictPages = {'Tela Inicial': [r"C:\Users\ACER\Desktop\streamlit\pdfInitial.py", "🏠"], 
                 'Ferramentas/PDF/Único': [r"C:\Users\ACER\Desktop\streamlit\pdfUnique.py", "✴️"], 
                 'Ferramentas/PDF/Múltiplos': [r"C:\Users\ACER\Desktop\streamlit\pdfMult.py", "✳️"]}
    pages = []
    keyPages = list(dictPages.keys())
    for l, key in enumerate(keyPages):
        dataPages = dictPages[key]        
        if l == 0:
            newPage = st.Page(page=dataPages[0], title=key, icon=dataPages[1], default=True)
        else:
            newPage = st.Page(page=dataPages[0], title=key, icon=dataPages[1])
        pages.append(newPage)
    pg = st.navigation(pages, position="top", expanded=True)
    pg.run()

if __name__ == '__main__':
    nameApp = 'Ferramentas PDF'
    st.set_page_config(page_title=nameApp,  page_icon=":material/files:", 
                       layout='wide')
    with open(r'C:\Users\ACER\Documents\configuration.css') as f:
        css = f.read()
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
    main()
