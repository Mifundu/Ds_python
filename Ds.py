def prog():  
    from colorama import Fore, Style
    def mzil():
        while True:
            global email
            print("-------------Enregistrement-------------\n")
            email=input("Donnez votre email: ")
            import re
            regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+([.-_])+([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+(@centrale.tn)+')
            if re.fullmatch(regex, email) :
                return True
            else:
                print("\n",Fore.RED + "Votre adresse mail est invalide" + Style.RESET_ALL,"\n")      
    def fpass():
        import maskpass
        import string
        re=True
        while re==True:
            """psw=print("Introduire votre pwd ")"""
            psw = maskpass.askpass()
            if (
                any(char in string.punctuation for char in psw) and
                any(char.islower() for char in psw) and
                any(char.isupper() for char in psw) and
                any(char.isdigit() for char in psw) and
                8 == len(psw)
                ):
                print("\n",Fore.GREEN + "Mot de passe validé." + Style.RESET_ALL,"\n")
                re=False
            else:
                print("\n",Fore.RED +"Mot de passe invalide: Assurez-vous qu'il contient au moins un caractère spécial, une minuscule, une majuscule, un chiffre et a une longueur entre 8 et 12 caractères."+ Style.RESET_ALL,"\n")
        return psw
    def save():
        mzil()
        e=fpass()
        with open("Enregistrement.txt",'w') as file:
            file.write(f"Le mot de passe est : {e} et le mail est: {email}")
    def login():
        import maskpass
        print("-------------Authentification-------------\n")
        b=input("Entrez le mail : ")
        u=maskpass.askpass()
        with open("Enregistrement.txt ",'r') as file:
            o= file.readline().strip()
            k=o.split("est :")[1].split()[0]
            l=o.split("et le mail est :")[0].split()[-1]
        if (u  == k) and (b == l):
            def Menu_principale():
                while True:
                    print("\n-------------MENU/Principale-------------\n\nA. jouer à la roulette \n\nB. Décalage par cezar\n")
                    choix=input("\nVeuillez choisir soit A ou B : \n")
                    choix=choix.upper()
                    if choix == 'A':
                        choix1='a'
                        Menu_Roulette()
                        break
                    elif choix == 'B':
                        Menu_Cezar()
                        break
                    else:
                        print("\n", Fore.RED + "Choix invalide. Veuillez choisir A ou B." + Style.RESET_ALL,"\n")
            def Menu_Roulette():
                while True:
                    print("\n-------------MENU/Roulette-------------\n\na. Commencer à jouer  \n\nb. Revenir au menu principale\n")
                    choix=input("\nVeuillez choisir soit a ou b : \n")
                    choix=choix.lower()  
                    if choix=='a':
                        print("Bienvenue dans la Roulette \n")
                        import jeu
                        jeu.roulette()
                        break
                    elif choix=='b':
                        Menu_principale()
                        break
                    else:
                        print("\n", Fore.RED + "Choix invalide. Veuillez choisir a ou b." + Style.RESET_ALL,"\n")
            def Menu_Cezar():
                while True:
                    print("\n-------------MENU/chiffrement-------------\n\na. Donnez un mot à chifrer   \n\nb. Revenir au menu principale\n")
                    choix=input("\nVeuillez choisir soit a ou b : \n")
                    choix=choix.lower()  
                    if choix=='a':
                        Menu_chiffrement()
                        break
                    elif choix=='b':
                        Menu_principale()
                        break
                    else:
                        print("\n", Fore.RED + "Choix invalide. Veuillez choisir a ou b." + Style.RESET_ALL,"\n")
            def Menu_chiffrement():
                while True:
                    print("\n-------------MENU/Cesar-------------\n\n1. Cesar avec code ASCII   \n\n2. Cesar dans les 26 lettres    \n")
                    choix=int(input("\nVeuillez choisir soit 1 ou 2 : \n"))
                    if choix == 1:
                        mot=input("Donnez le mot à chiffrer : ")
                        decalage=int(input("Donnez le décalage : "))
                        Decalage_ascii(mot,decalage)
                        break
                    elif choix==2:
                        mot=input("Donnez le mot à chiffrer : ")
                        decalage=int(input("Donnez le décalage : "))
                        Decalage_26_lettres(mot,decalage)
                        break
                    else:
                        print("\n", Fore.RED + "Choix invalide. Veuillez choisir 1 ou 2." + Style.RESET_ALL,"\n")
            def Decalage_ascii(mot, decalage):
                resultat = ""
                for lettre in mot:
                    if lettre.isalpha():
                        if lettre.islower():
                            resultat += chr((ord(lettre) - ord('a' ) + decalage) % 26 + ord('a'))
                        else:
                            resultat += chr((ord(lettre) - ord('A' ) + decalage) % 26 + ord('A'))
                    else:
                        resultat += lettre
                print(f"\nle chiffrement César avec le decalage ASCII du mot {mot} est : {resultat}\n")
                exit
            def Decalage_26_lettres(mot, decalage):
                alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                mot = mot.upper()
                resultat = ""
                for lettre in mot:
                    if lettre.isalpha() and lettre in alphabet:
                        index = (alphabet.index(lettre) + decalage) % 26
                        resultat += alphabet[index]
                    else:
                        resultat += lettre
                print(f"\nle chiffrement César avec le decalage les 26 lettres du mot {mot} est : {resultat}\n")
                exit
            Menu_principale()
        else :
            print("\n", Fore.RED + "Vous n'êtes pas enregistré, veuillez vous enregistrer svp. "+ Style.RESET_ALL)
            save()
            login()
    save()
    login()


