"""Python module to knwo if a string is palindrome"""

def is_palindrome(string: str) -> bool:
    string = string.replace(" ","").lower()
    return (string == string[::-1])


# mypy palindrome.py --check-untyped-defs  : verifica tipado estático
# .\venv\Scripts\activate
def run():
    print(is_palindrome(1000))


if __name__ == '__main__':
    run()