# modules/external_apis.py
import streamlit as st
import requests

def app(st):
    st.title("Uso de APIs Externas (demonstração)")
    st.markdown("Exemplo simples: consultar uma API pública (exchangerate.host) e ViaCEP")

     
    #  EXEMPLO 1 — Cotação USD -> BRL
    st.markdown("#### Exemplo: cotação (USD->BRL)")
    if st.button("Consultar cotação USD/BRL"):
        try:
            # API atualizada — endpoint /convert
            r = requests.get(
                "https://api.exchangerate.host/convert?from=USD&to=BRL",
                timeout=5
            )
            data = r.json()

            # NOVO FORMATO da API
            rate = data["info"]["rate"]

            st.success(f"1 USD = {rate:.4f} BRL (fonte: exchangerate.host)")
            st.json(data)  # opcional
        except Exception as e:
            st.error(f"Erro ao consultar cotação: {e}")

    #  EXEMPLO 2 — ViaCEP
    st.markdown("#### Exemplo: ViaCEP (consulta CEP)")
    cep = st.text_input("Digite um CEP (somente números)", value="01001000")

    if st.button("Consultar CEP"):
        try:
            r = requests.get(f"https://viacep.com.br/ws/{cep}/json/", timeout=5)
            data = r.json()

            if "erro" in data:
                st.error("CEP não encontrado")
            else:
                st.success("CEP encontrado com sucesso:")
                st.json(data)

        except Exception as e:
            st.error(f"Erro: {e}")

    #  DOCUMENTAÇÃO DO EXERCÍCIO
    with st.expander("📄 Documentação"):
        st.markdown("""
**Objetivo:** Demonstrar o uso prático de APIs externas dentro de uma aplicação Streamlit.

### ✔ O que este módulo faz
Este módulo demonstra como integrar APIs reais usando Python + Streamlit, incluindo:

- 🟦 **Cotação USD → BRL** usando a API exchangerate.host  
- 🟪 **Consulta de CEP** usando a API pública ViaCEP  

Essas APIs retornam dados em JSON, e o módulo mostra como:
- Enviar requisições HTTP  
- Interpretar o JSON  
- Exibir os dados para o usuário  
- Tratar erros apropriadamente  
---
        """)
