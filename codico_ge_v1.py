import pandas as pd

# Carrega a planilha exportada do SAP
try:
    df_clientes = pd.read_excel('exportacao_sap.xlsx')
except FileNotFoundError:
    print("Erro: Arquivo 'exportacao_sap.xlsx' não encontrado.")
    exit()

# Limpeza básica
df_clientes.dropna(subset=['email', 'nome_cliente'], inplace=True) # Remove linhas sem email ou nome
df_clientes.drop_duplicates(subset=['id_cliente'], inplace=True) # Remove clientes duplicados

print(f"Encontrados {len(df_clientes)} clientes únicos para contatar.")

# Salva uma lista limpa para referência
df_clientes.to_csv('clientes_para_contatar.csv', index=False)
