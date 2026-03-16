nome_maq1 = input()
qtdpeças_maq1 = int(input())
reacaocandace_maq1 = input()

nome_maq2 = input()
qtdpeças_maq2 = int(input())
reacaocandace_maq2 = input()

nome_maq3 = input()
qtdpeças_maq3 = int(input())
reacaocandace_maq3 = input()

nome_maq4 = input()
qtdpeças_maq4 = int(input())
reacaocandace_maq4 = input()

pontuacaofinalmaq1 = 0
pontuacaofinalmaq2 = 0
pontuacaofinalmaq3 = 0
pontuacaofinalmaq4 = 0




#Pontuação da máquina 1 
pontuacao_maq1 = len(nome_maq1) + qtdpeças_maq1


if nome_maq1 == 'MáquinaDeBanhoForçado':
    pontuacao_maq1 += -20
    
if ('i' in nome_maq1.lower() and 'n' in nome_maq1.lower() and 'a' in nome_maq1.lower() 
    and 't' in nome_maq1.lower() and 'o' in nome_maq1.lower() and 'r' in nome_maq1.lower()):
    pontuacao_maq1 += -50

if ('p' in nome_maq1.lower() and 'e' in nome_maq1.lower()
    and 'r' in nome_maq1.lower() and 'y' in nome_maq1.lower() ):
    pontuacao_maq1 += 20

if reacaocandace_maq1 == 'MÃE! O PHINEAS E O FERB ESTÃO CONSTRUINDO UMA MÁQUINA GIGANTE!':
    pontuacao_maq1 += 30

elif reacaocandace_maq1 == 'EU SABIA QUE ELES ESTAVAM APRONTANDO ALGUMA COISA!':
    pontuacao_maq1 += 20

elif reacaocandace_maq1 == 'OK... ISSO É BEM ESTRANHO.':
    pontuacao_maq1 += 10

elif reacaocandace_maq1 == 'AH, NEM É TÃO IMPRESSIONANTE ASSIM.':
    pontuacao_maq1 += -5

elif reacaocandace_maq1 == 'MÃE! A MÁQUINA SUMIU DE NOVO!':
    pontuacao_maq1 += -10

elif reacaocandace_maq1 == 'AH, ESQUECE…':
    pontuacao_maq1 += -15

if nome_maq1 == 'HidromassagemAutomáticaDoPerry':
    pontuacao_maq1 *= 2





#Pontuação da máquina 2 
pontuacao_maq2 = len(nome_maq2) + qtdpeças_maq2

if nome_maq2 == 'MáquinaDeBanhoForçado':
    pontuacao_maq2 += -20
    
if ('i' in nome_maq2.lower() and 'n' in nome_maq2.lower() and 'a' in nome_maq2.lower() 
    and 't' in nome_maq2.lower() and 'o' in nome_maq2.lower() and 'r' in nome_maq2.lower()):
    pontuacao_maq2 += -50

if ('p' in nome_maq2.lower() and 'e' in nome_maq2.lower()
    and 'r' in nome_maq2.lower() and 'y' in nome_maq2.lower() ):
    pontuacao_maq2 += 20

if reacaocandace_maq2 == 'MÃE! O PHINEAS E O FERB ESTÃO CONSTRUINDO UMA MÁQUINA GIGANTE!':
    pontuacao_maq2 += 30

elif reacaocandace_maq2 == 'EU SABIA QUE ELES ESTAVAM APRONTANDO ALGUMA COISA!':
    pontuacao_maq2 += 20

elif reacaocandace_maq2 == 'OK... ISSO É BEM ESTRANHO.':
    pontuacao_maq2 += 10

elif reacaocandace_maq2 == 'AH, NEM É TÃO IMPRESSIONANTE ASSIM.':
    pontuacao_maq2 += -5

elif reacaocandace_maq2 == 'MÃE! A MÁQUINA SUMIU DE NOVO!':
    pontuacao_maq2 += -10

elif reacaocandace_maq2 == 'AH, ESQUECE…':
    pontuacao_maq2 += -15

