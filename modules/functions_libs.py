# modules/functions_libs.py
import streamlit as st
import math

def fibonacci(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def app(st):
    st.title("Funções e Bibliotecas")
    st.markdown("Demonstração de funções definidas pelo usuário e uso de libs padrão (math).")
    n = st.slider("Quantos termos de Fibonacci?", 1, 30, 8)
    st.write(fibonacci(n))

    st.markdown("Exemplo: fatorial usando math")
    x = st.number_input("Número para fatorial", value=5, min_value=0)
    if st.button("Calcular fatorial"):
        st.write(math.factorial(x))

    #  DOCUMENTAÇÃO DO EXERCÍCIO
    with st.expander("📄 Documentação"):
        st.markdown("""
**Objetivo:** Demonstrar a criação e uso de funções definidas pelo usuário, bem como o uso de bibliotecas padrão do Python.

### **Descrição**
Este exercício apresenta dois conceitos fundamentais:
1. **Funções próprias** — como a função `fibonacci()`, que gera uma lista com os *n* primeiros termos da sequência.
2. **Bibliotecas padrão** — como a biblioteca `math`, utilizada aqui para calcular o fatorial de um número informado pelo usuário.

O usuário escolhe quantos termos deseja visualizar da sequência de Fibonacci e pode calcular o fatorial de qualquer número inteiro não negativo.

### **Estruturas Utilizadas**
- **Funções definidas pelo usuário:**  
  - `fibonacci(n)`
- **Biblioteca padrão:**  
  - `math.factorial()`
- **Entradas do usuário:**  
  - `st.slider()`  
  - `st.number_input()`
  - `st.button()`
- **Saída de dados:**  
  - `st.write()` para exibir listas e resultados numéricos

### **Conceitos Reforçados**
- Uso de funções próprias para modularização  
- Importação e utilização de bibliotecas Python  
- Estruturas de repetição (`for` no Fibonacci)  
- Lógica matemática e algoritmos básicos  
        """)
