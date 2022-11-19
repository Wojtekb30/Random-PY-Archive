from googletrans import Translator
translator = Translator()
while 1==1:
    tempwynik = input("Text to translate to Polish: ")
    print(' ')
    tlumacz = translator.translate(tempwynik, dest='pl')
    tempwynik = tlumacz.text
    print(tempwynik)
    print(' ')
