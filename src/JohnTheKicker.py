import hashlib
import time

def adivinhar_tipo_hash(hash_alvo):
    """Descobre o algoritmo baseado no tamanho da string do hash."""
    tamanho = len(hash_alvo)
    if tamanho == 32:
        return 'md5'
    elif tamanho == 40:
        return 'sha1'
    else:
        return None

def quebrar_hash(hash_alvo, wordlist):
    """Roda o ataque de dicionário contra o hash fornecido."""
    tipo_hash = adivinhar_tipo_hash(hash_alvo)
    
    if not tipo_hash:
        print("[-] Erro: Tamanho de hash inválido. Certifique-se de que é um MD5 (32 chars) ou SHA1 (40 chars).")
        return

    print(f"\n[*] Analisando... Tipo de hash detectado: {tipo_hash.upper()}")
    print(f"[*] Iniciando ataque contra: {hash_alvo}")
    
    start_time = time.time() # Inicia o relógio

    for palavra in wordlist:
        # Codifica a palavra testada
        palavra_bytes = palavra.encode('utf-8')
        
        # Gera o hash da palavra atual
        if tipo_hash == 'md5':
            hash_teste = hashlib.md5(palavra_bytes).hexdigest()
        elif tipo_hash == 'sha1':
            hash_teste = hashlib.sha1(palavra_bytes).hexdigest()
        

        if hash_teste == hash_alvo:
            end_time = time.time()
            tempo_gasto = end_time - start_time
            print(f"\n[+] SUCESSO! A senha foi quebrada: '{palavra}'")
            print(f"[*] Tempo de execução: {tempo_gasto:.6f} segundos")
            return

    end_time = time.time()
    tempo_gasto = end_time - start_time
    print("\n[-] FALHA: A senha não está no nosso dicionário.")
    print(f"[*] Tempo de execução: {tempo_gasto:.6f} segundos")

# ==========================================
# EXECUÇÃO DO PROGRAMA
# ==========================================

# O nosso "Dicionário"
dicionario_senhas = [
    "123456",
    "password",
    "admin",
    "root",
    "secreta",
    "secreta123", # A senha do seu exemplo
    "senha123",
    "qwerty"
]

print("=== QUEBRADOR DE HASHES (MD5 / SHA1) ===")
# Pede para você colar o hash no terminal
hash_usuario = input("Cole o hash aqui e aperte Enter: ").strip().lower()

# Chama a função principal
quebrar_hash(hash_usuario, dicionario_senhas)