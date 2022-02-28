# -*- coding: utf-8 -*-
import matplotlib
import math
"""
Spyder Editor

This is a temporary script file.
"""
#counting the letters

class WordClass:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2   
    
def count_letter(string, letter):
    contador = 0
    for word in string:
        contador = contador + word.count(letter)
    return contador

def sliceToArray(string):
    wordsArray = []
    for i in range(0 , len(string), 6):
        wordsArray.append(string[i:(i+5)])
    return wordsArray

def search_word(letter, string):
    wordsWithLetter = []
    contador = 0
    for word in string:
        if (word.find(letter) != -1):
            wordsWithLetter.append(word)
    for char in letter:
        for word in wordsWithLetter:
            if(word.find(char) != -1):
                contador = contador + 1
        if (contador == 0):
            print("No hay palabras con ", letter)
            return 0
        contador = 0
    return wordsWithLetter          

def most_letter(wordsList, letras1):
    contador = 0
    #cosa = WordClass("A", 0)
    lista = [['0', 0]]
    for char in letras1:
        for word in wordsList:
            if(word.find(char) != -1):
                contador = contador + 1
        lista.append([char, contador])
        contador = 0
    lista.pop(0)
    lista.sort(key = lambda x: x[1], reverse = True)
    return lista

def wordSearch(lista):
    newList = []
    wordList = []
    for i in range(10):
        newList.append(lista[i][0])
    wordList = search_word(newList[i], newWord)
    for i in newList:
       wordList = search_word(wordList)
       
def wordSearch2(wordsList, letra1, letra2):
    newList =[]
    newList = search_word(letra1, wordsList)
    if newList == 0:
        return 0
    newList = search_word(letra2, newList)
    return newList

def wordSearch3(wordsList, letra1, letra2, letra3):
    newList =[]
    newList1 = []
    newList2 = []
    newList = search_word(letra1, wordsList)
    if newList == 0:
        return 0
    newList1 = search_word(letra2, newList)
    if newList1 == 0:
        print("No hay palabras con ", letra1, letra2)
        return 0
    newList2 = search_word(letra3, newList1)
    if newList2 == 0:
        print("No hay palabras con ", letra1, letra2, letra3)
        return 0
    return newList2

def wordSearch4(wordsList, letra1, letra2, letra3, letra4):
    newList =[]
    newList = search_word(letra1, wordsList)
    newList = search_word(letra2, newList)
    newList = search_word(letra3, newList)
    newList = search_word(letra4, newList)
    return newList

def wordSearchPosition(wordList, letra1, posicion):
    wordsWithLetter = []
    contador = 0
    for word in wordList:
        if (word[posicion - 1] == letra1):
            wordsWithLetter.append(word)
            contador = contador + 1
    if contador == 0:
        print("No hay palabras con la letra" + letra1 + "en la posicion", posicion)
        return 0
    return wordsWithLetter

def wordSearchNotPosition(wordList, letra1, posicion):
    wordsWithLetter = []
    contador = 0
    if posicion < 1:
        print("Error posicion menor a 1")
        return
    for word in wordList:
        if (word[posicion - 1] != letra1):
            wordsWithLetter.append(word)
            contador = contador + 1
    if contador == 0:
        print("No hay palabras con la letra" + letra1 + "en la posicion", posicion)
        return 0
    return wordsWithLetter

def wordSearchNoLetter(wordList, letra1):
    wordsWithLetter = []
    contador = 0
    for word in wordList:
        if (word.find(letra1) == -1):
            wordsWithLetter.append(word)
    for char in letra1:
        for word in wordsWithLetter:
            if(word.find(char) == -1):
                contador = contador + 1
        if (contador == 0):
            print("No hay palabras con ", letra1)
            return 0
        contador = 0
    return wordsWithLetter

def letterPosition(wordList, letra1):
    timesLetter = [0, 0, 0, 0, 0]
    cuentaLetra = count_letter(wordList, letra1)
    for word in wordList:
        for i in range(0, 5):
            if (word[i] == letra1):
                timesLetter[i] = timesLetter[i] + 1
    for i in range(0, len(timesLetter)):
        timesLetter[i] = timesLetter[i]/cuentaLetra
    return timesLetter

def entropyLetter(wordList):
    entropy = 0
    letrasTotales = 5*10836
    for char in letras:
        lettercount = count_letter(wordList, char)
        probability = lettercount / letrasTotales
        if probability==0: probability=1
        entropy = entropy + (probability*math.log2(1/probability))
    return entropy
            
#main
# a = input("Introduce una palabra de 5 letras: ")
# while (len(a)!=5) :
#     print("Su palabra no tiene 5 letras")
#     a = input("Vuelva a introducir una palabra valida: ")
# Open files with data
palabras = open("words.txt", "rt", encoding="utf-8")
data = palabras.read()
palabras.close()
alfabeto = open("alphabet.txt", "rt", encoding="utf-8")
letras = alfabeto.read()
alfabeto.close()
# Pass the words in file to an array of words
newWord = sliceToArray(data)
# Sort letters in number of words they apear
lista = most_letter(newWord, letras)