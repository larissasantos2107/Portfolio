# modules/records_files.py
import streamlit as st
import pandas as pd
import io

def app(st):
    st.title("Registros e Arquivos em Disco")
    st.markdown("Exemplo de criar, salvar e ler registros (CSV).")

    st.markdown("#### Criar registros (exemplo)")
    data = {
        "id": [1,2,3],
        "nome": ["Ana", "Bruno", "Carla"],
        "edv": [101,102,103]
    }
    df = pd.DataFrame(data)
    st.dataframe(df)

    st.markdown("#### Baixar CSV")
    csv = df.to_csv(index=False).encode()
    st.download_button("Download CSV de exemplo", csv, file_name="registros_exemplo.csv", mime="text/csv")

    st.markdown("#### Fazer upload de arquivo (ler registros)")
    uploaded = st.file_uploader("Envie um CSV com colunas: id, nome, edv", type=["csv"])
    if uploaded:
        df2 = pd.read_csv(uploaded)
        st.write("Arquivo carregado:")
        st.dataframe(df2)
        st.success("Arquivo lido com sucesso!")

    #  DOCUMENTAÇÃO DO EXERCÍCIO
    with st.expander("📄 Documentação"):
        st.markdown("""
### **Objetivo**
Demonstrar como criar registros em memória usando pandas, salvar dados em um arquivo CSV e realizar a leitura de arquivos enviados pelo usuário.

### **Descrição**
Este módulo apresenta três partes principais:

1. **Criação de registros (DataFrame)**  
   Um conjunto de dados simples é criado usando um dicionário Python e convertido para DataFrame com `pandas.DataFrame()`.

2. **Geração e Download de Arquivo CSV**  
   O DataFrame é convertido para CSV usando `df.to_csv()`, codificado como bytes e disponibilizado ao usuário via `st.download_button()`.

3. **Upload e Leitura de Arquivos**  
   O usuário pode enviar um arquivo CSV contendo colunas pré-definidas.  
   O arquivo é lido com `pandas.read_csv()` e exibido na tela usando `st.dataframe()`.

### **Funcionalidades Utilizadas**
- Manipulação de dados com **Pandas**
- Criação de arquivos CSV
- Upload de arquivos via Streamlit
- Exibição de tabelas com `st.dataframe()`
- Geração de feedback com `st.success()`

### **Conceitos Reforçados**
- Estruturas de dados tabulares
- Conversão e persistência de dados em arquivos
- Interação com o usuário por meio de uploads/downloads
- Leitura e validação básica de arquivos externos
        """)
