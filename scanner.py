class Token:
    """Struktura przechowująca informacje o rozpoznanym tokenie."""

    def __init__(self, kod, wartosc, kolumna):
        self.kod = kod
        self.wartosc = wartosc
        self.kolumna = kolumna

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
            self.biezacy_znak = None
        else:
            self.biezacy_znak = self.tekst[self.pozycja]

    def pomijaj_biale_znaki(self):
        """Pomijanie znaków białych (spacje, tabulatory, znaki nowej linii)."""
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
        while self.biezacy_znak is not None and (self.biezacy_znak.isalnum() or self.biezacy_znak == '_'):
            wynik += self.biezacy_znak
            self.idz_dalej()
        return Token('ID', wynik, start_kolumna)

    def skaner(self):
        """
        Główna funkcja skanera. Wywoływana w pętli z zewnątrz, zwraca JEDEN token.
        Brak pętli while!
        """
        # 1. Pomijamy białe znaki na starcie (odpowiednik SkipSpaces)
        self.pomijaj_biale_znaki()

        # 2. Jeśli to koniec, zwracamy EOF
        if self.biezacy_znak is None:
            return Token('EOF', '', self.pozycja + 1)

        # Zapamietujemy kolumne (+1 dla czytelnosci)
        kolumna = self.pozycja + 1

        # 3. Rozpoznawanie liczb
        if self.biezacy_znak.isdigit():
            return self.skanuj_liczbe()

        # 4. Rozpoznawanie identyfikatorow
        if self.biezacy_znak.isalpha() or self.biezacy_znak == '_':
            return self.skanuj_identyfikator()

        # 5. Tokeny jednowartosciowe
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

        # 6. Obsluga bledow leksykalnych
        bledny_znak = self.biezacy_znak
        blad_kolumna = self.pozycja + 1
        self.idz_dalej()
        raise ValueError(f"Blad leksykalny: nierozpoznany znak: '{bledny_znak}'; kolumna: {blad_kolumna}")