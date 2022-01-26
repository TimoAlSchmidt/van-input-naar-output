print("Met hoeveel personen bent u?")
Personen = int(input())
print("Hoeveel kost een toegangsticket?")
ToegangsTicketPrijs = float(input())
print("Per hoeveel minuten wordt de GameSeat verhuurt?")
GameSeatMinutenPerPrijs = int(input())
print("Hoeveel kost het om in de GameSeat voor " + str(GameSeatMinutenPerPrijs) + " minuten te zitten?")
GameSeatPrijs = float(input())
print("Hoeveel minuten blijven u in de GameSeat?")
MinutenInGameSeat = int(input())
EindBedrag = round(Personen*(ToegangsTicketPrijs+(GameSeatPrijs*(MinutenInGameSeat/GameSeatMinutenPerPrijs)))*100)/100

print(EindBedrag)

print("Dit geweldige dagje-uit met " + str(Personen) + " mensen in de Speelhal met " + str(MinutenInGameSeat) + " minuten VR kost je maar " + str(EindBedrag) + " euro")