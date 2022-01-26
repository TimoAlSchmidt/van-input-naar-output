# Timo A. Schmidt
# Opdracht: Pizza Calculator

klaar = False
hoeveelheidPerMaat = [0,0,0]
smallPrijs = 11.79
mediumPrijs = 13.79
largePrijs = 16.79
smallTotaal = 0.0
mediumTotaal = 0.0
largeTotaal = 0.0
totaalPrijs = 0.0


while(not klaar): # While loop om ervoor te zorgen dat we niet per ongeluk uit de pizzabestel-menu gaan
    print("Kies uw maat: \n 1) Small (25 cm; €"+str(smallPrijs)+")\n 2) Medium (30 cm; €"+str(mediumPrijs)+")\n 3) Large (35 cm; €"+str(largePrijs)+")")
    maat = 0
    try: # Try zodat er geen errors voorkomen.
        maat = int(input())
        if(maat < 1 or maat > 3): # Zorgt ervoor dat we 1,2,3 krijgen.
            print("Inccorect antwoord. Voer alstublieft 1, 2 of 3 in.")
            continue # Continue brengt ons terug naar prompt 1
    except: 
        print("Incorrect antwoord. Voer alstublieft 1, 2 of 3 in.")
        continue # Continue brengt ons terug naar prompt 1
    
    while(True): # Nog een while loop omdat er misschien een reëel getal i.p.v. een geheel getal worden ingevult worden
        print("Hoeveel pizza's wilt u?")
        try: # Try om ervoor te zorgen dat de gebruiken alleen een geheel getal invult.
            pizzas = int(input())
            if(pizzas < 0): 
                print("Incorrect antwoord, vul alstublief een positief getal in.")
                continue
        except:
            print("Incorrect antwoord, voer alstublieft alleen een geheel getal in.")
            continue
        else:
            hoeveelheidPerMaat[maat-1] = pizzas # Omdat arrays bij 0 beginnen en niet bij 1, moeten we maat-1 doen.
            break # break omdat we uit deze while willen

    while(True): # While true zodat we niet terug naar het begin gaan als de gebruiker een fout maakt
        # Bereken totaalprijzen
        smallTotaal = round(hoeveelheidPerMaat[0]*smallPrijs, 2)
        mediumTotaal = round(hoeveelheidPerMaat[1]*mediumPrijs, 2)
        largeTotaal = round(hoeveelheidPerMaat[2]*largePrijs, 2)
        totaalPrijs = round(smallTotaal+mediumTotaal+largeTotaal, 2)


        print("U heeft nu "+str(hoeveelheidPerMaat[0])+" Small pizza's (€"+str(smallTotaal)+"), "+str(hoeveelheidPerMaat[1])+" Medium pizza's (€"+str(mediumTotaal)+") en "+str(hoeveelheidPerMaat[2])+" Large pizza's (€"+str(largeTotaal)+").")
        print("Dit kost €"+str(totaalPrijs)+".")
        print("Is dit alles (Y/N)?")
        compleet = input()
        if(compleet != "Y" and compleet != "N"): # Zorg ervoor dat we een correct antwoord krijgen
            print("Incorrect antwoord, voer alstublieft Y or N in.")
            continue
        else:
            if(compleet == "Y"):
                klaar = True
                break # Break om uit de while te gaan
            else:
                klaar = False
                break # Break om uit de while te gaan

print("De totale prijs is €"+str(totaalPrijs))
