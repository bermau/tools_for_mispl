def reformat_script(script):
    INDENT_SIZE = 4  # Taille de l'indentation en espaces

    lines = script.split('\n')
    formatted_lines = []

    indent_level = 0
    for line in lines:
        line = line.strip()  # Supprimer les espaces en début et fin de ligne
        if line:
            if line.endswith('THEN'):
                formatted_lines.append(' ' * (indent_level * INDENT_SIZE) + line)
                indent_level += 1
            elif line.endswith(';'):
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

