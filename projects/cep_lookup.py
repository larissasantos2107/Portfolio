# projects/cep_lookup.py
import streamlit as st
import requests

def app(st):
    st.header("Consultar CEP (ViaCEP)")
    cep = st.text_input("CEP (apenas números)", value="01001000")

    if st.button("Consultar CEP"):
        try:
            r = requests.get(f"https://viacep.com.br/ws/{cep}/json/", timeout=5)
            data = r.json()

            if data.get("erro"):
                st.error("CEP inválido ou não encontrado.")
            else:
                st.success("CEP encontrado!")
                st.json(data)

        except Exception as e:
            st.error(f"Erro ao consultar CEP: {e}")

    st.markdown("**Observação:** ViaCEP é pública e gratuita, não precisa de chave.**")

    #  DOCUMENTAÇÃO DO PROJETO
    with st.expander("📄 Documentação"):
        st.markdown("""
### **Objetivo**
Demonstrar como consumir uma API pública (ViaCEP) para consultar dados de endereço a partir de um CEP informado pelo usuário.

---

### **Descrição Geral**
Este projeto realiza a consulta de CEP usando a API pública **ViaCEP**, que retorna informações como:

- Logradouro  
- Bairro  
- Cidade  
- Estado  
- Código IBGE  

O usuário digita um CEP e a aplicação faz uma requisição HTTP para obter os dados.

---

### **Funcionamento**
1. O usuário informa um número de CEP (somente dígitos).  
2. Ao clicar em **Consultar CEP**, o app:
   - Faz uma requisição GET para a API ViaCEP.
   - Converte a resposta para JSON.
   - Verifica se o CEP existe.
3. Exibe:
   - Mensagem de erro (se o CEP for inválido).  
   - Ou os dados completos em formato JSON.

---

### **Tecnologias Utilizadas**
- **Streamlit** para a interface.  
- **Requests** para realizar chamadas HTTP.  
- **ViaCEP** como serviço público gratuito de consulta.

---

### **Tratamento de Erros**
A aplicação trata possíveis falhas, como:

- CEP inexistente  
- CEP inválido  
- Falha na conexão  
- Tempo de resposta excedido  

---

### **Conceitos Reforçados**
- Consumo de APIs REST  
- Requisições HTTP GET  
- Manipulação de JSON  
- Validação de entrada de usuário  
        """)
