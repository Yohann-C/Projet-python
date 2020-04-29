import csv
from csv import reader

 
class Ajouter(): 
    
    def ajouterFiche(self,nom,categorie,dateDeParution,realisateur,acteur,note,commentaire):
        with open('CritiqueFilmBD.csv', 'a') as file:
            writer = csv.writer(file, delimiter = ',')
            writer.writerow([nom,categorie,dateDeParution,realisateur,acteur,note,commentaire])

    
    
 
class LireBD():
    
    def lireFiche(self,numFiche):
        
        with open('CritiqueFilmBD.csv', 'rt', encoding='utf-8') as f:
            csv_reader = reader(f)
            x=0
            for line in csv_reader:
                if not line:
                    continue 
                if x == numFiche:
                    return line
                x+=1
                
                
    def nombreFiche(self):
        
        with open('CritiqueFilmBD.csv', 'rt', encoding='utf-8') as f:
            csv_reader = reader(f)
            x=0
            for line in csv_reader:
                if not line:
                    continue 
                x+=1
            return x

        
 



        


  
    
#Ajouter().ajouterFiche("Sous le sunlight","rigolo",2000,"Gilber Montagne","blibu et bli et blou",5,"GENIAL LE FILM")

#print(LireBD().lireFiche(1),"     ",LireBD().nombreFiche()) 

#print(LireBD().regroupeFiche(1))

#LireBD().regroupeFiche(2)
print(LireBD().nombreFiche())
#d