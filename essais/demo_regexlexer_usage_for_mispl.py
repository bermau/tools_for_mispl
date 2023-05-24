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
            # (r"(/\*.*\*\/)", Comment),
            (r'#.*$', Comment),
            # Ajoutez ici les règles de coloration syntaxique pour votre langage personnalisé
            # Exemple : (?i) permet de rendre la regex case-insensitive.
            (r'(?i)(if|then|else|while|for)', Keyword),
            (r'"(.*?)"', String),
            (r'\d+', Number),
            (r'\b(True|False|yes|no)\b', Name.Builtin),
            (r'[a-zA-Z_]\w*', Name),
        ]
    }

# Charger le script à colorer
script = '''
if condition ThEn:
# Ceci est un commentaire
# code   /* Ceci est un autre commentaire  */  hors commentaire
    print("Hello, world!")
Else:
    print("Goodbye, world!")
'''

# Obtenir le lexer pour le langage personnalisé
lexer = MyLanguageLexer()

# Appliquer la coloration syntaxique et obtenir le résultat avec la nouvelle indentation
formatted_script = highlight(script, lexer, TerminalFormatter())

# Afficher le résultat
print(formatted_script)
