"""
Funções com Parâmetro Padrão (Default Paramters)

-Funções onde a passagem de parâmetro seja opcional

# Exemplo de função onde a passagem do parâmetro seja opcioal;

print('Gabriel Mancini')

print()
-----------------------------------------------------------------
#Exemplo de função onde a passagem de parâmetro seja obrigatória

def quadrado(numero);
return numero ** 2

print(quadrado(3))
print(quadrado()) #Type Error
-----------------------------------------------------------------------

def exponencial(numero=4, potencia=2):
    return numero ** potencia

print(exponencial(2, 3)) # 2 * 2 * 2 = 8
print(exponencial(3, 2)) # 3 * 3 = 9

print(exponencial(3)) #Por padrão eleva ao quadrado
print(exponencial(3, 5)) #Eleva à potencia informada pelo usuário

#OBS
# Se o usuário passar somente 1 argumento, este será atribuido ao parâmetro número, e será calculado o quadrado deste número:
# Se o usuário passar 2 argumentos, o primeiro será atribuído ao parâmetro número e o segundo ao parâmetro potencia. Então
#será calculada esta potência.
print(exponencial())

#OBS: Em funções Python, os parâmetros com valores default (padrão) DEVEM sempre estar no final da declaração.

#ERRO!
def teste(num=2, potencia): | #Correto é (potencia, num=2)
    return num ** potencia

print(teste(6))
---------------------------------------------------------------------------------------------------------------------------------
# Outros exemplos

def soma(num1=5, num2=2):    # Se num1 e num2 não recebessem nenhum valor 2 e 3 receberiam #TypeError
    return num1 + num2

1- print(soma(4, 3))
2- print(soma(4))  #TypeError
3- print(soma())   #TypeError
----------------------------------------------------------------------------------------------------------
# Exemplo mais complexo

def mostra_informacao(nome='Gabriel', instrutor=False):
    if nome == 'Gabriel' and instrutor:
        return 'Bem-Vindo instrutor Gabriel!!'
    elif nome == 'Gabriel':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome})'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Isabella'))
-----------------------------------------------------------------------------
# Por que utilizar parâmetros com valor default?

- Nos permite ser mais flexiveis nas funções;
- Evita erros com parâmetros incorretos;
- Nos permite trabalhar com exemplos mais legíveis de código;
-----------------------------------------------------------------------------
# Quais tipos de dados podmeos utilizar como valors defalt para parâmetros?

- Qualquer tipo de dados: Números, Strings, floats, booleanos, listas, tuplas, dicionários, funções e etc;
---------------------------------------------------------------------------------------------------------------
# Exemplos

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtração(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtração))
----------------------------------------------------------------------------------------------------------------
# Escopo - Evitar problemas e confusões...

# Variáveis globais
# Variáveis locais

instrutor = 'Gabriel'  # Variável Global

def diz_oi():
    instrutor = 'Mancini'
    return f'Oi {instrutor}'

print(diz_oi())

#OBS: Se tivermos uma variável local com o mesmo nome de uma variável globaL, a local terá preferênciaç.
------------------------------------------------------------------------------------------------------------------
def diz_oi():
    prof = 'Geek'   # Variável local
    return f'Olá {prof}'

print(diz_oi())

print(prof)   # NameError

# Atenção com variáveis globais (Se puder evitar, evite!)

total = 0

def incrementa():
    total = total + 1 # UnboundLocalError (A variável local está sendo utilizada para processamento sem ter sido inicializada)
    return total

print(incrementa())
------------------------------------------------------------------------------------------------------------------
# Arrumando o exemplo acima para que fique correto:

total = 0

def incrementa():
    global total  # Avisando que queremos utilizar a variável global
    total = total + 1  # UnboundLocalError (A variável local está sendo utilizada para processamento sem ter sido inicializada)
    return total

print(incrementa())
--------------------------------------------------------------------------------------------------------------------------------
# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de espaço de variável

def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()
print(fora())
print(fora())
print(fora())

print(Dentro()) # Erro
"""










