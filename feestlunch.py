print("Wat is de prijs van een croissant?")
CroissantPrijs = float(input())
print("Hoeveel croissants bestelt u?")
AantalCroissant = int(input())
print("Wat is de prijs van een stokbrood?")
StokbroodPrijs = float(input())
print("Hoeveel stokbroken bestelt u?")
AantalStokbrood = int(input())
print("Hoeveel korting krijgt u bij een kortingsbon?")
KortingBon = -abs(float(input()))
print("Hoeveel kortingsbonnen heeft u?")
AantalKortingBon = int(input())
Totaal = 0.0
EindBedrag = (AantalCroissant * CroissantPrijs) + (AantalStokbrood * StokbroodPrijs) + (AantalKortingBon * KortingBon)

print(EindBedrag)

print("De feestlunch kost je bij de bakker "+ str(EindBedrag)+" euro voor de "+ str(AantalCroissant)+" croissantjes en de "+str(AantalStokbrood) +" stokbroden als de "+ str(AantalKortingBon)+ " kortingsbonnen nog geldig zijn!")