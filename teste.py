alfabeto = 'abcdefghijklmnopqrstuvwxyz' #alfabeto completo atualizado
quantos = None # tanto de casas a ser pulados no alfabeto

def codificar(frase):
    m = ''
    for c in frase:
        if c in alfabeto:
            c = alfabeto.index(c) # pesquisando qual a posição da letra no alfabeto
            m += alfabeto[(c + quantos) % len(alfabeto)] # ('fazer o alfabeto ficar em um loop para quando chega no 'z' ele voltar para o 'a')
        else:
            m += c #adicionar um espaço caso a letra da palavra digitada não esteja no alfabeto
    print('Mensagem criptografada = {}'.format(m)) #resposta completa
def descodificar(frase):
    m = '' 
    for c in frase:
        if c in alfabeto: 
            c = alfabeto.index(c) # pesquisando qual a posição da letra no alfabeto
            m += alfabeto[(c - quantos) % len(alfabeto)]# ('fazer o alfabeto ficar em um loop para quando chega no 'z' ele voltar para o 'a')
        else: # caso a letra não esteja no alfabeto
            m += c #adicionar um espaço caso a letra da palavra digitada não esteja no alfabeto
    print('Mensagem descriptografada = {}'.format(m))
print('______________________________________________________')
frase  =  str(input('Escreva uma frase: '))
pergunta1 = int(input('''Você deseija codificar ou descodificar? 
1(codificar) ou 2(descodificar)? '''))
quantos = int(input('Chave: ')) # casas a ser puladas no alfabeto
print('______________________________________________________')

if (pergunta1 == 1):
    codificar(frase)
elif(pergunta1 == 2):
 Chave('>') # casas a ser puladas no alfabeto
