# app.py - Portfólio Lah Queen (Streamlit)
import streamlit as st
from modules import (
    decision_repetition,
    vectors_matrices,
    functions_libs,
    records_files,
    recursion_complexity,
    external_apis,
    utils
)
from projects import cep_lookup, usd_rate, bus_monitor

st.set_page_config(page_title="Portfólio da Larissa", layout="wide", initial_sidebar_state="expanded")

# Header
st.markdown(
    """
    <div style="display:flex;align-items:center;gap:16px">
      <div style="font-size:34px;font-weight:700;color:#2b076e">🌺 Portfólio da Larissa</div>
    </div>
    """,
    unsafe_allow_html=True
)
st.write("---")

# Sidebar navigation (CORRIGIDO — label não está mais vazio)
with st.sidebar:
    st.markdown("## Navegação")

    page = st.radio(
        "Menu principal",
        (
            "Resumo",
            "Decisão e Repetição",
            "Vetores e Matrizes",
            "Funções e Bibliotecas",
            "Registros e Arquivos",
            "Recursividade & Complexidade (Big O)",
            "APIs Externas",
            "Projetos de Aula",
        ),
        label_visibility="collapsed"
    )

# PÁGINAS

# Resumo / Home
if page == "Resumo":
    st.title("Resumo do projeto")
    st.markdown("""
    **Objetivo:** demonstrar os conceitos de algoritmos/estrutura de dados e implementar projetos práticos:
    - Decisão e Repetição
    - Vetores e Matrizes
    - Funções e Bibliotecas
    - Registros e Arquivos em disco
    - Recursividade
    - Complexidade (Big O)
    - Uso de APIs externas
    """)
    st.markdown("---")
    st.markdown("### Como navegar")
    st.write("Use o menu lateral para abrir cada seção. Em 'Projetos de Aula' estão os projetos: CEP, Cotação do Dólar, Monitoramento de Frota")

    #  DOCUMENTAÇÃO DO SISTEMA
    with st.expander("📄 Documentação do Portfólio"):
        st.markdown("""
### **Objetivo Geral do Sistema**
Este portfólio reúne todos os conteúdos desenvolvidos na disciplina de Algoritmos e Estruturas de Dados, incluindo:
- Fundamentos essenciais de lógica de programação  
- Estruturas sequenciais, condicionais e de repetição  
- Vetores e matrizes  
- Modularização com funções e bibliotecas  
- Registros e persistência em arquivos  
- Recursividade e análise de complexidade (Big O)  
- Consumo de APIs  
- Projetos práticos integrando tudo  

A aplicação serve como um **painel interativo**, permitindo executar cada módulo, visualizar códigos, testar algoritmos e rodar aplicações reais integradas a APIs.

---

### **Organização do Sistema**
O projeto está estruturado em **três blocos principais**:

#### **1. Módulos didáticos (`modules/`)**
- Exemplos práticos  
- Interface interativa via Streamlit  
- Demonstrações visuais ou numéricas  
- Explicações teóricas  

#### **2. Projetos práticos (`projects/`)**
- Consulta CEP  
- Cotação do Dólar  
- Monitoramento de Frota  
- Bot Telegram  

#### **3. Aplicação principal (`app.py`)**
Gerencia:
- Navegação  
- Layout  
- Carregamento de módulos  
- Organização geral  

---

### **Fluxo de Uso**
1. O usuário escolhe uma área no menu.  
2. O módulo correspondente é carregado.  
3. O módulo mostra entradas, algoritmo e saída.  
4. Projetos reais podem ser testados diretamente.  

---
        """)

# Decisão e Repetição
elif page == "Decisão e Repetição":
    decision_repetition.app(st)

# Vetores e Matrizes
elif page == "Vetores e Matrizes":
    vectors_matrices.app(st)

# Funções e Bibliotecas
elif page == "Funções e Bibliotecas":
    functions_libs.app(st)

# Registros e Arquivos
elif page == "Registros e Arquivos":
    records_files.app(st)

# Recursividade e Complexidade
elif page == "Recursividade & Complexidade (Big O)":
    recursion_complexity.app(st)

# APIs Externas (exemplos)
elif page == "APIs Externas":
    external_apis.app(st)

# Projetos de Aula
elif page == "Projetos de Aula":
    st.title("Projetos implementados em aula")
    st.markdown("Escolha um projeto para abrir:")

    project = st.selectbox(
        "Selecione um projeto",
        ["Consultar CEP", "Consultar cotação do Dólar", "Monitoramento da frota de ônibus"]
    )

    if project == "Consultar CEP":
        cep_lookup.app(st)
    elif project == "Consultar cotação do Dólar":
        usd_rate.app(st)
    elif project == "Monitoramento da frota de ônibus":
        bus_monitor.app(st)

