'''
    Conjunto não é ordenado e nem indexado -> não podem ser referenciados por índice ou chave
    Não aceita itens repetidos
    São estruturas heterogêneos podendo armazenar diferentes tipos
    True e 1 em conjunto é a mesma coisa então mostra apenas um deles -> isso vale pro 0 e False
    Você pode apenas verificar se um item existe ou não no conjunto
    Utiliza-se quando você não deseja ter valores repetidos, como nomes, entre outros
    Operações matemáticas de conjunto são possíveis de se utilizar dentro de conjuntos do Python
'''

conjunto = {"apple", "banana", "cherry"}
print(conjunto)

if "apple" in conjunto: # Verifica se tem ou não
    print(f"A palavra apple está no conjunto.")

for x in conjunto: # Percorreu os itens
    print(x)

# Para fazer a função de adicionar itens
conjunto.add("orange")
print(conjunto)

# Para fazer a remoção de itens
nomes = {"FNB", "Aegis", "Envy", "Titan", "Frosty", "Tinowns"}
print(nomes)
# Remove - caso o item não exista, gerará um erro
nomes.remove("Tinowns")
print(nomes)
# Discard - caso o item não existe, não gerará um erro
nomes.discard("Dynkedo")

# conjunto vazio com inserção do usuário
numeros = set() # aqui cria um conjunto vazio!
for i in range(5):
    num = int(input("Informe um número qualquer: "))
    numeros.add(num)

print(numeros)

# Unindo conjuntos 
unindoConjunto = conjunto.union(nomes)
print(unindoConjunto)

# Intersecção de conjuntos: retorna somente os que são iguais no conjunto
x = {"Yone", "Ahri", "Irelia", "Katarina"}
y = {"Katarina", "Talon", "Cassiopeia"}
z = x.intersection(y)
print(z)

# Diferença entre os conjuntos: todos os itens que estão no x mas não no y
a = x.difference(y)
print(a)

# Set -> transforma itens de uma lista, tupla ou string em conjunto
texto = "banananeira"
conjunto = set(texto)
print(texto)

loud = ["Robs", "Croc", "Tinowns", "Route", "Ceos"]
loudSet = set(loud)
print(loudSet)
