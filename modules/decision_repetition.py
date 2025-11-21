# modules/decision_repetition.py
import streamlit as st

def generate_table(number: int):
    return [f"{number} x {i} = {number*i}" for i in range(1, 11)]

def app(st):
    st.title("Decisão e Repetição")
    st.markdown("Exemplo: gerar tabuada e uso de decisões (if/else).")
    n = st.number_input("Digite um número para ver a tabuada:", min_value=0, max_value=100, value=2, step=1)
    if st.button("Gerar Tabuada"):
        lines = generate_table(n)
        for l in lines:
            st.write(l)

    st.markdown("### Exemplo de decisão")
    idade = st.slider("Idade:", 0, 100, 20)
    if idade < 18:
        st.warning("Menor de idade")
    elif idade < 65:
        st.success("Adulto")
    else:
        st.info("Idoso")


    # DOCUMENTAÇÃO DO EXERCÍCIO


    with st.expander("📄 Documentação"):
        st.markdown("""
**Objetivo:** Demonstrar o uso das estruturas de decisão e repetição por meio de exemplos simples em Streamlit.

### **Descrição**
Este exercício permite que o usuário gere uma tabuada a partir de um número escolhido.  
Também demonstra o uso de estruturas condicionais exibindo mensagens baseadas na idade selecionada.

### **Estruturas Utilizadas**
- **Decisão:**  
  - `if idade < 18:`  
  - `if st.button("Gerar Tabuada"):`  
- **Repetição:**  
  - Laço `for` para construir a tabuada.
- **Entradas do usuário:**  
  - `st.number_input()`  
  - `st.slider()`
- **Saída de dados:**  
  - `st.write()`  
  - Mensagens de status (`warning`, `success`, `info`)
        """)
