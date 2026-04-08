class Token:
    """Struktura przechowująca informacje o rozpoznanym tokenie."""

    def __init__(self, kod, wartosc, kolumna):
        self.kod = kod  # kod tokenu 'NUMBER', 'PLUS'
        self.wartosc = wartosc  # wartosc tokenu '76', '+'
        self.kolumna = kolumna  # pozycja rozpoczecia tokenu

    def __repr__(self):
        return f"Token(kod='{self.kod:6}', atrybut='{self.wartosc:2}', kolumna={self.kolumna})"


class AnalizatorLeksykalny:
    def __init__(self, tekst):
        self.tekst = tekst
        self.pozycja = 0
        self.biezacy_znak = self.tekst[self.pozycja] if self.tekst else None

    def idz_dalej(self):
        """Przesuwa wskaźnik na kolejny znak w tekście."""
        self.pozycja += 1
        if self.pozycja >= len(self.tekst):
            self.biezacy_znak = None  # koniec tekstu
        else:
            self.biezacy_znak = self.tekst[self.pozycja]

    def pomijaj_biale_znaki(self):
        """Pomijanie znaków białych."""
        while self.biezacy_znak is not None and self.biezacy_znak.isspace():
            self.idz_dalej()

    def skanuj_liczbe(self):
        """Rozpoznaje token wielowartościowy: Liczba całkowita."""
        wynik = ''
        start_kolumna = self.pozycja + 1
        while self.biezacy_znak is not None and self.biezacy_znak.isdigit():
            wynik += self.biezacy_znak
            self.idz_dalej()
        return Token('NUMBER', wynik, start_kolumna)

    def skanuj_identyfikator(self):
        """Rozpoznaje token wielowartościowy: Identyfikator (zmienna)."""
        wynik = ''
        start_kolumna = self.pozycja + 1
        # najpierw litera, potem cyfry lub litery
        while self.biezacy_znak is not None and self.biezacy_znak.isalnum():
            wynik += self.biezacy_znak
            self.idz_dalej()
        return Token('ID', wynik, start_kolumna)

    def skaner(self):
        """
        Główna funkcja skanera. Wywoływana w pętli zwraca kolejny token.
        Działa jak maszyna stanów bazująca na bieżącym znaku.
        """
        while self.biezacy_znak is not None:

            # 1. pomijanie bialych znakow
            if self.biezacy_znak.isspace():
                self.pomijaj_biale_znaki()
                continue

            # zapamietujemy kolumne (+1 dla czeytelnosci)
            kolumna = self.pozycja + 1

            # 2. rozpoznawanie liczb
            if self.biezacy_znak.isdigit():
                return self.skanuj_liczbe()

            # 3. rozpoznawanie identyfikatorow
            if self.biezacy_znak.isalpha():
                return self.skanuj_identyfikator()

            # 4. tokeny jednowartosciowe
            znak = self.biezacy_znak
            if znak == '+':
                self.idz_dalej()
                return Token('PLUS', znak, kolumna)
            elif znak == '-':
                self.idz_dalej()
                return Token('MINUS', znak, kolumna)
            elif znak == '*':
                self.idz_dalej()
                return Token('MUL', znak, kolumna)
            elif znak == '/':
                self.idz_dalej()
                return Token('DIV', znak, kolumna)
            elif znak == '(':
                self.idz_dalej()
                return Token('LPAREN', znak, kolumna)
            elif znak == ')':
                self.idz_dalej()
                return Token('RPAREN', znak, kolumna)

            # 5. Obsluga bledow leksykalnych
            # jesli nie pasuje do zadnej reguly, zglaszamy blad
            bledny_znak = self.biezacy_znak
            blad_kolumna = self.pozycja + 1
            self.idz_dalej()  # idziemy dalej
            raise ValueError(f"Blad leksykalny: nierozpoznany znak: '{bledny_znak}'; kolumna: {blad_kolumna}")

        # zwracamy token konca pliku
        return Token('EOF', '', self.pozycja + 1)