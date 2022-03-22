# -*- coding: utf-8 -*-
import matplotlib
import math
import random
"""
Spyder Editor
@TODO: Se puede reducir el número de funciones que buscan palabras con X letras:
    https://www.w3schools.com/python/python_functions.asp
    apartado Arbitrary Keyword Arguments, **kwargs
This is a temporary script file.
"""
#counting the letters

##
#función que cuenta la cantidad de letras que hay en una lista de palabras.
#atributos:
    #string es la lista de strings que contiene las palabras
    #letter es la letra que queremos contar
#return:
    #número(int) de veces que aparece una letra en el string
##
def count_letter(string, letter):
    contador = 0
    for word in string:
        contador = contador + word.count(letter)
    return contador

def count_word(string, letter):
    contador = 0
    for char in string:
        if (char.find(letter) != -1):
            contador = contador + 1
    return contador

##
#función que convierte un string en una lista de strings separados por el espacio eliminando el espacio
#atributos:
    #string: string del que queremos obtener las palabras
#return
    #lista con las palabras de 5 letras separadas
#TODO:
    #está diseñado para palabras de 5 letras, quizás se podría parametrizar o ajustar según se quiera
##
def sliceToArray(string):
    wordsArray = []
    for i in range(0 , len(string), 6):
        wordsArray.append(string[i:(i+5)])
    return wordsArray

##
#función que busca palabras con una letra específica
#atributos:
    #string: lista de la que queremos obtener las palabras
    #letra: letra que queremos que contenga la lista objetivo
#return
    #lista con las palabras que incluyan la letra
#TODO:
    #
##
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
##
#función que ordena una lista de listas con las letras más comunes y la cantidad de palabras en las que aparece
#atributos:
    #wordList: lista con palabras en las que se quiere contar aparición de letras
    #letras1: string con el alfabeto para buscar las letras
#return
    #lista las letras y la cantidad de palabras en las que aparece
#TODO:
    #limpiar o clarificar ciertas cosas
##
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

def wordSearch(wordList, string):
    newList = wordList
    for char in string:
        newList = search_word(char, newList)
    return newList

##
#función que busca palabras con una letra en una posición especifica
#atributos:
    #wordList: lista de la que queremos obtener las palabras
    #letra1: letra que queremos que contenga la lista objetivo
    #posicion: posicion del 1 al 5 en la que se encuentra la letra1
#return
    #lista con las palabras que incluyan la letra letra1 en la posición posicion
#TODO:
    #
##  
def wordSearchPosition(wordList, letra1, posicion):
    wordsWithLetter = []
    contador = 0
    if (0>=posicion<5):
        print("Introduzca una posición entre 1 y 5")
        return
    for word in wordList:
        if (word[posicion - 1] == letra1):
            wordsWithLetter.append(word)
            contador = contador + 1
    if contador == 0:
        print("No hay palabras con la letra" + letra1 + "en la posicion", posicion)
        return 0
    return wordsWithLetter

## NO TENGO NI IDEA QUE HACE ESTA FUNCION, CREO QUE LO MISMO QUE HACE ESTO SE PUEDE CONSEGUIR MÁS FACILMENTE CON search_word()
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
##
#función que busca palabras que no contenga una letra
#atributos:
    #wordList: lista de la que queremos obtener las palabras
    #letra1: letra que no queremos que contenga la lista objetivo
#return
    #lista con las palabras que no incluyan la letra
#TODO:
    #
##  
def wordSearchNoLetter(wordList, letra1):
    wordsWithLetter = []
    whateverList = wordList
    for char in letra1:
        for word in whateverList:
            if (word.find(letra1) == -1):
                wordsWithLetter.append(word)
    return wordsWithLetter

##
#función que calcula la probabilidad de que una letra esté en una posición de la palabra
#atributos:
    #wordList: lista de la que queremos obtener las palabras
    #letra1: letra que queremos que contenga la lista objetivo
    #letra2: segunda letra que queremos que contenga la lista objetivo
#return
    #lista con las palabras que incluyan las letras
#TODO:
    #
##  
def letterPosition(wordList, letra1):
    timesLetter = [0.0, 0.0, 0.0, 0.0, 0.0]
    cuentaLetra = count_letter(wordList, letra1)
    for word in wordList:
        for i in range(0, 5):
            if (word[i] == letra1):
                timesLetter[i] = timesLetter[i] + 1
    for i in range(0, len(timesLetter)):
        timesLetter[i] = timesLetter[i]/cuentaLetra
    return timesLetter

