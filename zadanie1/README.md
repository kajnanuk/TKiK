
---

## Język implementacji

Python

---
## Specyfikacja Tokenów

| Kod (Symbol) | Wyrażenie regularne / Znak | Opis | Typ tokenu       | Atrybut (Wartość) |
| :--- | :--- | :--- |:-----------------| :--- |
| `NUMBER` | `[0-9]+` | Liczba całkowita | Wielowartościowy | Ciąg cyfr, np. `"76"`, `"8"` |
| `ID` | `[a-zA-Z_][a-zA-Z0-9_]*` | Identyfikator (nazwa zmiennej) | Wielowartościowy | Ciąg znaków, np. `"x"`, `"suma"` |
| `PLUS` | `+` | Operator dodawania | Jednowartościowy | *Brak* (stały: `"+"`) |
| `MINUS` | `-` | Operator odejmowania | Jednowartościowy | *Brak* (stały: `"-"`) |
| `MUL` | `*` | Operator mnożenia | Jednowartościowy | *Brak* (stały: `"*"`) |
| `DIV` | `/` | Operator dzielenia | Jednowartościowy | *Brak* (stały: `"/"`) |
| `LPAREN` | `(` | Nawias otwierający | Jednowartościowy | *Brak* (stały: `"("`) |
| `RPAREN` | `)` | Nawias zamykający | Jednowartościowy | *Brak* (stały: `")"`) |
| `EOF` | *Koniec ciągu / pliku* | Znacznik końca tekstu | Pomocniczy       | *Brak* |