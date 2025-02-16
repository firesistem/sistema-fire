import streamlit as st
import pandas as pd

# Função para ler a planilha
def ler_planilha(arquivo):
    try:
        df = pd.read_excel(arquivo, sheet_name=0)  # Tenta ler a primeira aba
        return df
    except Exception as e:
        st.error(f"Erro ao ler o arquivo: {e}")
        return None

# Função para obter a ocupação com base no tipo de edificação
def obter_ocupacao(df, tipo_edificacao):
    try:
        # Imprime os nomes das colunas para verificar
        print("Nomes das colunas no DataFrame:", df.columns)

        # Use lower() para comparar sem diferenciar maiúsculas/minúsculas
        ocupacao = df[df['Tipo de edificação'].str.lower() == tipo_edificacao.lower()]['Ocupação'].iloc[0]
        return ocupacao
    except IndexError:
        return "Não encontrada"
    except KeyError as e:
        st.error(f"Coluna não encontrada: {e}")
        return None

# Interface Streamlit
st.title("DIMENSIONAMENTO DOS SISTEMAS CONTRA INCÊNDIO E PÂNICO")

# Leitura da planilha
arquivo = "ocupação.xlsx"  # Nome do arquivo (deve estar no mesmo diretório)
# SE O ARQUIVO ESTIVER EM OUTRO DIRETÓRIO, MODIFIQUE A LINHA ACIMA
# Ex: arquivo = "C:/Users/mathe/Documents/PYTHON CURSO/INCÊNDIO/ocupação.xlsx"
df = ler_planilha(arquivo)

if df is not None:
    # Tratamento de erros
    try:
        # Imprime os nomes das colunas para verificar
        print("Nomes das colunas no DataFrame:", df.columns)

        # Input para selecionar o tipo de edificação
        tipo_selecionado = st.selectbox("Selecione o Tipo de Edificação", df['Tipo de edificação'].unique())

        # Exibição da ocupação correspondente
        if tipo_selecionado:
            ocupacao = obter_ocupacao(df, tipo_selecionado)
            if ocupacao == "Não encontrada":
                st.warning("Nenhuma ocupação correspondente encontrada para este tipo de edificação.")
            elif ocupacao is not None:
                st.write(f"A ocupação correspondente é: {ocupacao}")

    except KeyError as e:
        st.error(f"Coluna não encontrada: {e}") 