	

    import random
    print """Angela Game, Gioco originale di P.G.Perotto per la
    presentazione della Programma 101 negli Stati Uniti d'America"""
    a = 203
    while 30 > a or 100 < a:
            a = input("Inserisci meta tra 30 e 100: ")
    # inserimento meta
    # inizio variabili di lavoro
    z = 0
    m = a+1
    j = 0
    k = 0
    #fine variabili di lavoro
    while z < a:
    #il ciclo finisce quando z e' maggiore di a
            k = input("Inserisci un numero da 1 a 6: ")
            #puntata giocatore
            if 0 < k < 7 and k != j and k != 7-j:
                    #verifica che sia tra 1 e 6, che non sia uguale alla puntata o all'equivalente sulla faccia del dado
                    z = z+k
                    #nuovo totale
                    if z == a:
                            print '\033[1;32mHai vinto\033[1;m'
                    elif z>a:
                            print '\033[1;31mHai perso\033[1;m'
                    else:
                    #se non vinci esegue queste condizioni
                            j = random.randint(1,6)
                            #crea casualmente j
                            if z > a-6:
                                    j = a-z
                            #condizione che, se possibile, fa vincere la macchina
                            if 0 < j < 7 and j != k and k != 7-k:
                            #verifica come nella puntata utente
                                    if z > a-6:
                                            j = a-z
                                    z = j+z
                                    print "puntata macchina:", j
                                    print "totale puntata:", z
                                    if z == a:
                                            print '\033[1;31mHai perso\033[1;m'
                                    elif z > a:
                                            print '\033[1;32mHai vinto\033[1;m'
                            else:
                                    z = z-j #annulla puntata macchina
                                    #print j, "Puntata macchina non valida" #se la puntata macchina non e' valida stampa errore e continua il gioco.
                                    j = 0
                                    #se non e' valido tenta di rigenerare il numero
                                    j = random.randint(1,6)
                                    #crea casualmente j
                                    if z > a-6:
                                            j = a-z
                                    #condizione che, se possibile, fa vincere la macchina
                                    if 0 < j < 7 and j != k and k != 7-k:
                                    #verifica come nella puntata utente
                                            if z > a-6:
                                                    j = a-z
                                            z = j+z
                                            print "puntata macchina:", j
                                            print "totale puntata:", z
                                            if z == a:
                                                    print '\033[1;31mHai perso\033[1;m'
                                            elif z > a:
                                                    print '\033[1;32mHai vinto\033[1;m'
                                            else:
                                                    print "Errore macchina, resetto"
                                                    j = 0
            else:
                     print '\033[1;31mNon Barare\033[1;m' #stringa rossa
    #print "Il punteggio da raggiungere era", a
    #print "Punteggio raggiunto", z
    #print "Ultimo lancio della macchina", j
    #variabili di debug
    print """Simulatore di Angela Game, primo gioco per PC
    creato da Sciking e dal team Angela Game P101
    Versione 0.6.1 in Python, nome in codice "Francesca" """
    #info
    raw_input("Premi INVIO per continuare.")
    import os
    os.system("clear")
    exit()
    #scikingpc.blogspot.it

