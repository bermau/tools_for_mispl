# essai de clang proposé par ChatGPT.
import clang.cindex

def format_c_code(code):
    # Créer l'indexeur Clang
    index = clang.cindex.Index.create()

    # Créer un fichier virtuel à partir de la chaîne de code
    virtual_file = "virtual_file.c"
    unsaved_files = [(virtual_file, code)]

    # Définir les options de formatage
    options = clang.cindex.TranslationUnit.PARSE_DETAILED_PROCESSING_RECORD

    # Analyser la chaîne de code en utilisant les options spécifiées
    tu = index.parse(virtual_file, unsaved_files=unsaved_files, options=options)

    # Récupérer les diagnostics (erreurs, avertissements, etc.)
    diagnostics = tu.diagnostics

    # S'il y a des erreurs, les afficher et quitter
    if any(diagnostic.severity >= clang.cindex.Diagnostic.Error for diagnostic in diagnostics):
        for diagnostic in diagnostics:
            if diagnostic.severity >= clang.cindex.Diagnostic.Error:
                print(diagnostic)

        return code  # Renvoyer la chaîne de code non formatée

    # Récupérer la nouvelle version formatée du code
    formatted_code = tu.get_spelling()

    return formatted_code

# Exemple d'utilisation
code = '''
#include <stdio.h>

int main() {
    printf("Hello, world!");
    return 0;
}
'''

formatted_code = format_c_code(code)
print(formatted_code)

# Dans cet exemple, nous utilisons le module clang.cindex du package python-clang pour accéder à la fonctionnalité de
# formatage fournie par Clang. La fonction format_c_code prend une chaîne de code C en entrée, la parse à l'aide de
# l'indexeur Clang, puis retourne la version formatée du code à l'aide de la méthode get_spelling().
#
# Assurez-vous d'installer le package python-clang avant d'exécuter cet exemple. Vous pouvez l'installer en utilisant
# pip install python-clang.
