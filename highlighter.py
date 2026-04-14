import html as html_lib
import json
import os


def load_theme(file_path="styles.json"):
    """Wczytuje motyw z pliku JSON. Zwraca pusty schemat w razie braku pliku."""
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"styles": {}, "token_mapping": {}}


def highlight(oryginalny_tekst, tokens, theme_file="styles.json"):
    theme = load_theme(theme_file)
    styles = theme.get("styles", {})
    mapping = theme.get("token_mapping", {})

    default_style = styles.get("DEFAULT", "color: black;")

    html_output = ""
    ostatnia_pozycja = 0

    for token in tokens:
        if token.kod == 'EOF':
            break

        start_idx = token.kolumna - 1

        # 1. Dodajemy tekst pomiędzy tokenami (białe znaki)
        pominiete_znaki = oryginalny_tekst[ostatnia_pozycja:start_idx]
        html_output += html_lib.escape(pominiete_znaki)

        # 2. Mapowanie: Token -> Grupa -> Styl CSS
        # Jeśli token nie ma przypisanej grupy, dostanie tag "DEFAULT"
        grupa_tokenu = mapping.get(token.kod, "DEFAULT")
        style = styles.get(grupa_tokenu, default_style)

        wartosc = html_lib.escape(token.wartosc)
        html_output += f'<span style="{style}">{wartosc}</span>'

        ostatnia_pozycja = start_idx + len(token.wartosc)

    # 3. Reszta tekstu na końcu
    html_output += html_lib.escape(oryginalny_tekst[ostatnia_pozycja:])
    return html_output


def wrap_html(content):
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Grupy Składniowe - Highlight</title>
<style>
    body {{ font-family: 'Consolas', 'Monaco', monospace; background-color: #ecf0f1; padding: 40px; }}
    pre {{ background-color: #ffffff; padding: 20px; border-radius: 8px; border: 1px solid #bdc3c7; line-height: 1.5; font-size: 15px; }}
</style>
</head>
<body>
    <pre>{content}</pre>
</body>
</html>"""