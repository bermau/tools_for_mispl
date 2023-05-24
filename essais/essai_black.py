import black


code = """
int main() {
    if (condition) {
        printf("Hello, world!");
    } else {
        printf("Goodbye, world!");
    }
    return 0;
}
"""

formatted_code = black.format_str(code, mode=black.FileMode())

print(formatted_code)