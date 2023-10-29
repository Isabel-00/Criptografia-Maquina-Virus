from Vigenere import *

import string
import random
import unicodedata


def palabra_a_numeros(palabra):
    palabra = palabra.lower()  # Convierte toda la palabra a minúsculas
    palabra=unicodedata.normalize('NFD', palabra) #Elimina tildes
    numeros = []
    for letra in palabra:
        if 'a' <= letra <= 'z':
            numero = ord(letra) - ord('a')
            numeros.append(numero)
    return numeros

def numeros_a_palabra(numeros):
    palabra = ""
    for numero in numeros:
        if 0 <= numero <= 25:
            letra = chr(ord('a') + numero)
            palabra += letra
    return palabra

def completa_longitud(texto):
    while len(texto)<25:
        texto += random.choice(string.ascii_lowercase)
    return texto    

def entrada_parametros():
    texto = input("Introduce un texto de 25 caracteres (sin contar espacios): ")

    while len(texto.replace(" ", "")) > 25:
        print("Texto inválido. Asegúrate de que el texto tenga 25 caracteres.")
        texto = input("Introduce un texto de 25 caracteres: ")

    clave = input("Introduce una clave de 2, 3 o 6 caracteres (sin contar espacios): ")

    while len(clave.replace(" ", "")) not in (2, 3, 6):
        print("Clave inválida. Asegúrate de que la clave sea de 2, 3 o 6 caracteres.")
        clave = input("Introduce una clave de 2, 3 o 6 caracteres: ")
    
    return texto.replace(" ", ""), clave.replace(" ", "")

def Cifrado_Vigenere(t,c):
    clave_numeros=palabra_a_numeros(c)
    texto_numeros=palabra_a_numeros(completa_longitud(t))
    print(clave_numeros,texto_numeros)
    
    if len(c)==2:
        vm = Vig_Codificacion_25_2(texto_numeros,clave_numeros)
        cifrado = vm.compute()
        cifrado = cifrado[1][29:54]
        vm = Vig_Decodificacion_25_2(cifrado,clave_numeros)
        descifrado = vm.compute()
        descifrado = descifrado[1][29:54]
        
    elif len(c)==3:
        vm = Vig_Codificacion_25_3(texto_numeros,clave_numeros)
        cifrado = vm.compute()
        cifrado = cifrado[1][29:54]
        vm = Vig_Decodificacion_25_3(cifrado,clave_numeros)
        descifrado = vm.compute()
        descifrado = descifrado[1][29:54]
        
    elif len(c)==6:
        vm = Vig_Codificacion_25_6(texto_numeros,clave_numeros)
        cifrado = vm.compute()
        cifrado = cifrado[1][29:54]
        vm = Vig_Decodificacion_25_6(cifrado,clave_numeros)
        descifrado = vm.compute()
        descifrado = descifrado[1][29:54]
    
    
    print("El texto cifrado es",numeros_a_palabra(cifrado))
    print("El texto descifrado es",numeros_a_palabra(descifrado))       