##función en desarrollo, calculo de entropía y valor de información de las palabras
def entropyLetter(wordList, letter):
    entropy = 0
    counting = count_word(wordList, letter)
    p = counting/len(wordList)
    if p == 0:
        entropy = entropy;
    else:
        entropy =  p*math.log2(1/p)
    return entropy

def entropyWord(wordList, string):
    entropy = 0
    for char in string:
        entropy = entropy + entropyLetter(wordList, char)
    return entropy

def entropyWordPosition(wordList, string):
    entropy = 0
    timesLetter = [0, 0, 0, 0, 0]
    timesWord = [0, 0, 0, 0, 0]
    for char in string:
        counting = count_word(wordList, char)
        p = counting/len(wordList)
        timesLetter = letterPosition(wordList, char)
        timesWord[string.index(char)] = timesLetter[string.index(char)]*p
    for i in range(0, len(timesLetter)):
        if timesWord[i] == 0:
            entropy = entropy
        else:
            entropy = entropy + timesWord[i]*math.log2(1/timesWord[i])
    return entropy

def entropyAllWord(wordList):
    entropy = 0;
    lista = [["0", 0]]
    for word in wordList:
        entropy = entropyWord(wordList, word)
        lista.append([word, entropy])
    lista.pop(0)
    lista.sort(key = lambda x: x[1], reverse = True)
    return lista
    
def entropyAllWordsPosition(wordList):
    entropy = 0;
    lista = [["0", 0]]
    for word in wordList:
        entropy = entropyWordPosition(wordList, word)
        lista.append([word, entropy])
    lista.pop(0)
    lista.sort(key = lambda x: x[1], reverse = True)
    return lista
## WIP
def compareWords(answer, solution, wordList):
    solutionList = wordList
    for char in answer:
        if (solution.count(char) == 0):
            solutionList = wordSearchNoLetter(solutionList, char)
        elif (solution.count(char) == 1):
            if answer.find(char) == solution.find(char):
                solutionList = wordSearchPosition(solutionList, char, answer.find(char)+1)
            elif answer.find(char) != solution.find(char):
                solutionList = search_word(char, solutionList)
        ##elif (solution.count(char)==2):
            
    return solutionList
            
def playGame(wordList):
   wordIndex = random.randrange(0, len(wordList))
   solutionWord = wordList[wordIndex]
   print("Solucion es ", solutionWord)
   solutionList = wordList
   sortedList = entropyAllWordsPosition(wordList)
   for i in range(0, 5):
       sortedList = entropyAllWordsPosition(solutionList)
       firstWord = sortedList[0][0]
       solutionList = compareWords(firstWord, solutionWord, wordList)
   sortedList = entropyAllWordsPosition(solutionList)
   return sortedList[0][0]
            
#main

# Open files with data
palabras = open("words.txt", "rt", encoding="utf-8")
data = palabras.read()
palabras.close()
alfabeto = open("alphabet.txt", "rt", encoding="utf-8")
letras = alfabeto.read()
alfabeto.close()
# Pass the words in file to an array of words
newWord = sliceToArray(data)
newList = newWord
letrasCorrectas = []
contLetra = 0
a = "1"
b = "2"
while((contLetra != 5) or (a != b)):
    a = input("Introduce una palabra de 5 letras: ")
    a.upper()
    while (len(a)!=5) :
         print("Su palabra no tiene 5 letras")
         a = input("Vuelva a introducir una palabra valida: ")
    while (newList.count(a) == 0):
        a = input("Su palabra no está en las posibles palabras, vuelva a introducir una palabra válida: ")
    b = input("Qué letras están en la palabra? ")
    if (a == b):
        print("HA GANADO EN " + str(contLetra+1) + " intentos")
        break
    newList = wordSearch(newList, b)
    for char in a:
        if b.find(char) == -1:
            newList = wordSearchNoLetter(newList, char)
    for char in b:
        if letrasCorrectas.count(char) == 0:
            c = int(input("En qué posición está " + char + ", si no sabe conteste 0: "))
            if c == 0:
                newList = wordSearchNotPosition(newList, char, a.find(char)+1)
            else:
                letrasCorrectas.append(char)
                newList = wordSearchPosition(newList, char, c)
    newList1 = entropyAllWordsPosition(newList)
    if (len(newList1) > 3):
        print("Su siguiente intento debería ser: " + newList1[0][0] + " " + newList1[1][0] + " " + newList1[2][0])
    else:
        print("Su siguiente intento debería ser: " + newList1[0][0])
    contLetra = contLetra + 1
if contLetra == 5:
    print("HA PERDIDO")