#Variáveis de disponibilidade e adições das quantidades de jovens titãs disponíveis

quantidade_candidatos = 0
selecionado = None

robin_disponibilidade = input()
if robin_disponibilidade == 'S':
    quantidade_candidatos += 1

estelar_disponibilidade = input()
if estelar_disponibilidade == 'S':
    quantidade_candidatos += 1

ciborgue_disponibilidade = input()
if ciborgue_disponibilidade =='S':
    quantidade_candidatos += 1

ravena_disponibilidade = input()
if ravena_disponibilidade =='S':
    quantidade_candidatos += 1

mutano_disponibilidade = input() 
if mutano_disponibilidade == 'S':
    quantidade_candidatos += 1

#Outros processos

if quantidade_candidatos == 0:
    print('Parece que ninguém quer participar da Liga da Justiça,'
        ' o Batman vai ter que ouvir um Super-Esculacho do Super-Homem' 
        ' por não ter conseguido ninguém super forte!')

    
elif quantidade_candidatos == 1:
    print('Através de um processo seletivo rigoroso,' 
        ' o mais novo integrante da Liga da Justiça foi escolhido!')
    if (robin_disponibilidade == 'S' and estelar_disponibilidade == 'N' 
    and ciborgue_disponibilidade == 'N' and ravena_disponibilidade  =='N' and  
    mutano_disponibilidade == 'N'):
        print('Finalmente, Batman e Robin lado a lado,' 
              ' agora como iguais na Liga, será que o Menino'
                ' Prodígio se provar digno do cargo?!')
    if (robin_disponibilidade == 'N' and estelar_disponibilidade == 'S' 
    and ciborgue_disponibilidade == 'N' and ravena_disponibilidade  =='N' and  
    mutano_disponibilidade == 'N'):
        print('Com a fúria de Tamaran e o brilho das suas rajadas,' 
              ' a Estelar vai iluminar o caminho da Liga da Justiça!')
        
    
elif 4 >= quantidade_candidatos >= 2:
    print(f'Mesmo com {quantidade_candidatos} candidatos, o(a) {selecionado}' 
        ' foi selecionado(a)! O Superman ficaria impressionado' 
        f' com o novo SUPER membro da Liga! Seja bem-vindo(a) {selecionado}!')
    

elif quantidade_candidatos == 5:
    print('Em toda a vida do Batman, ele nunca viu um lugar' 
          ' tão caótico quanto a torre dos titãns depois da notícia,' 
          ' nem mesmo Gotham, com isso ele percebe que não' 
          ' seria ali o local ideal para encontrar o novo salvador da terra!')

#O amor está no ar
if ((robin_disponibilidade == 'S' and estelar_disponibilidade == 'S' 
    and ciborgue_disponibilidade == 'N' and ravena_disponibilidade  =='N' and  
    mutano_disponibilidade == 'N') or (robin_disponibilidade == 'N' and estelar_disponibilidade == 'N' 
    and ciborgue_disponibilidade == 'N' and ravena_disponibilidade  =='S' and  
    mutano_disponibilidade == 'S')):
    print('Parece que o cavalherismo ainda não morreu não é mesmo?')
    
    if (robin_disponibilidade == 'S' and estelar_disponibilidade == 'S' 
    and ciborgue_disponibilidade == 'N' and ravena_disponibilidade  =='N' and  
    mutano_disponibilidade == 'N'):
        selecionado = 'Estelar'
    elif (robin_disponibilidade == 'N' and estelar_disponibilidade == 'N' 
    and ciborgue_disponibilidade == 'N' and ravena_disponibilidade  =='S' and  
    mutano_disponibilidade == 'S'):
        selecionado = 'Ravena'

#A disputa do tofu
if (robin_disponibilidade == 'N' and estelar_disponibilidade == 'N' 
    and ciborgue_disponibilidade == 'S' and ravena_disponibilidade  =='N' and  
    mutano_disponibilidade == 'S'):
    quantidade_tofu_mutano = int(input('Digite a quantidade de Tofu que Mutano comeu:'))
    quantidade_tofu_ciborgue = int(input('Digite a quantidade de Tofu que Ciborgue comeu:'))
    if  quantidade_tofu_mutano > quantidade_tofu_ciborgue:
        selecionado = 'Mutano'
    elif  quantidade_tofu_mutano < quantidade_tofu_ciborgue:
        selecionado = 'Ciborgue'
    else:
        selecionado = input('Vemos um empate! o selecionado, entre o Mutano e o Ciborgue,'
                            ' foi o:')
        
#A Liderança Inquestionável
if  quantidade_candidatos == 3 or quantidade_candidatos == 4:
    if robin_disponibilidade == 'S':
        selecionado = 'Robin'
    else:
        selecionado = 'Ravena'
        if ravena_disponibilidade == 'N':
            print('O Batman não iria perder a chance de ter' 
                  'um dos seres mais poderosos do Universo DC no time,' 
                  'o preparo dele não permite isso!')

            

#Overdose de Titãs
if quantidade_candidatos == 5:
    selecionado = None


#Qualquer outro caso







