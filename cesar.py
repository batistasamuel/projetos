############################## Criptografia de Cesar Versão 1 ####################################   

######################## Início da Função para cifrar ou decifrar ################################
def cesar(frase,shift,op):
    abc='abcdefghijklmnopqrstuvwxyz'
    cifra=[]
    for id in frase.lower():
        # Condicional para tratar tudo o que não é letra: pontuação e caracteres especiais
        if id  not in abc:
            posicao=id
            cifra.append(posicao)
        elif op == '0':
            # Operação cifrar
            posicao=((abc.find(id)+shift) %26)
            cifra.append(abc[posicao])
        elif op == '1':
            # Operação decifrar
            posicao=((abc.find(id)-shift) % 26)
            cifra.append(abc[posicao])
        else:
            print('erro na operação')
    print('\nA frase após a operação escolhida é: \n \n' + ''.join(cifra))           
########################################## Fim da Função ##########################################

################ Início da Função para remover, cedilha, travessões etc ###########################
from unicodedata import normalize
def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')
#------------- Fonte desta função: https://wiki.python.org.br/RemovedorDeAcentos -----------------#
########################################## Fim da Função ##########################################

####################################### Início do Programa ########################################
op=input('\nInforme a operação da criptografia de Cesar (0 para cifrar ou 1 para decifrar): \n \n')
shift=int(input('\nInforme o deslocamento da criptografia de Cesar: \n \n'))
#shift=input('\nInforme o deslocamento da criptografia de Cesar: \n \n')
frase=remover_acentos(input('\nDigite a frase a ser cifrada ou decifrada com criptografia de Cesar: \n \n'))
if op == '0' or op == '1' and type(shift) == int and type(frase) == str:
    cesar(frase,shift,op)
else:
    print('A operação deve ser um valor entre zero e um, o deslocamento deve ser um número inteiro e a frase deve ser um texto')
######################################### Fim do Programa ########################################