import markovgen

file_ = open('C:\Users\MarcH_000\Desktop\CIPA.txt')

markov = markovgen.Markov(file_)
print(markov.generate_markov_text())