'''
Luke, I Am Your ...
Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke.

Person	Relation
Darth Vader	father
Leia	sister
Han	brother in law
R2D2	droid
Examples
relation_to_luke("Darth Vader") ➞ "Luke, I am your father."

relation_to_luke("Leia") ➞ "Luke, I am your sister."

relation_to_luke("Han") ➞ "Luke, I am your brother in law."
Notes
N/A
'''
relatives_dict = {'Darth Vader': "Luke, I am your father.",
                 'Leia': "Luke, I am your sister."}

def relation_to_luke(relative):
    if relatives_dict[relative]:
        print(f'{relatives_dict[relative]}')
    else:
        print(f'{relative} Não é parente')

relation_to_luke('Darth Vader'.upper())