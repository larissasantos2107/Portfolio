# projects/usd_rate.py
import streamlit as st
import requests

def app(st):
    st.header("Consultar cotação do Dólar")

    if st.button("Consultar agora (USD->BRL)"):
        try:
            r = requests.get(
                "https://economia.awesomeapi.com.br/json/last/USD-BRL",
                timeout=5
            )

            j = r.json()
            rate = float(j["USDBRL"]["bid"])

            st.metric(label="USD → BRL", value=f"1 USD = {rate:.4f} BRL")

            st.write("Dados brutos da API:")
            st.json(j)

        except Exception as e:
            st.error(f"Erro ao consultar cotação: {e}")

    #  DOCUMENTAÇÃO DO PROJETO
    with st.expander("📄 Documentação"):
        st.markdown("""
### **Objetivo**
Consultar em tempo real a cotação do dólar (USD) em relação ao real (BRL) utilizando uma API pública de câmbio.

---

### **Descrição Geral**
A aplicação usa a API **AwesomeAPI**, que não requer chave de acesso, para obter a taxa de conversão entre:

- **USD → BRL**

Quando o usuário clica no botão, uma requisição é enviada e o resultado é exibido:

- Métrica com o valor atual  
- JSON completo retornado pela API  

---

### **Como Funciona**
1. Usuário clica em **"Consultar agora (USD->BRL)"**  
2. O app faz uma requisição GET:  
   `https://economia.awesomeapi.com.br/json/last/USD-BRL`
3. A resposta JSON é convertida para Python.  
4. O valor da chave `"USDBRL"]["bid"]` é exibido como cotação atual.  
5. Em seguida, mostra-se o JSON bruto para fins didáticos.

---

### **Tecnologias Utilizadas**
- **Streamlit** — Interface interativa  
- **Requests** — Realiza a chamada HTTP  
- **API AwesomeAPI** — Fonte dos valores de câmbio  

---

### **Tratamento de Erros**
O código trata:

- Tempo limite excedido  
- Falha de conexão  
- Estrutura inesperada na resposta da API  
- Exceções gerais  

---

### **Conceitos Reforçados**
- Consumo de APIs externas  
- Manipulação de JSON  
- Métricas e exibição elegante com Streamlit  
- Verificação e tratamento de falhas na requisição  
        """)
