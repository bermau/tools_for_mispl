from pygments import highlight
from pygments.lexer import RegexLexer, bygroups
from pygments.token import *
from pygments.formatters import TerminalFormatter

# Definition of the lexer for your custom language
class MyLanguageLexer(RegexLexer):
    name = 'MyLanguage'
    aliases = ['mylang']
    filenames = ['*.mylang']

    tokens = {
        'root': [
            (r'\s+', Text),
            (r'#.*$', Comment),

            # Indentation rule for increasing indentation level
            (r'^(.*:\n)([ \t]*)', bygroups(using(this), Text), 'indent'),
            # Indentation rule for decreasing indentation level
            (r'^([ \t]*)(?=\S)', Text, 'dedent'),
            # Other token rules for syntax highlighting
            (r'(if|else|while|for)', Keyword),
            (r'"(.*?)"', String),
            (r'\d+', Number),
            (r'\b(True|False)\b', Name.Builtin),
            (r'[a-zA-Z_]\w*', Name),
        ],
        'indent': [
            (r'[ \t]+', Text),
            (r'.*\n', Text, '#pop'),
        ],
        'dedent': [
            (r'[ \t]+', Text),
            (r'.*\n', Text, '#pop'),
        ],
    }

# Load the script to be highlighted
script = '''
if condition:
    print("Hello, world!")
    if nested_condition:
      print("Nested statement")
else:
    print("Goodbye, world!")
'''

# Get the lexer for the custom language
lexer = MyLanguageLexer()

# Apply syntax highlighting and obtain the result with the adjusted indentation
formatted_script = highlight(script, lexer, TerminalFormatter())

# Display the result
print(formatted_script)
