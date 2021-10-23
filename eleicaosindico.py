#fazer um programa que leia os votos de moradores de um prédio e valide eles, como regra, podendo cada morador, votar só uma vez.
from time import sleep#trazer a função sleep de time

def cont1(a, d):#função para gerar a versão em procentagem de a
    a = a / d
    a = a * 100
    return a

def cont2(b, d):#função para gerar a versão em porcentagem de b
    b = b / d
    b = b * 100
    return b

def cont3(c, d):#função para gerar a versão em porcentagem de c
    c = c / d
    c = c * 100
    return c

def cont4(e, d):#função para gerar a versão em porcentagem de e
    e = e / d
    e = e * 100
    return e

a = 0#declarar a
b = 0#declarar b
c = 0#declarar c
d = 0#declarar d
e = 0#declarar e

print("*" + "="*75 + "*")#menu das eleições com prints
print("                              URNA ELETRÔNICA")
print("*" + "="*75 + "*\n")
sleep(1)#função sleep para parar o programa por 2 segundos
print("*"+ "="*22 + "ELEIÇÃO PARA SÍNDICO DO PRÉDIO"+ "="*23 +"*\n")
sleep(1)#função sleep para parar o programa por 2 segundos
print("*" + "="*8 + "E OS CANDIDATOS, COM SEUS RESPECTIVOS NÚMEROS AO LADO, SÃO" + "=" * 9 + "*\n")
sleep(1)#função sleep para parar o programa por 2 segundos

nome_moradores = ["A",
                  "B",
                  "C",
                  "D",
                  "E",
                  "F"
                  ]#lista de nomes para armazenar os nomes das pessoas

codigo_moradores = [1, 2, 3, 4, 5, 6]#lista de números para armazenar os códigos de validação

while d != 6:#condição de repetição que manterá o programa rodando até todos terem votado
    print("\n\nCANDIDATO: JOÃO BAPTISTA CORRÊA [56]")#print do nome do candidato
    sleep(2)#função sleep para parar o programa por 2 segundos
    print("CANDIDATO: LUCAS VINÍCIUS DE ABREU [65]")#print do nome do candidato
    sleep(2)#função sleep para parar o programa por 2 segundos
    print("CANDIDATO: CARLOS VOLTOR MELO[48]\n")#print do nome do candidato
    sleep(2)#função sleep para parar o programa por 2 segundos
    nome = str(input("DIGITE SEU NOME COMPLETO, POR FAVOR: ")).strip().upper()#nome da pessoa que está acessando
    codigo = int(input("DIGITE O SEU CÓDIGO: "))#codigo de verificação, para se ter certeza que é realmente a pessoa
    sleep(2)#função sleep para parar o programa por 2 segundos

    pos1 = -1#declaração de uma posição inicial
    for h in range(len(nome_moradores)):#criação da condição de repetição para percorrer a lista de nomes
        if nome_moradores[h] == nome:#busca na lista de nomes para ver se existe esse valor dentro da lista
            pos1 = h#novo valor de posição

    pos2 = -1#declaração de uma posição inicial
    for i in range(len(nome_moradores)):#condição de repetição para percorrer a listra de números
        if codigo_moradores[i] == codigo:#busca na lista de códigos de validação para saber se aquele código é válido
            pos2 = i#novo valor de posição

    if nome == nome_moradores[pos1] and codigo == codigo_moradores[pos2] and pos1 == pos2:#condições para validação do voto da pessoa
        print(f"\nOLÁ, VOCÊ É {nome} E PODE VOTAR!")#condições para voto foram validadas!
        sleep(1)#função sleep para parar o programa por 1 segundo
        print("DIGITE O NÚMERO DO CANDIDATO DO SEU INTERESSE.")#informativo de instrução para voto
        sleep(1)#função sleep para parar o programa por 1 segundo
        x = int(input("CASO NÃO SE INTERESSE POR NENHUM DOS 3, DIGITE UM NÚMERO ALEATÓRIO: "))#local de continuação da instrução e para voto no número do candidato

        del nome_moradores[pos1]#deleta o nome, pois, ele já votou

        del codigo_moradores[pos2]#deleta o código, pois ele já foi validado

        if x == 56:#condição para soma do voto no candidato um
            a = a + 1#candidato um teve voto somado
            d = d + 1#soma de quantos votaram
            sleep(1)#função sleep para parar o programa por 1 segundo
            print(f"TENHA UM BOM DIA, {nome}!")#mensagem de bom dia
            sleep(2)#função sleep para parar o programa por 2 segundos
        elif x == 65:#condição para soma do voto no candidato dois
            b = b + 1#candidato dois teve voto somado
            d = d + 1#soma de quantos votaram
            sleep(1)#função sleep para parar o programa por 1 segundo
            print(f"TENHA UM BOM DIA, {nome}!")#mensagem de bom dia
            sleep(2)#função sleep para parar o programa por 2 segundos
        elif x == 48:#condição para soma do voto no candidato três
            c = c + 1#candidato três teve voto somado
            d = d + 1#soma de quantos votaram
            sleep(1)#função sleep para parar o programa por 1 segundo
            print(f"TENHA UM BOM DIA, {nome}!")#mensagem de bom dia
            sleep(2)#função sleep para parar o programa por 2 segundos
        else:#condição para soma do voto nos anulados
            e = e + 1#anulação de voto teve voto somado
            d = d + 1#soma de quantos votaram
            sleep(1)#função sleep para parar o programa por 1 segundo
            print("ENTENDEMOS SEU VOTO!")
            sleep(1)#função sleep para parar o programa por 1 segundo
            print(f"TENHA UM BOM DIA, {nome}!")#mensagem de bom dia
            sleep(2)#função sleep para parar o programa por 2 segundos
    elif nome != nome_moradores[pos1] or codigo != codigo_moradores[pos2] or pos1 != pos2:#condiçõess para exibir mensagem de erro
        print("VOCÊ DIGITOU ALGUM VALOR ERRADO!")#informando sobre um erro
        sleep(1)#função sleep para parar o programa por 1 segundo
        print("DIGITE NOVAMENTE!")#intruções para quem errar
        sleep(1)#função sleep para parar o programa por 1 segundo

