conquista = []
ponto = 0

print("==========================\nCIDADE NATURALIDADE RARA \n==========================\n \n")
print("Bom dia! \nMe chamo José e sou o reporter do jornal da manhã de domingo.\nHoje faremos perguntas sobre oque fazer nas ruas envolvendo a cultura da paz\n")
print("Bom dia dona Sara. Hoje farei algumas perguntas para a senhora")
print("Certo meu querido. Sou sua fã \nObrigado. Conforme a senhora vá acertando ou errando as perguntas havera um sistema de pontuação")

print("================ PRIMEIRA FASE========================")
print ("A senhora está na rua e vê uma idosa com medo de atravessar na sinaleira. A princípio, acha estranho, pois o sinal está vermelho")
escolha = ""

while escolha != "A":
    
    print("\nA) Ajudar e perguntar por que ela esta com medo sendo que esta vermelho \nB) Você decide não se envolver e continua andando. \n")
    escolha = input("\nQual a sua Reação?")

    if escolha == "A":
        print("\n Você ganhou 7 pontos de paz.\n")
        ponto += 7
        
        conquista.append("Empatia")
        print("Sua atitude emana empatia. \n====PARABENZ====\nVocê acaba de ganhar sua primeira conquista\n[EMPATIA]")
        
    elif escolha == "B":
        print("\nVocê perdeu 1 ponto de paz. Às vezes, pequenas atitudes podem fazer grande diferença na vida de alguém.")
        print("\nSua escolha foi errada retorne e faça tudo de novo\n")
    else:
        print("Erro no sistema\n")
        ponto -= 1
print("\n======================SEGUNDA FASE=======================")

alternativa = ""

while alternativa !="A":
    print("\nIndo para casa você encontra uma quantidade relevante de lixo na rua impedindo a passagem de carro na pista. \nOque é mais adequado a se fazer?")
    print("A) Pego todo o lixo com equipamentos ideais para o ocorrido: \nB) Sair sem fazer nada e deixo acontecer um assidente de transito e um engarrafamento generalizado:")
    
    alternativa = input("\n Qual a alternativa certa?")
   
    if alternativa == "A":
        print ("\nVocê ganhou mais 5 pontos PARABÉNS")
        ponto += 5
        conquista.append("Generosidade")
        print("Você esta muito inteligente\n==== MEUS PARABENS ====\nSua segunda conquista foi adicionada\n[GENEROSIDADE]")
       
    elif alternativa == "B":
        print("\nVocê perdeu 3 ponto de paz pois ignorar problemas coletivos pode causar impactos para muitas pessoas.")
        ponto -= 3
       
    else:
        print("\n \nErro no sistema")
print("\n======================TERCEIRA FASE=======================")
questao = ""

print("\nEm uma escola, dois grupos de alunos brigavam e não se respeitavam. Para melhorar a convivência, a escola criou uma semana com conversas e atividades em grupo.\nDurante as atividades, os alunos aprenderam a trabalhar juntos, respeitar as diferenças e resolver os problemas com diálogo. No final, todos entenderam que a paz começa com respeito e cooperação. \n")
while questao != "A":
    print("1° que a escola fez para melhorar a convivência dos alunos? \nA) Criou atividades e conversas em grupo \nB) Cancelou as aulas da turma.")
    questao = input("\nQual alternativa esta correta?")
    
    if questao == "A":
        print("\nQue increvel você é muito inteligente. Mais 8 pontos")
        ponto += 8
        conquista.append("Critico")
        print("Sua resposta esta digna de mais uma conquista\n[CRITICO]")
        
    elif questao == "B":
        print("\nO uso de atividades em coletivo e muito importante, portanto menos 5 pontos")
        ponto -= 5

    else:
        print("\nErro no sistema")
print("\n======================QUARTA FASE=======================")


item = ""
print("Durante uma competição esportiva na escola, um aluno perdeu a partida e ficou muito irritado. Qual atitude demonstra uma cultura de paz?")

while item != "C" and item != "B":
    print("A) Fazer provocações e xingar o colega que venceu a partida.\nB) Sair da quadra sem falar com ninguém após o jogo\nC) Conversar com respeito, ouvir os dois lados e buscar uma solução em conjunto.")
    
    item=input("\nQual ideia esta certa? ") 
    
    if item == "B":
        print("Boa atitude mais 2 pontos")
        ponto += 2
    elif item == "C":
        print("Sua atitude foi linda e ajudou a não alarmar a situação\nVocê merece uma conquista juntamente com mais 7 pontos\n[BRAVURA]")
        ponto += 7
        conquista.append("Bravura")

    else:
        print("Sua atitude não foi digna.\nMenos 15 pontos")
        ponto -= 15

print("\n======================QUINTA FASE=======================")


print(f"Sua pontuação é: {ponto} ")

