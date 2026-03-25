# programme de gestion de revenu :
revenu = float(input("entrer votre revenu : "))
depenses = 0
while True :
    choix = input("est ce que vous voulez ajouter une nouvelle depenses (oui/non): ")
    if choix == "oui" : 
        montant = float(input("entrer le montant voulez : "))
        depenses += montant 
        # depneses = depenses + montant
    else :
        break
solde = revenu - depenses
print("total des depenses : " , depenses)
print("le solde : " ,solde)

# par cat
revenu = float(input("entrer votre revenu : "))
nourriture = 0
skin_care = 0
habits = 0
depenses = 0
for i in range(3) :
    cat = input("categorie (nourriture/skin_care/habits) : ")
    if cat != "nourriture" and cat != "skin_care" and cat != "habits" :
        print("catégorie n'est pas correcte")
        # break
        continue
    montant = float(input("montant : "))
    if cat == "nourriture" :
        nourriture += montant
    elif cat == "skin_care" :
        skin_care += montant
    elif cat == "habits" :
        habits += montant
total = nourriture + skin_care + habits
solde = revenu - total

print("\n----resultat-----" )
print("nourriture :" ,nourriture)
print("skin_care :" ,skin_care)
print("habits : " ,habits)
print("le total : " ,total )
print("le solde : " ,solde)