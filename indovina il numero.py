import random
dati={}
try:
    print("INDOVINA IL NUMERO")
    print("\nBenvenuto a: INDOVINA IL NUMERO")
    while True:
        nome_giocatore=input("\nInserisci il tuo nome: ")
        nome_prova=""
        for lettera in nome_giocatore:
            if lettera!=" ":
                nome_prova+=lettera
        if nome_prova=="":
            print("Nome non valido.")
        else:
            print("\nBuona fortuna "+nome_giocatore+"!")
            break
    numero_partita=0
    lista_partite=[]
    numero_partita_save=0
    while True:
        print("""\nMENÙ:
 -Modalità normale (1)
 -Modalità invertita (2)
 -Raccolta dati (3)
 -Esci (4)""")
        while True:
            scelta_menù=input("\nInserisci il numero corrispondente all'opzione desiderata: ")
            if scelta_menù=="1":
                numeri_provati=[]
                numeri_validi=[]
                numero_partita+=1
                partita="Partita n."+str(numero_partita)
                lista_partite.append(partita)
                print("\nIn questo semplice gioco bisogna indovinare un numero compreso tra 0 e 100, con un massimo di 10 tentativi.")
                print("Nel caso sbagliassi ti verrà dato un indizio.")
                print("Cerca dunque di trovare la strategia migliore per massimizzare le tue probabilità di vittoria!")
                tentativi=10
                dict_verdetti={10:"Lo ammetto, sei davvero fortunato!",9:"Che fortuna!",8:"Che fortuna!",7:"Che fortuna!",6:"Complimenti!",5:"Beh...il giusto sta nel mezzo!",4:"Bravo!",3:"Per poco...",2:"Per poco...",1:"Per un pelo!"}
                print("\nNUOVA PARTITA")
                numero_computer=random.randint(0,100)
                while True:
                    try:
                        numero_giocatore=input("\nInserisci un numero: ")
                        numero_giocatore=int(numero_giocatore)
                        if numero_giocatore>=0 and numero_giocatore<=100:
                            if numero_giocatore<numero_computer:
                                tentativi-=1
                                if tentativi>0:
                                    print("Il numero selezionato è minore del numero da indovinare.")
                                    if tentativi==1:
                                        print("Ti rimane un tentativo.")
                                    else:
                                        print("Ti rimangono",tentativi,"tentativi.")
                                numeri_provati.append(numero_giocatore)
                            if numero_giocatore>numero_computer:
                                tentativi-=1
                                if tentativi>0:
                                    print("Il numero selezionato è maggiore del numero da indovinare.")
                                    if tentativi==1:
                                        print("Ti rimane un tentativo.")
                                    else:
                                        print("Ti rimangono",tentativi,"tentativi.")
                                numeri_provati.append(numero_giocatore)
                            if numero_giocatore==numero_computer:
                                print("Compilmenti! Hai indovinato!")
                                verdetto_computer=dict_verdetti[tentativi]
                                print("Giudizio del Computer:",verdetto_computer)
                                numeri_provati.append(numero_giocatore)
                                risultato="vittoria"
                                break
                            if tentativi==0 and numero_giocatore!=numero_computer:
                                print("Hai finito i tentativi a tua dipsosizione. Riprova!")
                                risultato="sconfitta"
                                numeri_validi.append(numero_giocatore)
                                break
                            numeri_validi.append(numero_giocatore)
                        else:
                            print("Numero non valido.")
                            numeri_provati.append(numero_giocatore)
                    except ValueError:
                        numero_giocatore=str(numero_giocatore)
                        print("Elemento non valido.")
                if numero_giocatore==numero_computer:
                    tentativi-=1
                    numeri_validi.append(numero_giocatore)
                dati[partita]={}
                dati[partita]["Tipo di partita"]="Modalità normale"
                dati[partita]["Nome del giocatore"]=nome_giocatore
                dati[partita]["Numero da indovinare"]=numero_computer
                dati[partita]["Tentativi usati"]=10-tentativi
                dati[partita]["Numeri provati"]=numeri_provati
                dati[partita]["Numeri validi provati"]=numeri_validi
                dati[partita]["Risultato"]=risultato
                if risultato=="vittoria":
                    dati[partita]["Giudizio del Computer"]=verdetto_computer
                dati[partita]["informazioni"]=""
                break
            if scelta_menù=="2":
                numero_partita+=1
                partita="Partita n."+str(numero_partita)
                lista_partite.append(partita)
                numero_basso=0
                numero_alto=100
                tentativi=10
                numeri_provati=[]
                print("\nIn questa versione di Indovina il Numero dovrai scegliere un numero compreso tra 0 e 100 e farlo idovinare al Computer.")
                print("\nNUOVA PARTITA")
                while True:
                    try:
                        numero_giocatore=int(input("\nInserisci un numero: "))
                        if numero_giocatore>=0 and numero_giocatore<=100:
                            while True:
                                numero_computer=random.randint(numero_basso,numero_alto)
                                numeri_provati.append(numero_computer)
                                print("\nIl Computer ha scelto:",numero_computer)
                                while True:
                                    print("\n-Il numero selezionato è minore del numero da indovinare. (1)")
                                    print("-Il numero selezionato è maggiore del numero da indovinare. (2)")
                                    print("-Il numero selezionato è uguale del numero da indovinare. (3)")
                                    relazione_num=input("\nInserisci il numero corrispondente all'opzione corretta: ")
                                    if relazione_num=="1":
                                        if numero_computer<numero_giocatore:
                                            numero_basso=numero_computer+1
                                            tentativi-=1
                                            if tentativi==1:
                                                print("Al Computer rimane un tentativo.")
                                            if tentativi>1:
                                                print("Al Computer rimangono",tentativi,"tentativi.")
                                            break
                                        else:
                                            numeri_provati.remove(numero_computer)
                                            print("L'operazione selezionata non è corretta.")
                                            print("\nScelta del Computer:",numero_computer)
                                    if relazione_num=="2":
                                        if numero_computer>numero_giocatore:
                                            numero_alto=numero_computer-1
                                            tentativi-=1
                                            if tentativi==1:
                                                print("Al Computer rimane un tentativo.")
                                            if tentativi>1:
                                                print("Al Computer rimangono",tentativi,"tentativi.")
                                            break
                                        else:
                                            print("L'operazione selezionata non è corretta.")
                                            print("\nScelta del Computer:",numero_computer)
                                    if relazione_num=="3":
                                        if numero_computer==numero_giocatore:
                                            tentativi-=1
                                            print("Il computer ha vinto!")
                                            risultato="sconfitta"
                                            while True:
                                                verdetto_giocatore=input("Inserisci il tuo giudizio: ")
                                                verdetto_prova=""
                                                for lettera in verdetto_giocatore:
                                                    if lettera!=" ":
                                                        verdetto_prova+=lettera
                                                if verdetto_prova=="":
                                                    print("Giudizio non valido, riprova.\n")
                                                else:
                                                    break
                                            break
                                        else:
                                            print("L'operazione selezionata non è corretta.")
                                            print("\nScelta del Computer:",numero_computer)
                                    if relazione_num!="1" and relazione_num!="2" and relazione_num!="3":
                                        print("Nessuna operazione trovata per il numero selezionato.")
                                        print("\nScelta del Computer:",numero_computer)
                                if tentativi==0 and numero_computer!=numero_giocatore:
                                    print("Il Computer ha finito i tentativi a sua disposizione.")
                                    risultato="vittoria"
                                    break
                                if numero_computer==numero_giocatore:
                                    break
                            break
                        else:
                            print("Numero non valido.")
                    except ValueError:
                        print("Elemento non valido.")
                dati[partita]={}
                dati[partita]["Tipo di partita"]="Modalità invertita"
                dati[partita]["Nome del giocatore"]=nome_giocatore
                dati[partita]["Numero da indovinare"]=numero_giocatore
                dati[partita]["Tentativi usati"]=10-tentativi
                dati[partita]["Numeri provati"]=numeri_provati
                dati[partita]["Risultato"]=risultato
                if risultato=="sconfitta":
                    dati[partita]["Giudizio del Giocatore"]=verdetto_giocatore
                dati[partita]["informazioni"]=""
                break
            if scelta_menù=="3":
                while True:
                    if lista_partite==[]:
                        print("\nNon hai ancora giocato nessuna partita.")
                        break
                    else:
                        for partit in lista_partite:
                            print("\n"+partit)
                            if dati[partit]["Tipo di partita"]=="Modalità normale":
                                frase_num_provati="Numeri provati: "
                                for numero in dati[partit]["Numeri provati"]:
                                    frase_num_provati+=str(numero)+", "
                                lista_frase_num_provati=list(frase_num_provati)
                                del lista_frase_num_provati[-1]
                                del lista_frase_num_provati[-1]
                                frase_num_provati=""
                                for i in lista_frase_num_provati:
                                    frase_num_provati+=i
                                frase_num_validi="Numeri validi provati: "
                                for numero in dati[partit]["Numeri validi provati"]:
                                    frase_num_validi+=str(numero)+", "
                                lista_frase_num_validi=list(frase_num_validi)
                                del lista_frase_num_validi[-1]
                                del lista_frase_num_validi[-1]
                                frase_num_validi=""
                                for i in lista_frase_num_validi:
                                    frase_num_validi+=i
                                print("Tipo di partita:",dati[partit]["Tipo di partita"])
                                print("Nome del giocatore:",dati[partit]["Nome del giocatore"])
                                print("Numero da indovinare:",dati[partit]["Numero da indovinare"])
                                print("Tentativi usati:",dati[partit]["Tentativi usati"])
                                print(frase_num_provati)
                                print(frase_num_validi)
                                print("Risultato:",dati[partit]["Risultato"])
                                if dati[partit]["Risultato"]=="vittoria":
                                    print("Giudizio del Computer:",dati[partit]["Giudizio del Computer"])
                            if dati[partit]["Tipo di partita"]=="Modalità invertita":
                                frase_num_provati="Numeri provati: "
                                for numero in dati[partit]["Numeri provati"]:
                                    frase_num_provati+=str(numero)+", "
                                lista_frase_num_provati=list(frase_num_provati)
                                del lista_frase_num_provati[-1]
                                del lista_frase_num_provati[-1]
                                frase_num_provati=""
                                for i in lista_frase_num_provati:
                                    frase_num_provati+=i
                                print("Tipo di partita:",dati[partit]["Tipo di partita"])
                                print("Nome del giocatore:",dati[partit]["Nome del giocatore"])
                                print("Numero da indovinare:",dati[partit]["Numero da indovinare"])
                                print("Tentativi usati:",dati[partit]["Tentativi usati"])
                                print(frase_num_provati)
                                print("Risultato:",dati[partit]["Risultato"])
                                if dati[partit]["Risultato"]=="sconfitta":
                                    print("Giudizio del Giocatore:",dati[partit]["Giudizio del Giocatore"])
                            if dati[partit]["informazioni"]!="":
                                print("Altre informazioni:",dati[partit]["informazioni"])
                        print("\nOPZIONI:")
                        print(" -Aggiungi informazioni a una partita (1)")
                        print(" -Elimina informazioni a una partita (2)")
                        print(" -Indietro (3)")
                        scelta_opzioni=""
                        while True:
                            scelta_opzioni=input("\nInserisci il numero corrispondente all'opzione desiderata: ")
                            if scelta_opzioni=="1":
                                while True:
                                    n_partita=input("\nInserisci il numero della partita a cui vuoi aggiungere informazioni: ")
                                    partita1="Partita n."+str(n_partita)
                                    if partita1 in lista_partite:
                                        while True:
                                            informazioni=input("Inserisci le informazioni che vuoi aggiungere: ")
                                            informazioni_prova=""
                                            for lettera in informazioni:
                                                if lettera!=" ":
                                                    informazioni_prova+=lettera
                                            if informazioni_prova=="":
                                                print("Informazioni non valide.\n")
                                            else:
                                                break
                                        dati[partita1]["informazioni"]=informazioni
                                        break
                                    else:
                                        print("Il numero inserito non è valido.")
                                break
                            if scelta_opzioni=="2":
                                while True:
                                    n_partita=input("\nInserisci il numero della partita a cui vuoi eliminare informazioni: ")
                                    partita1="Partita n."+str(n_partita)
                                    if partita1 in lista_partite:
                                        if dati[partita1]["informazioni"]=="":
                                            print("Questa partita non ha informazioni da poter eliminare.")
                                            input()
                                        else:
                                            dati[partita1]["informazioni"]=""
                                        break
                                    else:
                                        print("Il numero inserito non è valido.")
                                break
                            if scelta_opzioni=="3":
                                break
                            else:
                                print("Nessuna operazione trovata per il numero selezionato.")
                        if scelta_opzioni=="3":
                            break
                break
            if scelta_menù=="4" or scelta_menù=="ESC":
                pass
                break
            else:
                print("Nessuna operazione trovata per il numero selezionato.")
        if scelta_menù=="4" or scelta_menù=="ESC":
            print("\nGIOCO TERMINATO")
            break
except KeyboardInterrupt:
    print("\nGIOCO TERMINATO FORZATAMENTE")
