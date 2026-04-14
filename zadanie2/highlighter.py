import html as html_lib

STYLES = {
    "ID": "color: blue; font-weight: bold;",
    "NUMBER": "color: red;",
    "PLUS": "color: purple;",
    "MINUS": "color: purple;",
    "MUL": "color: purple;",
    "DIV": "color: purple;",
    "LPAREN": "color: gray;",
    "RPAREN": "color: gray;"
}


def highlight(oryginalny_tekst, tokens):
    html_output = ""
    ostatnia_pozycja = 0

    for token in tokens:
        if token.kod == 'EOF':
            break

        # Kolumna w skanerze jest liczona od 1, więc odejmujemy 1 by mieć indeks
        start_idx = token.kolumna - 1

        # 1. Dodajemy tekst pomiędzy poprzednim tokenem a obecnym (białe znaki)
        pominiete_znaki = oryginalny_tekst[ostatnia_pozycja:start_idx]
        html_output += html_lib.escape(pominiete_znaki)

        # 2. Tworzymy ostylowany span dla samego tokenu
        wartosc = html_lib.escape(token.wartosc)
        style = STYLES.get(token.kod, "color: black;")
        html_output += f'<span style="{style}">{wartosc}</span>'

        # 3. Aktualizujemy wskaźnik pozycji
        ostatnia_pozycja = start_idx + len(token.wartosc)

    # 4. Dodajemy ewentualne białe znaki na samym końcu pliku
    html_output += html_lib.escape(oryginalny_tekst[ostatnia_pozycja:])

    return html_output


def wrap_html(content):
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Syntax Highlight</title>
<style>
    body {{ font-family: monospace; background-color: #f5f5f5; padding: 20px; }}
    pre {{ background-color: white; padding: 15px; border: 1px solid #ddd; border-radius: 5px; font-size: 14px; }}
</style>
</head>
<body>
<pre>{content}</pre>
</body>
</html>"""