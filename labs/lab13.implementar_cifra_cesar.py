"""Para continuar a discussão sobre funções definidas pelo usuário, você escreverá um programa que implementa uma cifra de César, que é um método simples de criptografia. A cifra de César pega as letras de uma mensagem e desloca cada uma ao longo do alfabeto um certo número de posições.

Neste laboratório, você vai:

Criar funções definidas pelo usuário
Usar várias funções para implementar um programa de criptografia com a cifra de César

Para entender o que a função faz, use uma amostra de entrada de alphabet="ABC". A string de retorno para essa entrada seria "ABC" + "ABC" = "ABCABC". O sinal de mais (+) concatena as strings em uma string."""


def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet


def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return shiftAmount
    
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage
    
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)
    
"""Antes de ir para o código, planeje a lógica:
Defina uma variável de string para conter o alfabeto inglês.

Para poder deslocar as letras, dobre sua string de alfabeto.

Receba uma mensagem do usuário para criptografar.

Obtenha uma chave de cifra do usuário.

Criptografe a mensagem.

Descriptografar a mensage"""
    
def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')
    
    runCaesarCipherProgram()
    