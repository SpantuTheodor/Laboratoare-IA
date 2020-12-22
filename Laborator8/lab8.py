from gensim.models import Word2Vec
from nltk.corpus import stopwords
from nltk import tokenize

stop_words = set(stopwords.words('romanian'))
file = open("text.txt")
line = file.read()
lista_propozitii = tokenize.sent_tokenize(line)
matrix = []
print(lista_propozitii)

dictionary = dict()
lista_propozitii_impartite = []

for propozitie in lista_propozitii:
    lista_aux = []
    for cuvant in propozitie.split():
        cuvant = cuvant.replace(".", "")
        cuvant = cuvant.lower()

        print(cuvant)
        lista_aux.append(cuvant)
        if cuvant in dictionary:
            dictionary[cuvant] += 1
        else:
            dictionary[cuvant] = 1
    lista_propozitii_impartite.append(lista_aux)

V = len(dictionary)
print(len(dictionary))
i = 0

for cuvant in dictionary.keys():
    vector_cuvant = []
    for _ in range(i):
        vector_cuvant.append(0)
    vector_cuvant.append(1)
    for _ in range(V - i - 1):
        vector_cuvant.append(0)
    matrix.append(vector_cuvant)
    i += 1

print(matrix)

print(dictionary)

model = Word2Vec(lista_propozitii_impartite, min_count=1)
print(model)
print(model.wv.most_similar(positive = ["ion", "humulesti", "limba", "geniu", "a"]))