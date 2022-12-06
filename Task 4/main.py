# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# wasExpensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False. 


###    SPRENDIMAS

class Movie:
    def __init__ (self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget
    
    def wasExpensive(self):
        if self.budget > 100000000:
            print("True")
        else:
            print("False")


avatar = Movie("Avatar", "James Cameron", 310000000)

avatar.wasExpensive()

fightClub = Movie("Fight Club", "David Fincher", 65000000)

fightClub.wasExpensive()
