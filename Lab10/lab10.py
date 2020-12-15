import io
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# EXERCITIUL 1
stop_words = set(stopwords.words('romanian'))
file1 = open("pg35323.txt")

# Use this to read file content as a stream:
line = file1.read()
words = line.split()
for r in words:
    if not r in stop_words:
        appendFile = open('filteredtext.txt', 'a')
        appendFile.write(" " + r)
        appendFile.close()

# EXERCITIUL 2

dictionary = dict()

fisier = open('filteredtext.txt', 'r')

line = fisier.read()
words = line.split()

for r in words:
    if r in dictionary:
        dictionary[r] += 1
    else:
        dictionary[r] = 1

fisier_aparitii = open('aparitii.txt', 'w')
for key in dictionary.keys():
    dictionary[key] = dictionary[key] / len(dictionary.keys()) * 1000000
    fisier_aparitii.write(str(key) + ": " + str(dictionary[key]) + "\n")

fisier_aparitii.close()

# EXERCITIUL 3

file1 = open("oseminte pierdute.txt")

line = file1.read()
words = line.split()
for r in words:
    if not r in stop_words:
        appendFile = open('filteredtext2.txt', 'a')
        appendFile.write(" " + r)
        appendFile.close()

dictionary2 = dict()

fisier = open('filteredtext2.txt', 'r')

line = fisier.read()
words = line.split()

for r in words:
    if r in dictionary2:
        dictionary2[r] += 1
    else:
        dictionary2[r] = 1

fisier_aparitii2 = open('aparitii2.txt', 'w')
for key in dictionary2.keys():
    dictionary2[key] = dictionary2[key] / len(dictionary2.keys()) * 1000000
    fisier_aparitii2.write(str(key) + ": " + str(dictionary2[key]) + "\n")

fisier_aparitii2.close()

suma = 0
for key2 in dictionary2.keys():
    if key2 in dictionary.keys():
        suma = suma + abs(dictionary2[key2] - dictionary[key2])
    else:
        suma = suma + abs(dictionary2[key2] - 0)

print("SUMA: ", suma, "\n")
print("MEDIA: ", suma / len(dictionary2))
