# modules/vectors_matrices.py
import streamlit as st
import numpy as np
import pandas as pd

def app(st):
    st.title("Vetores e Matrizes")
    st.markdown("Operações básicas com listas (vetores) e matrizes (numpy).")

    st.markdown("#### Vetor exemplo")
    vetor = list(map(int, st.text_input("Digite números separados por espaço", "1 2 3 4 5").split()))
    st.write("Vetor:", vetor)
    st.write("Soma:", sum(vetor))
    st.write("Média:", sum(vetor)/len(vetor) if vetor else 0)

    st.markdown("#### Matriz exemplo")
    rows = st.number_input("Número de linhas", 2, 10, 3)
    cols = st.number_input("Número de colunas", 2, 10, 3)

    if st.button("Gerar matriz aleatória"):
        M = np.random.randint(0, 10, size=(rows, cols))
        df = pd.DataFrame(M, columns=[f"C{i}" for i in range(cols)])
        st.dataframe(df)
        st.write("Transposta:")
        st.dataframe(df.T)

    #  DOCUMENTAÇÃO DO EXERCÍCIO
    with st.expander("📄 Documentação"):
        st.markdown("""
### **Objetivo**
Demonstrar operações fundamentais com **vetores (listas)** e **matrizes (arrays NumPy)**, reforçando conceitos de estrutura de dados e manipulação básica.

---

### **Parte 1 – Vetores**
O usuário digita uma sequência de números, que é convertida automaticamente em uma lista de inteiros.

**Operações realizadas:**
- Exibição do vetor  
- Soma dos elementos  
- Média dos valores inseridos  
- Validação para evitar divisão por zero  

---

### **Parte 2 – Matrizes**
O usuário escolhe o **número de linhas e colunas**, e o sistema gera uma matriz aleatória usando NumPy.

**Funcionalidades:**
- Geração de matriz com valores aleatórios (0 a 9)  
- Exibição da matriz em formato de tabela (Pandas DataFrame)  
- Exibição da matriz **transposta**  

---

### **Conceitos Reforçados**
- Vetores: lista, soma, média, manipulação básica  
- Matrizes: geração, visualização, transposição  
- Uso de NumPy para operações matemáticas  
- Uso de DataFrames para exibição estruturada  
- Interação dinâmica com Streamlit  

### **Bibliotecas Utilizadas**
- **NumPy** – Para manipulação de matrizes  
- **Pandas** – Para exibição tabular  
- **Streamlit** – Interface interativa  
        """)
