from scanner import *

def main():
    # poprawne wyrazenie z zadania
    # 2+3*(76+8/3)+ 3*(9-3)
    # bledne wyrazenie do testow
    # 2+3 * $ + 5
    wyrazenie = input("Podaj wyrażenie: ")

    skaner_obj = AnalizatorLeksykalny(wyrazenie)

    # funkcja skaner w petli az do EOF
    while True:
        try:
            token = skaner_obj.skaner()
            print(token)
            if token.kod == 'EOF':
                break
        except ValueError as e:
            print(f"\n[!] WYKRYTO BLAD: {e}")
            break

if __name__ == "__main__":
    main()