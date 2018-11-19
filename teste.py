alfabeto = 'abcdefghijklmnopqrstuvwxyz'
quantos = None

def codificar(frase):
    m = ''
    for c in frase:
        if c in alfabeto:
            c = alfabeto.index(c)
            m += alfabeto[(c + quantos) % len(alfabeto)]
        else:
            m += c
    print('Mensagem criptografada = {}'.format(m))
def descodificar(frase):
    m = ''
    for c in frase:
        if c in alfabeto:
            c = alfabeto.index(c)
            m += alfabeto[(c - quantos) % len(alfabeto)]
        else:
            m += c
    print('Mensagem descriptografada = {}'.format(m))
print('______________________________________________________')
frase  =  str(input('Escreva uma frase: '))
pergunta1 = int(input('''Você deseija codificar ou descodificar? 
1(codificar) ou 2(descodificar)? '''))
quantos = int(input('Tanto de casas a ser puladas: '))
print('______________________________________________________')

if (pergunta1 == 1):
    codificar(frase)
elif(pergunta1 == 2):
    descodificar(frase)
input('>')
