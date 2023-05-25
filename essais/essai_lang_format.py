import filecmp
import os

import subprocess
import tempfile


# Non utilisé ici
code = '''
#include <stdio.h>

int main() {
  printf("Hello, world!");
      return 0;
}
'''


# test_input = os.path.join(os.path.dirname(__file__), test_input)
# test_output = os.path.join(os.path.dirname(__file__), test_output)


outname = os.path.join("fichier_c_apres_reformat.c")
with open(outname, "w") as out:
    subprocess.run(["clang-format-15", "fichier_a_reformater.c"], stdout=out, check=True)

    # Check that the content is equal
    # assert filecmp.cmp(outname, test_output)