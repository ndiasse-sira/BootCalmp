from random import randint
import random

file=open("mots.txt","r")
mots=file.readlines()
taille_mots=len(mots)



def niveau1():
    """ 
       Objectifs:tire un mot au hasard dans le tableau1
       Méthodes:Boucle pour avec des instructions séquentielles
       Besoins:taille_mots,tab1,m,c
       Connu:
       Entrées:-
       Sorties:mot
       Résutats:-
       Hypotheses: -
      
        
    """
    tab1=[]
    for i in range(taille_mots):
       
        m=random.choice(mots).strip()
        if len(m)<5:
          tab1.append(m)
    c=randint(0,len(tab1))      
    mot=random.choice(tab1)
    print(f"{len(tab1)} mots chargees")
    print("Je vous propose un mot de 2-4 lettres. De quel mot s’agit-il ?")
    return mot


def niveau2():
    """ 
       Objectifs:tire un mot au hasard dans le tableau2
       Méthodes: Boucle pour avec des instructions séquentielles
       Besoins: taille_mots,tab2,m,c
       Connu:-
       Entrées:-
       Sorties:mot
       Résutats:
       Hypotheses: -
      
        
    """
    tab2=[]
    for i in range(taille_mots):
         m=random.choice(mots).strip()
         if len(m)>5 or len(m) <8:
          tab2.append(m)
    c=randint(0,len(tab2))      
    mot=random.choice(tab2)
    print(f"{len(tab2)} mots chargees")
    print("Je vous propose un mot de 5 -7 lettres. De quel mot s’agit-il ?")
    return mot   


def niveau3():
    """ 
       Objectifs:tire un mot au hasard dans le tableau3
       Méthodes:Boucle pour avec des instructions séquentielles
       Besoins:taille_mots,tab3,m,c
       Connu:-
       Entrées:-
       Sorties:mot
       Résutats:-
       Hypotheses: -
      
        
    """
    tab3=[]
    for i in range(taille_mots):
         m=random.choice(mots).strip()
         if len(m)>8 :
          tab3.append(m)
    c=randint(0,len(tab3))      
    mot=random.choice(tab3)
    print(f"{len(tab3)} mots chargees")
    print("Je vous propose un mot de 9 lettres. De quel mot s’agit-il ?")
    return mot   
    


       
        
    

def Play(words):
   """ 
       Objectifs:
       Méthodes:boucle pour et tant que avec des instructions séquentielles et d'entrée sortie
       Besoins:parti,chances,tentatives trouver tab_letters, guess
       Connu:
       Entrées:words
       Sorties:
       Résutats:
       Hypotheses: 
      
        
    """
   parti=1
   chances=6
   tentative=0
   trouver=False
   tab_letters=[]
   guess=''
   print(''+'_ '*len(words)+'\n')
   while chances>0:
       guess=input('Entrer une lettre : ')
       if guess == words :
           trouver=True
       else:
           if guess in tab_letters:
               print(f"Vous avez deja deviner la lettre{guess} \n")
               continue
           print('	',end='')
           a_deviner=False
           for letter in words:
               if letter == guess:
                   
                   a_deviner=True
                   print("Bravo, lettre correcte\n")
                   tab_letters.append(letter)
                   print(letter,end=' ')
                   if len(words) == len(tab_letters):
                       trouver=True
               elif letter in tab_letters:
                   print(letter,end=' ')
               else:
                   print('_',end=' ')  
           print()
       if trouver:
           print(f"Bravo, vous avez gagne, le mot etait '{words}'\n")
           print(f"Votre score est de: {(chances-tentative)*len(words)}")  
           with open("log_game.txt", 'a') as f:
                            f.write("Niveau Moyen:\n")
                            print("Vous etes a votre partie n'{}\n".format(parti), file=f)
                            print("Le score est {}\n".format((chances-tentative)*len(words)), file=f)
                            print("Le nombre de tentatives est {}\n".format(chances), file=f) 
                           
                            
           break
       if not a_deviner :
           print(f"{guess} n'est pas la lettre")  
           chances-=1
           tentative+=1
           
           if chances == 5:
                        print ("""
                                                        +++++++
                                                        |     |
                                                        |     O      
                                                        |        
                                                        |
                                                        |
                                                        |
                                                        |
                                                    ___|___""")
           elif chances ==4 :
                        print ("""
                                                        +++++++
                                                        |     |
                                                        |    \\O      
                                                        |        
                                                        |
                                                        |
                                                        |
                                                        |
                                                    ___|___""")

           elif chances == 3:
                        print ("""
                                                        +++++++
                                                        |     |
                                                        |    \\O/      
                                                        |        
                                                        |
                                                        |
                                                        |
                                                        |
                                                    ___|___""")
           elif chances == 2:
                        print ("""
                                                        +++++++
                                                        |     |
                                                        |    \\O/      
                                                        |     |       
                                                        |     |
                                                        |
                                                        |
                                                        |
                                                    ___|___""")
           elif chances == 1:
                        print ("""
                                                        +++++++
                                                        |     |
                                                        |    \\O/      
                                                        |     |       
                                                        |     |
                                                        |    /
                                                        |
                                                        |
                                                    ___|___""")
           elif chances== 0:
                        print ("""
                                                        +++++++
                                                        |     |
                                                        |    \\O/      
                                                        |     |       
                                                        |     |
                                                        |    / \\
                                                        |
                                                        |
                                                    ___|___
                                             """)
           
           print(f'il vous reste {chances} tentatives\n')
           
          
                         
           
   if not trouver:
       print(f"\n Desole vous avez perdu, le mot etait '{words}'\n") 		
       with open("log_game.txt", 'a') as f:
                            f.write("Niveau Moyen:\n")
                            print("Le score est {}\n".format(chances), file=f)
                            print("Le nombre de tentatives est {}\n".format(tentative), file=f) 
                            print("Vous etes a votre partie n'{}\n".format(parti), file=f)           
        
   parti+=1 
          
	




def main():
    
    while True:
        
        print(f">>> Bienvenue dans LET-GET <<< \n\t\t")
        print(f"##########################\nVous avez 6  tentatives")
        print ("""
                                                        +---+
                                                        |   |
                                                            |
                                                            |
                                                            |
                                                            |
                                                    ===========\n""")
        
        niveau=int(input("Choisir un niveau de 1 a 3: "))
        if niveau==1:
            mot=niveau1()
           
            Play(mot)
        elif niveau==2:
            mot=niveau2()
            Play(mot)
        else:
            mot=niveau3()
            Play(mot)    
    
        choice = input("Vous voulez rejouer O/N :")
        if choice in ['no','No','NO','n','N']:
            exit()
			




if __name__ == '__main__':
	main()         