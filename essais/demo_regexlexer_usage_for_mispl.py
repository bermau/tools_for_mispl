from pygments import highlight
from pygments.lexer import RegexLexer
from pygments.formatters import TerminalFormatter
from pygments.token import *

# Définition du lexer personnalisé directement dans le script principal
class MyLanguageLexer(RegexLexer):
    name = 'MyLanguage'
    aliases = ['mylang']
    filenames = ['*.mylang']

    tokens = {
        'root': [
            (r'\s+', Text),
            (r'(?s)/\*.*?\*/', Comment),
            (r'#.*$', Comment),
            # Ajoutez ici les règles de coloration syntaxique pour votre langage personnalisé
            # Exemple : (?i) permet de rendre la regex case-insensitive.
            (r'(?i)(if|then|else|endif|Do|Done|while|for)', Keyword),
            (r'"(.*?)"', String),
            (r'\d+', Number),
            (r'\b(True|False|yes|no)\b', Name.Builtin),
            (r'[a-zA-Z_]\w*', Name),
        ]
    }

# Charger le script à colorer

script = '''
/*** Ajouter MESSAGE sur Ac. HBST si valeur < 10 ou < 100 et > 1000***/

IF .Result.NumericValue() < 10  THEN
erreur  /* Commentaire */ erreur
IF .Result.Order.Issuer.Ward().Mnemonic = "4506" OR .Result.Order.Issuer.Ward().Mnemonic = "4516" OR .Result.Order.Issuer.Ward().Mnemonic = "4536" 
THEN MESSAGE ("ATTENTION résultat inférieur à 10, si dossier DIALYSE ou AURA, rajouter l'Ag HBS dans GLIMS !!!!");
.CascadeRequest("HBS");ENDIF;

ENDIF;
'''


# Obtenir le lexer pour le langage personnalisé
lexer = MyLanguageLexer()

# Appliquer la coloration syntaxique et obtenir le résultat avec la nouvelle indentation
formatted_script = highlight(script, lexer, TerminalFormatter())

# Afficher le résultat
print(formatted_script)
