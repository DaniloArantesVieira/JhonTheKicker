# Hash

Projeto voltado para estudos de **hashes**, **quebra de hash** e uso de ferramentas auxiliares em segurança ofensiva/defensiva.

## Estrutura

```text
hash/
├─ src/
│  ├─ exemplo_hash.py
│  ├─ hash_breaker.py
│  └─ john_the_kicker.py
├─ README.md
└─ requirements.txt
```

## Objetivo

Este projeto reúne scripts para:
- gerar ou demonstrar hashes;
- testar técnicas de identificação/quebra de hash;
- apoiar estudos práticos de segurança da informação.

## Arquivos

- `exemplo_hash.py`: exemplo introdutório de uso de hashes.
- `HashBreaker.py`: script principal relacionado a tentativa de quebra/validação de hashes.
- `JohnTheKicker.py`: utilitário complementar para testes com hashes, possivelmente integrando ou simulando fluxos parecidos com ferramentas conhecidas.

## Requisitos

- Python 3.10+
- Dependências listadas em `requirements.txt`

## Como instalar

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scriptsctivate   # Windows
pip install -r requirements.txt
```

## Como executar

Exemplos:

```bash
python exemplo_hash.py
python HashBreaker.py
python JohnTheKicker.py
```

## Observações

- Este material deve ser utilizado apenas para **fins educacionais e laboratoriais**.
- Caso o projeto use wordlists, hashes de teste ou arquivos auxiliares, mantenha-os fora de repositórios públicos quando necessário.