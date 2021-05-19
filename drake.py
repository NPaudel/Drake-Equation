import random
import csv



for i in range (0,10): #change the number of loops

    # values of all variable used here are subject to debate, numbers here are for indication only

    star = random.uniform(1,3) #number of stars that form in galaxy per year
    fraction_star=random.uniform(0.2,0.5)#fraction of stars that have planets
    habitable=0.2 #fraction of stars that are habitable
    life=random.uniform(0.5,1) #fraction of habitable planets that develop life 
    life_intelligent=random.uniform(0.5,1)#fraction of planets with life that develop intelligent life
    communication=random.uniform(0.1,0.2)#fraction of civillizations that can release detectable signals in space
    commspan=random.randint(100,1000)#the length of time they release signals in solar years
    

    result=star*fraction_star*habitable*life*life_intelligent*communication*commspan
    
    #[result]=[star,fraction_star,habitable,life,life_intelligent,communication,commspan,result]
    #remove the previous line from comment to export all the variables used.

 

    with open('drake.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([result])
