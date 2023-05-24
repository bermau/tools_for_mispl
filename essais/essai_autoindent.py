import autopep8

# Incorrectly indented software text
text = '''
#include <stdio.h>

int main() {
printf("Hello, world!");
if (condition) {
    printf("Condition is true");
} else {
    printf("Condition is false");
}
return 0;
}
'''
print("Hello")
# Set the K&R C style configuration
kr_config = autopep8.parse_args(['--indent-size', '4'])
# kr_config = autopep8.parse_args()

# Correct the indentation using K&R C style
corrected_text = autopep8.fix_code(text, options=kr_config)

# Display the corrected text
print(corrected_text)
