#coding:utf-8

'''
VOUS VOULONS MANIPULER LES LISTES ET LES BOUCLE POUR FORMÉS DES FIGURES GÉOMETRIQUE

NB NOUS IRIONT DE FACON SEPARE
-------------------------------------------------------------------------------------
1- un triangle equilatéral
2- un triangle rectangle
3- un rectangle
4- un losange
-------------------------------------------------------------------------------------
'''

# commençons par un triangle equilatéral
'''
 	le tiangle equilatéral à ses trois cotés egals
 	**********************************************
voici un exemple
------------------------
 	 |    *		|
 	 |   * *	|
 	 |  * * *	|
 	 | * * * *	|
------------------------
'''

marge=['* ',' ']

#Je veux obtenir mon triangle sur 10 ligne
#Remarquez que marge[0] contient '*' et un espace ' '

iteration = 0

# definitionn du nombre de ligne 

ligne = 10

print('1 - ----------------------Triangle equilatéral---------------------')

while iteration <= ligne:

	print('{} {}'.format(marge[1] * (ligne - iteration), marge[0] * iteration))

	iteration+=1

'''

2- triangle rectangle
Nous connaissons tous la définition d'un triangle rectangle 
'''
print('2 - ----------------------Triangle rectangle---------------------')

iteration = 0

# definitionn du nombre de ligne 

ligne = 10

while iteration <= ligne:

	print('{}'.format(marge[0] * iteration))

	iteration+=1


print('3 ------------------ Un rectangle---------------------') 

iteration = 0
colonne = 30
ligne= 6
rectangle = ['*']

while iteration <= ligne:

	print('{}'.format(rectangle[0] * colonne))

	iteration+=1


print('4 ------------------ le losange ---------------------') 

iteration = 0

# definitionn du nombre de ligne 

ligne = 10


while iteration <= ligne:

	print('{} {}'.format(marge[1] * (ligne - iteration), marge[0] * iteration))

	if iteration == ligne:
		iteration = 10
		while iteration >= 0:

			print('{} {}'.format(marge[1] * (ligne - iteration), marge[0] * iteration))
			iteration -= 1
		break
	iteration+=1
		