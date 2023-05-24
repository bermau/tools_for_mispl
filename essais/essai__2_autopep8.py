"""Exemple d'usage de autopep8"""

import autopep8

texte = """
import truc 
 import machin, chose

def ma_Fonction(a):
       return (a *2)
       
 
"""

fixed_code = autopep8.fix_code(texte,
                  # options={'ignore': ['E']}
                               )
# 'print( 123 )\n'
print(fixed_code)