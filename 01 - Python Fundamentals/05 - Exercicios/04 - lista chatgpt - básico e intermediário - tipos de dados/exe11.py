# Dado o dicionário anterior, adicione o campo "salário" e remova o campo "cidade".

pessoa = {
    "nome": "Ana", 
    "idade": 28, 
    "profissão": "Médica", 
    "cidade": "São Paulo"
    }

print(pessoa)

pessoa.update({"salário R$": 10000})
pessoa.pop("cidade")

print(pessoa)