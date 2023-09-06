import pymorphy2

text_morphy = pymorphy2.MorphAnalyzer()
# a = text_morphy.parse( 'стали' )
# print(a)

i = 0
with open('keywords.txt', 'r', encoding= 'UTF-8 ')as file:
    for line in file:
        line = line.strip().split('\t')
        word = line[0]
        morph_analyze = text_morphy.parse(word)
        print(word,morph_analyze[0].normal_form)
        if i > 5:
            break
        i += 1