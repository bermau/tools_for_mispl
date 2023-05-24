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
            (r'#.*$', Comment),
            # Ajoutez ici les règles de coloration syntaxique pour votre langage personnalisé
            # Exemple :
            (r'(if|else|while|for)', Keyword),
            (r'"(.*?)"', String),
            (r'\d+', Number),
            (r'\b(True|False)\b', Name.Builtin),
            (r'[a-zA-Z_]\w*', Name),
        ]
    }

# Charger le script à colorer
script = '''
if condition:
    print("Hello, world!")
else:
    print("Goodbye, world!")
'''

# Obtenir le lexer pour le langage personnalisé
lexer = MyLanguageLexer()

# Appliquer la coloration syntaxique et obtenir le résultat avec la nouvelle indentation
formatted_script = highlight(script, lexer, TerminalFormatter())

# Afficher le résultat
print(formatted_script)
