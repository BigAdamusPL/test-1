memy = {
    "LOL": "coś śmiesznego",
    "CRINGE": "jakaś wstydliwa sytułacja lub coś dziwnego",
    "ROFL": "odpowiedź na żart",
    "SHEESH": "lekka dezaprobata",
    "CREEPY": "straszny, złowieszczy",
    "AGGRO": "stać się zły szczegulnie na kogoś konkretnego",
}

while True:
    word = input("Wpisz słowo (używaj wielkich liter!): ")
    
    if word in memy:
        print("\n", memy[word], "\n")
    else:
        print("ERROR, źle napiszałeś lub nie ma takiego czegoś! \n spróbój popnownie")
