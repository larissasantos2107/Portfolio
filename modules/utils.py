# modules/utils.py
import math
import time

def timeit(func, *args, **kwargs):
    t0 = time.time()
    res = func(*args, **kwargs)
    t1 = time.time()
    return res, t1 - t0

def big_o_example_n(n):
    # exemplo linear O(n)
    s = 0
    for i in range(n):
        s += i
    return s


# DOCUMENTAÇÃO DO MÓDULO
def documentation(st):
    with st.expander("📄 Documentação"):
        st.markdown("""
### **Objetivo**
Fornecer funções utilitárias usadas nos exercícios de desempenho, recursividade e complexidade algorítmica.

---

### **Funções Incluídas**

#### **1. `timeit(func, *args, **kwargs)`**
Função utilizada para **medir o tempo de execução** de qualquer função Python.

**Como funciona:**
- Marca o tempo inicial.
- Executa a função passada como argumento.
- Marca o tempo final.
- Retorna:
  - O resultado da função executada
  - O tempo gasto em segundos

Essa função permite comparar desempenhos entre soluções diferentes.

---

#### **2. `big_o_example_n(n)`**
Implementa um algoritmo com **complexidade O(n)** para fins de demonstração.

**Descrição:**
- Percorre um loop simples de `0` até `n`
- Soma todos os valores nesse intervalo
- Serve como exemplo prático para medir na prática o tempo de execução de um algoritmo linear.

---

### **Conceitos Reforçados**
- Medição de desempenho de funções
- Diferença entre complexidade teórica e tempo real de execução
- Estrutura de loops lineares
- Ferramentas auxiliares para exercícios de algoritmos

Essas funções são usadas pelos módulos de:
- Recursividade
- Big O
- Avaliação de performance  
        """)
