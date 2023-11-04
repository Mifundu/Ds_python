def roulette():  
    import random
    sortir = 's'
    while sortir == 's':
        while True:
            try:
                G = float(input("\nDe combien disposez vous: "))
                if G <= 0:
                    print("Erreur de saisie, veuiller saisir des valeurs strictements positives ")
                    continue
                print(f"\nvotre solde est initialise a {G:.3f}$")
                break
            except ValueError:
                print("\nmauvaise saisie, vous n'avez pas entrer un nombre!!!")
        Continue = 'C'
        while Continue == 'C':
            x = random.randrange(1000)
            while True:
                try:
                    m = float(input("\nveuiller saisir votre mise pour ce tour: "))
                    if m > G:
                        print("vous ne disposez pas de ce montant!!!")
                    elif m <= 0:
                        print(f"erreur votre mise doit etre comprise entre 0.100 euro et {G} euro")
                    else:
                        print(f"Votre mise est initialise a {m:.3f}$")
                        break
                except ValueError:
                    print("Erreur veuiller reprendre avec des numeros s'il vous plait!!! ")
            G = G - m 
            while True:
                try:
                    y = int(input("\nchoisiser un numero compris entre 0 et 999 sur lequel sera placer votre mise: "))
                    if y < 0 and y > 999:
                        print("erreur votre numero n'est pas compris entre 0 et 999")
                    else:
                        print(f"le numero sur lequel votre mise sera placer est {y} ")
                        break
                except ValueError:
                    print("mauvaise saisie veuiller saisir un chiffre")
            print(f"\nle numero gagnant est {x}")
            if x == y:
                print("felicition vous avez fait le bon choix") 
                G = G + ( m * 3 )
            elif x % 2 == 0:
                if y % 2 == 0:
                    print("felicitation vous n'avez pas trouver le bon numero mais vous avez trouver une bonne couleur de case (le rouge)")
                    G = G + m + ( m * 0.5 )
                else:
                    print("vous avez perdu ce tour!!!")
                    m = 0
                if y % 2 != 0:
                    print("felicitation vous n'avez pas trouver le bon numero mais vous avez trouver une bonne couleur de case (le noir)")
                    G = G + m + ( m * 0.5 )
                else:
                    print("vous avez perdu ce tour!!!")
                    m = 0
            if G == 0:
                print(f"\nla partie est termine et vous avez perdu car votre solde est egal a {G} euro")
                break
            else:
                print(f"\n la valeur de votre solde est actuellement {G:.2f} euro")
            Continue = str(input("Voulez vous continuer avec un nouveau tour?(si oui entrer(C) sinon entrer une lettre differente de (C)): "))
        sortir = str(input("si vous voulez relancer une nouvelle partie entrer(s) sinon entrer une valeur differente pour sortir :"))
    print("\n vous avez quitte la partie, merci de votre participation ")    