print("ANALISANDO O TOTAL DAS ELEIÇÕES...")#apenas para enfeite
sleep(3)#função sleep para parar o programa por 3 segundos

a = cont1(a, d)#chamada da função para o cálculo da porcentagem de a
b = cont2(b, d)#chamada da função para o cálculo da porcentagem de b
c = cont3(c, d)#chamada da função para o cálculo da porcentagem de c
e = cont4(e, d)#chamada da função para o cálculo da porcentagem de d

print("O CANDIDATO JOÃO BAPTISTA CORRÊA RECEBEU {:.2f}% DOS VOTOS!".format(a))#informando a porcentagem de a
sleep(2)#função sleep para parar o programa por 2 segundos
print("O CANDIDATO LUCAS VINÍCIUS DE ABREU RECEBEU {:.2f}% DOS VOTOS!".format(b))#informando a porcentagem de b
sleep(2)#função sleep para parar o programa por 2 segundos
print("O CANDIDATO CARLOS VOLTOR MELO RECEBEU {:.2f}% DOS VOTOS!".format(c))#informando a porcentagem de c
sleep(2)#função sleep para parar o programa por 2 segundos
print("OS VOTOS ANULADOS REPRESENTAM {:.2f}% DOS VOTOS!".format(e))#informando a porcentagem de e
sleep(2)#função sleep para parar o programa por 2 segundos
if a > b and a > e and a > c:#condição que gerou resultado válido
    print("O CANDIDATO VENCEDOR É O JOÃO BAPTISTA!")#informando que o processo seguiu as condições e gerou um resultado válido
elif b > a and b > e and b > c:#condição que gerou resultado válido
    print("O CANDIDATO VENCEDOR É O LUCAS VINÍCIUS!")#informando que o processo seguiu as condições e gerou um resultado válido
elif c > a and c > b and c > e:#condição que gerou resultado válido
    print("O CANDIDATO VENCEDOR É O CARLOS VOLTOR!")#informando que o processo seguiu as condições e gerou um resultado válido
elif a > b and a == e and a > c:#condição que gerou resultado válido
    print("O CANDIDATO VENCEDOR É O JOÃO BAPTISTA!")#informando que o processo seguiu as condições e gerou um resultado válido
elif b > a and b == e and b > c:#condição que gerou resultado válido
    print("O CANDIDATO VENCEDOR É O LUCAS VINÍCIUS!")#informando que o processo seguiu as condições e gerou um resultado válido
elif c > a and c > b and c == e:#condição que gerou resultado válido
    print("O CANDIDATO VENCEDOR É O CARLOS VOLTOR!")#informando que o processo seguiu as condições e gerou um resultado válido
elif (a == b and b == c and a == c) or (a == b and c < b) or (c == b and c > a) or (a == c and c > b) or (e > a and e > b and e > c):#condições que gerariam incronguência
    print("O PROCESSO DE VOTAÇÃO SE TORNOU INVÁLIDO PELOS RESULTADOS GERADOS!")#informando que ocorreu uma incroguência na votação