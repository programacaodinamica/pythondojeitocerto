nota = 4.0
media_alta = 7
media_baixa = 5

if nota >= media_alta:
    print("Aprovado direto!😎")
elif nota >= media_baixa:
    print("Fazer prova final!")
    nota_pf = 4.0
    if nota_pf >= media_baixa:
        print("Aprovado na Prova Final")
    else:
        print("Precisa fazer a recuperação final")
        nota_rf = 4.9
        if nota_rf >= media_baixa:
            print("Aprovado na recuperação")
        else:
            print("REPROVADO!")    
else:
    print("Fazer recuperação final 😱")
    nota_rf = 5.0
    if nota_rf >= media_baixa:
        print("Aprovado na recuperação")
    else:
        print("REPROVADO!")