if nome_maq2 == 'HidromassagemAutomáticaDoPerry':
    pontuacao_maq2 *= 2




#Pontuação da máquina 3 
pontuacao_maq3 = len(nome_maq3) + qtdpeças_maq3

if nome_maq3 == 'MáquinaDeBanhoForçado':
    pontuacao_maq3 += -20
    
if ('i' in nome_maq3.lower() and 'n' in nome_maq3.lower() and 'a' in nome_maq3.lower() 
    and 't' in nome_maq3.lower() and 'o' in nome_maq3.lower() and 'r' in nome_maq3.lower()):
    pontuacao_maq3 += -50

if ('p' in nome_maq3.lower() and 'e' in nome_maq3.lower()
    and 'r' in nome_maq3.lower() and 'y' in nome_maq3.lower() ):
    pontuacao_maq3 += 20

if reacaocandace_maq3 == 'MÃE! O PHINEAS E O FERB ESTÃO CONSTRUINDO UMA MÁQUINA GIGANTE!':
    pontuacao_maq3 += 30

elif reacaocandace_maq3 == 'EU SABIA QUE ELES ESTAVAM APRONTANDO ALGUMA COISA!':
    pontuacao_maq3 += 20

elif reacaocandace_maq3 == 'OK... ISSO É BEM ESTRANHO.':
    pontuacao_maq3 += 10

elif reacaocandace_maq3 == 'AH, NEM É TÃO IMPRESSIONANTE ASSIM.':
    pontuacao_maq3 += -5

elif reacaocandace_maq3 == 'MÃE! A MÁQUINA SUMIU DE NOVO!':
    pontuacao_maq3 += -10

elif reacaocandace_maq3 == 'AH, ESQUECE…':
    pontuacao_maq3 += -15

if nome_maq3 == 'HidromassagemAutomáticaDoPerry':
    pontuacao_maq3 *= 2



#Pontuação da máquina 4
pontuacao_maq4 = len(nome_maq4) + qtdpeças_maq4

if nome_maq4 == 'MáquinaDeBanhoForçado':
    pontuacao_maq4 += -20
    
if ('i' in nome_maq4.lower() and 'n' in nome_maq4.lower() and 'a' in nome_maq4.lower() 
    and 't' in nome_maq4.lower() and 'o' in nome_maq4.lower() and 'r' in nome_maq4.lower()):
    pontuacao_maq4 += -50

if ('p' in nome_maq4.lower() and 'e' in nome_maq4.lower()
    and 'r' in nome_maq4.lower() and 'y' in nome_maq4.lower() ):
    pontuacao_maq4 += 20

if reacaocandace_maq4 == 'MÃE! O PHINEAS E O FERB ESTÃO CONSTRUINDO UMA MÁQUINA GIGANTE!':
    pontuacao_maq4 += 30

elif reacaocandace_maq4 == 'EU SABIA QUE ELES ESTAVAM APRONTANDO ALGUMA COISA!':
    pontuacao_maq4 += 20

elif reacaocandace_maq4 == 'OK... ISSO É BEM ESTRANHO.':
    pontuacao_maq4 += 10

elif reacaocandace_maq4 == 'AH, NEM É TÃO IMPRESSIONANTE ASSIM.':
    pontuacao_maq4 += -5

elif reacaocandace_maq4 == 'MÃE! A MÁQUINA SUMIU DE NOVO!':
    pontuacao_maq4 += -10

elif reacaocandace_maq4 == 'AH, ESQUECE…':
    pontuacao_maq4 += -15

if nome_maq4 == 'HidromassagemAutomáticaDoPerry':
    pontuacao_maq4 *= 2

pont_posicao1 = pontuacao_maq1
pont_posicao2 = pontuacao_maq2
pont_posicao3 = pontuacao_maq3
pont_posicao4 = pontuacao_maq4

if  pont_posicao1 < pont_posicao2:
    pont_posicao1, pont_posicao2 = pont_posicao2, pont_posicao1
    nome_maq1, nome_maq2 = nome_maq2, nome_maq1


