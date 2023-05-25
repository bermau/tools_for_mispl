from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

# Dans ce code, nous générons une chaîne de caractères html_content qui contient le code HTML du fichier de sortie.
# La partie importante est l'inclusion des styles CSS générés par formatter.get_style_defs('.highlight') dans la
# balise <style> de l'en-tête HTML.
#
# Ensuite, nous écrivons le contenu HTML dans un fichier nommé sortie.html en utilisant open() et write().


code = '''
# Votre script Python ici
def hello_world():
    print("Hello, World!")

hello_world()
'''

lexer = PythonLexer()
formatter = HtmlFormatter()

highlighted_code = highlight(code, lexer, formatter)

# Générer le code HTML avec les styles CSS inclus
html_content = f'''
<html>
<head>
    <style>
        {formatter.get_style_defs('.highlight')}
    </style>
</head>
<body>
    {highlighted_code}
</body>
</html>
'''

# Enregistrer le contenu HTML dans un fichier
with open('../sortie_v3.html', 'w') as file:
    file.write(html_content)

