import pandas as pd
from collections import defaultdict

def encontrar_nomes_duplicados(arquivo_excel, coluna_nome='nome'):
    """
    Identifica nomes duplicados em uma coluna específica de um arquivo Excel.
    
    Args:
        arquivo_excel (str): Caminho do arquivo Excel
        coluna_nome (str): Nome da coluna que contém os nomes (padrão: 'nome')
    
    Returns:
        tuple: (dicionário com nomes duplicados, total de nomes únicos)
    """
    try:
        # Ler o arquivo Excel
        df = pd.read_excel('arquivo.xlsx')
        
        # Verificar se a coluna existe
        if coluna_nome not in df.columns:
            print(f"\nErro: Coluna '{coluna_nome}' não encontrada no arquivo.")
            print(f"Colunas disponíveis: {', '.join(df.columns)}")
            return None, 0
        
        # Contar ocorrências de cada nome
        contador_nomes = defaultdict(int)
        nomes_duplicados = {}
        
        for nome in df[coluna_nome]:
            contador_nomes[nome] += 1
        
        # Filtrar apenas os duplicados
        for nome, count in contador_nomes.items():
            if count > 1:
                nomes_duplicados[nome] = count
        
        total_nomes_unicos = len(contador_nomes)
        
        return nomes_duplicados, total_nomes_unicos
    
    except FileNotFoundError:
        print(f"\nErro: Arquivo '{arquivo_excel}' não encontrado.")
        return None, 0
    except Exception as e:
        print(f"\nOcorreu um erro: {str(e)}")
        return None, 0

if __name__ == "__main__":
    print("=== Identificador de Nomes Duplicados em Excel ===")
    
    # Solicitar inputs do usuário
    caminho_arquivo = input("\nDigite o caminho do arquivo Excel (.xlsx): ").strip()
    coluna_nome = input("Digite o nome da coluna que contém os nomes (ou Enter para 'nome'): ").strip() or 'nome'
    
    if not caminho_arquivo.lower().endswith('.xlsx'):
        print("\nPor favor, informe um arquivo com extensão .xlsx")
    else:
        duplicados, total_unicos = encontrar_nomes_duplicados(caminho_arquivo, coluna_nome)
        
        if duplicados is None:
            # Erro já foi mostrado pela função
            pass
        elif not duplicados:
            print(f"\nNenhum nome duplicado encontrado na coluna '{coluna_nome}'.")
            print(f"Total de nomes únicos: {total_unicos}")
        else:
            print(f"\n=== NOMES DUPLICADOS ENCONTRADOS ({len(duplicados)} nomes repetidos) ===")
            
            # Ordenar por quantidade de ocorrências (decrescente)
            for nome, count in sorted(duplicados.items(), key=lambda item: item[1], reverse=True):
                print(f"- '{nome}': {count} ocorrências")
            
            print(f"\n=== RESUMO ===")
            print(f"Total de nomes únicos na coluna '{coluna_nome}': {total_unicos}")
            print(f"Nomes que se repetem: {len(duplicados)}")
            print(f"Porcentagem de repetição: {(len(duplicados)/total_unicos)*100:.1f}%")
            
            # Opção para exportar
            exportar = input("\nDeseja exportar a lista de duplicados? (s/n): ").lower()
            if exportar == 's':
                nome_saida = input("Digite o nome do arquivo de saída (sem extensão): ")
                
                # Criar DataFrame para exportação
                df_export = pd.DataFrame({
                    'Nome': duplicados.keys(),
                    'Ocorrências': duplicados.values()
                }).sort_values('Ocorrências', ascending=False)
                
                df_export.to_excel(f"{nome_saida}_nomes_duplicados.xlsx", index=False)
                print(f"Arquivo salvo como '{nome_saida}_nomes_duplicados.xlsx'")