from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

code = '''
# Votre script Python ici
def hello_world():
    print("Hello, World!")

hello_world()
'''

lexer = PythonLexer()
formatter = HtmlFormatter(linenos=True, cssclass="source")

highlighted_code = highlight(code, lexer, formatter)

# Afficher le code HTML avec coloration syntaxique
print(highlighted_code)

with open("../sortie.html", 'w') as f:
    f.write(highlighted_code)
