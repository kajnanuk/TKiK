import os
import sys

try:
    from scanner import AnalizatorLeksykalny
except ImportError:
    print("BŁĄD: Nie znaleziono pliku 'scanner.py'!")
    sys.exit(1)

from highlighter import highlight, wrap_html

def main():
    if not os.path.exists("input.txt"):
        print("Brak pliku 'input.txt'. Utwórz go w tym samym folderze.")
        return

    # Wczytujemy plik w całości, bez strip(), żeby zachować układ w 100%
    with open("input.txt", "r", encoding="utf-8") as f:
        wyrazenie = f.read()

    skaner_obj = AnalizatorLeksykalny(wyrazenie)
    tokens = []

    # Skaner działa samodzielnie i wywołujemy go wielokrotnie
    while True:
        try:
            token = skaner_obj.skaner()
            tokens.append(token)
            if token.kod == 'EOF':
                break
        except ValueError as e:
            print(f"\n[!] WYKRYTO BŁĄD W TWOIM SKANERZE: {e}")
            break

    # Przekazujemy oryginalny tekst oraz listę tokenów do highlightera
    colored = highlight(wyrazenie, tokens)
    html = wrap_html(colored)

    with open("output.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("Sukces! Wygenerowano plik 'output.html' z kolorowaniem składni.")

if __name__ == "__main__":
    main()