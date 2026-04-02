import hashlib
import time
from multiprocessing import Pool
import math


# 1. FUNÇÃO DO WORKER (O HOST DISTRIBUÍDO)

def quebrar_pedaco(dados):
    
    hash_alvo, pedaco_palavras, id_host = dados
    
    # O Worker varre apenas o seu pedaço da lista
    for palavra in pedaco_palavras:
        hash_teste = hashlib.md5(palavra.encode('utf-8')).hexdigest()
        
        if hash_teste == hash_alvo:
            return (id_host, palavra) # Retorna quem achou e a senha
            
    return None # Caso nao achar o pedaco


# 2. FUNÇÃO DO MASTER (COORDENADOR)

def iniciar_ataque_distribuido(hash_alvo, dicionario, num_hosts):
    print(f"\n[*] Configurando cluster com {num_hosts} hosts (workers)...")
    
    # Calcula o tamanho do pedaço para cada host
    tamanho_lista = len(dicionario)
    tamanho_pedaco = math.ceil(tamanho_lista / num_hosts)
    
    # Divide o dicionário em fatias e prepara o pacote de dados para envio
    tarefas = []
    for i in range(num_hosts):
        inicio = i * tamanho_pedaco
        fim = inicio + tamanho_pedaco
        pedaco = dicionario[inicio:fim]
        
        # Cria a "caixa" que será enviada ao host: (hash, lista_de_palavras, ID_do_host)
        tarefas.append((hash_alvo, pedaco, i+1))
        
    print(f"[*] Dicionário de {tamanho_lista} senhas dividido em {num_hosts} blocos.")
    
    start_time = time.time()
    
    # Inicia o Pool de processos
    # Isso simula os computadores paralelos usando os núcleos da CPU
    resultado_encontrado = None
    with Pool(processes=num_hosts) as pool:
        # Dispara todos os hosts ao mesmo tempo
        resultados = pool.imap_unordered(quebrar_pedaco, tarefas)
        
        for res in resultados:
            if res is not None:
                resultado_encontrado = res
                pool.terminate() # Se um achou, manda os outros pararem
                break

    end_time = time.time()
    tempo_gasto = end_time - start_time
    
    return resultado_encontrado, tempo_gasto


# EXECUÇÃO E BENCHMARK

if __name__ == '__main__':
    # Preparando o laboratório (Criando peso para a CPU)
    print("[*] Gerando dicionário gigante em memória (Aguarde...)")
    senha_real = "senha_secreta_final"
    hash_alvo = hashlib.md5(senha_real.encode('utf-8')).hexdigest()
    
    # Gera 5 milhões de senhas erradas e coloca a certa no final
    # Isso garante que a CPU vai ter que suar para achar
    dicionario_gigante = [f"teste_senha_{i}" for i in range(5000000)]
    dicionario_gigante.append(senha_real) 
    
    # Definindo os cenários de teste para o Professor
    # Vamos testar com 1, 2, 4, 8 e 16 hosts paralelos
    cenarios_hosts = [1, 2, 4, 8, 16]
    
    print("\n" + "="*50)
    print(" INICIANDO BENCHMARK DISTRIBUÍDO ")
    print("="*50)
    
    for num in cenarios_hosts:
        res, tempo = iniciar_ataque_distribuido(hash_alvo, dicionario_gigante, num)
        
        if res:
            id_host_vencedor, senha = res
            print(f"[+] Host {id_host_vencedor} quebrou o hash! Senha: '{senha}'")
            print(f"[!] TEMPO COM {num} HOST(S): {tempo:.4f} segundos")
        else:
            print("[-] Senha não encontrada.")
        print("-" * 50)