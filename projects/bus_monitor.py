# projects/bus_monitor.py
import streamlit as st
import pandas as pd
import pydeck as pdk

def app(st):
    st.header("Monitoramento da frota de ônibus")
    st.markdown("Faça upload de um CSV com colunas: id,latitude,longitude,status (em_rota|parado|manutencao).")

    uploaded = st.file_uploader("CSV frota", type=["csv"])

    if uploaded:
        df = pd.read_csv(uploaded)
        st.dataframe(df)

        if "latitude" in df.columns and "longitude" in df.columns:

            st.map(df.rename(columns={"latitude": "lat", "longitude": "lon"})[["lat", "lon"]])

            midpoint = (df["latitude"].mean(), df["longitude"].mean())

            st.write("Mapa interativo (pydeck)")
            layer = pdk.Layer(
                "ScatterplotLayer",
                data=df,
                get_position='[longitude, latitude]',
                get_radius=100,
                pickable=True
            )

            view = pdk.ViewState(
                latitude=midpoint[0],
                longitude=midpoint[1],
                zoom=11,
                pitch=0
            )

            r = pdk.Deck(layers=[layer], initial_view_state=view)
            st.pydeck_chart(r)

        else:
            st.warning("O CSV precisa conter as colunas 'latitude' e 'longitude'.")

    else:
        st.info("Envie um CSV de exemplo. (Você pode gerar um com colunas: id,latitude,longitude,status).")

    #  DOCUMENTAÇÃO DO PROJETO
    with st.expander("📄 Documentação"):
        st.markdown("""
### **Objetivo**
Criar um sistema simples de monitoramento de frota de ônibus usando mapas, upload de dados e visualização geográfica interativa.

---

### **Descrição Geral**
Este projeto permite ao usuário carregar um arquivo CSV contendo os dados da frota de ônibus, incluindo:

- **id**
- **latitude**
- **longitude**
- **status** (em_rota, parado, manutencao)

A aplicação então exibe:

1. **Tabela completa dos dados enviados**
2. **Mapa básico usando `st.map()`**
3. **Mapa interativo avançado com PyDeck**

---

### **Requisitos do CSV**
O arquivo deve conter obrigatoriamente as colunas:

| Coluna | Descrição |
|--------|-----------|
| `latitude` | Latitude do ônibus |
| `longitude` | Longitude do ônibus |
| `id` | Identificador do veículo |
| `status` | Situação atual |

Se as colunas de localização estiverem ausentes, a aplicação exibe um aviso ao usuário.

---

### **Funcionalidades do Mapa**
- **st.map()**  
  Exibe rapidamente os pontos no mapa usando Streamlit.

- **PyDeck (deck.gl)**  
  Permite visualização avançada com:
  - Camada `ScatterplotLayer`
  - Marcadores interativos
  - Raio personalizado
  - Visualização baseada em coordenadas médias (centro do mapa)

---

### **Conceitos Reforçados**
- Leitura de CSV com Pandas  
- Manipulação de dados geográficos  
- Visualização interativa com PyDeck  
- Upload de arquivos em aplicações Streamlit  
- Tratamento de dados e validação de colunas  

---

### **Possíveis Extensões**
- Filtros por status do ônibus  
- Cores diferentes para cada status  
- Atualização em tempo real  
- Histórico de trajetos (tracking)  

        """)
