import streamlit as st
import pandas as pd

# Caminho da planilha
caminho_planilha = r"C:\Users\mathe\Documents\PYTHON CURSO\INCÊNDIO\tabela1.xlsx"

# Função para carregar a planilha e extrair os valores da linha 5
def extrair_valores_da_planilha(altura_armazenagem, altura_teto, classe_mercadoria, estrutura_armazenagem):
    try:
        # Carregar a planilha
        df = pd.read_excel(caminho_planilha)
        
        # Verificar se os valores estão dentro dos intervalos especificados
        if 9.10 <= altura_armazenagem <= 10.69 and 10.7 <= altura_teto <= 12.19:
            # Extrair os valores da linha 5 (células 5F, 5G, 5H, 5I e 5J)
            valor_5f = df.iloc[4, 5]  # Linha 5, Coluna F (índice 4, 5)
            valor_5g = df.iloc[4, 6]  # Linha 5, Coluna G (índice 4, 6)
            valor_5h = df.iloc[4, 7]  # Linha 5, Coluna H (índice 4, 7)
            valor_5i = df.iloc[4, 8]  # Linha 5, Coluna I (índice 4, 8)
            valor_5j = df.iloc[4, 9]  # Linha 5, Coluna J (índice 4, 9)
            
            # Retornar os valores
            return valor_5f, valor_5g, valor_5h, valor_5i, valor_5j
        else:
            st.warning("Os valores de Altura de Armazenagem e Altura do Teto não estão nos intervalos especificados.")
            return None, None, None, None, None
    except Exception as e:
        st.error(f"Erro ao carregar a planilha: {e}")
        return None, None, None, None, None

# Interface do Streamlit
st.title("Consulta de Valores da Planilha")

# Seleção do tipo de edificação
Sprinkler = st.selectbox("Tipo de edificação", ["Edificação comum", "Depósito"])

# Condição para aparecer IT 24
if Sprinkler == "Depósito":
    st.title("VOLUME RTI SPRINKLER PARA DEPÓSITO - IT 24")
    
    # Inputs do usuário
    altura_armazenagem = st.number_input('Altura da Armazenagem (m)', value=0.0, step=0.1)
    altura_teto = st.number_input('Altura do Teto (m)', value=0.0, step=0.1)
    classe_da_mercadoria = st.selectbox("Classe da mercadoria", ["classe 1 a 4", "borracha", "plástico"])
    estrutura_de_armazenagem = st.selectbox("Estrutura de Armazenagem", ["Porta-palete sem prateleira sólida", "paletizadas", "pilhas sólidas"])

    # Botão para consultar os valores
    if st.button("Consultar Valores"):
        # Extrair os valores da planilha
        valor_5f, valor_5g, valor_5h, valor_5i, valor_5j = extrair_valores_da_planilha(altura_armazenagem, altura_teto, classe_da_mercadoria, estrutura_de_armazenagem)
        
        # Exibir os valores na interface
        if valor_5f is not None:
            st.success(f"Valor da célula 5F: {valor_5f}")
            st.success(f"Valor da célula 5G: {valor_5g}")
            st.success(f"Valor da célula 5H: {valor_5h}")
            st.success(f"Valor da célula 5I: {valor_5i}")
            st.success(f"Valor da célula 5J (VRTI): {valor_5j}")