# modules/recursion_complexity.py
import streamlit as st
from modules.utils import timeit, big_o_example_n

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

def app(st):
    st.title("Recursividade & Complexidade")
    st.markdown("Exemplo de recursividade (fatorial) e explicação do Big O.")

    n = st.number_input("n para fatorial recursivo", value=6, min_value=0, max_value=20)
    if st.button("Calcular (recursivo)"):
        res, t = timeit(factorial_recursive, n)
        st.write(f"Factorial({n}) = {res}  (tempo: {t:.6f}s)")

    st.markdown("### Explicações sobre Big O")
    st.write("""
    - O(1): tempo constante\n
    - O(n): tempo linear\n
    - O(n^2): tempo quadrático\n
    - O(log n): tempo logarítmico
    """)

    m = st.slider("Tamanho n para exemplo O(n) (medir tempo)", 1000, 100000, 5000, step=1000)
    _, t_lin = timeit(big_o_example_n, m)
    st.write(f"Exemplo O(n) com n={m} demorou {t_lin:.6f}s (depende da máquina).")

    #  DOCUMENTAÇÃO DO EXERCÍCIO
    with st.expander("📄 Documentação"):
        st.markdown("""
### **Objetivo**
Demonstrar o funcionamento de funções recursivas e apresentar conceitos fundamentais de análise de complexidade algorítmica (Big O).

### **Descrição**
O módulo possui duas partes principais:

1. **Cálculo de Fatorial com Recursividade**  
   Uma função recursiva `factorial_recursive()` é utilizada para calcular o fatorial de um valor `n`.  
   O tempo de execução é medido com a função utilitária `timeit()`.

2. **Demonstração de Complexidade Big O**  
   O módulo apresenta explicações dos principais tipos de complexidade:
   - O(1) — Constante  
   - O(n) — Linear  
   - O(n²) — Quadrática  
   - O(log n) — Logarítmica  

   Em seguida, o usuário pode executar um exemplo prático da complexidade **O(n)** usando a função `big_o_example_n()`.

### **Funcionalidades Utilizadas**
- Recursividade para cálculo de fatorial
- Medição de tempo de execução
- Explicação didática sobre Big O
- Ajuste interativo de valores via Streamlit

### **Conceitos Reforçados**
- Chamadas recursivas e pilha de execução  
- Crescimento do tempo de execução conforme o tamanho da entrada  
- Diferença entre tipos de complexidade algorítmica  
- Importância da análise de eficiência em algoritmos  
        """)
