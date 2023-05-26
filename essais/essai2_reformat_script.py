class MyLang():
    pass


keyw = {'IF': {'suite': 'condition',
               '': None},
        'THEN': {'state': 'new_bloc',
                 'indent': 1,
                 'wait_for': ('ELSE', 'ENDIF')},
        'ELSE': {'wait_for': ('ENDIF'),
                 'indent': -1},
        'ENDIF': {}}

states = {'condition': 'text',
          'bloc': None
          }


def pretraitement(script: str) -> str:
    pass


def reformat_script(script, indent = 0):
    INDENT_SIZE = 4  # Taille de l'indentation en espaces

    lines = script.split('\n')
    formatted_lines = []

    indent_level = indent
    for line in lines:
        line = line.strip()  # Supprimer les espaces en début et fin de ligne
        if line:
            if "ENDIF" in line:
                pos_cut = line.index("ENDIF")
                debut = line[:pos_cut]
                fin = line[pos_cut:]
                line = debut + "\n" + fin
                formatted_lines.append(reformat_script(line, indent_level))

            if 'THEN' in line:
                # Après THEN retour ligne
                pos_cut = line.index("THEN")
                debut = line[:pos_cut + 4]
                fin = line[pos_cut + 4:]
                formatted_lines.append(' ' * (indent_level * INDENT_SIZE) + debut)
                indent_level += 1
                if fin:
                    formatted_lines.append(' ' * (indent_level * INDENT_SIZE) + fin)
            elif 'ENDIF' in line:
                indent_level -= 1
                formatted_lines.append(' ' * (indent_level * INDENT_SIZE) + line)
            else:
                formatted_lines.append(' ' * (indent_level * INDENT_SIZE) + line)

    formatted_script = '\n'.join(formatted_lines)
    return formatted_script


script = """
IF .Result.NumericValue() < 10 THEN
IF .Result.Order.Issuer.Ward().Mnemonic = "4506" OR .Result.Order.Issuer.Ward().Mnemonic = "4516" OR .Result.Order.Issuer.Ward().Mnemonic = "4536" THEN MESSAGE ("ATTENTION résultat inférieur à 10, si dossier DIALYSE ou AURA, rajouter l'Ag HBS dans GLIMS !!!!");
.CascadeRequest("HBS");ENDIF;
ENDIF;
"""

formatted_script = reformat_script(script)
print(script)
print(formatted_script)
