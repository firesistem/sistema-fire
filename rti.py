import streamlit as st
import math
import locale

# Configurar o locale para o formato brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

st.title("VOLUME RTI SPRINKLER PARA DEPÓSITO - IT 24")

# Inputs para altura da armazenagem e altura do teto
altura_armazenagem = st.number_input('Altura da Armazenagem (m)', value=0.0, step=0.1)
altura_teto = st.number_input('Altura do Teto (m)', value=0.0, step=0.1)


# Lógica para definir as constantes e exibir os inputs condicionalmente
if altura_armazenagem <= 9.1 and altura_teto <= 10.7:
    k = 200
    p = 5.2
    t = 60  # Duração da RTI constante
    
else:
    k = st.number_input('Fator K', value=0.0, step=0.1)
    p = st.number_input('Pressão (bar)', value=0.0, step=0.1)
    t = st.number_input('Duração da RTI (min)', value=0.0, step=0.1)

# Valor constante
v = 12


# Botão para calcular
if st.button('Calcular Volume da RTI'):
    try:
        vrti = k * math.sqrt(p) * v * t
        vrti_formatted = locale.format_string("%.2f", vrti, grouping=True)
        st.success(f"O valor de Vrti é: {vrti_formatted} Litros")


    except ValueError:
        st.error("Por favor, insira valores numéricos válidos.")
