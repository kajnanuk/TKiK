STYLES = {
    "ID": "color: black;",
    "NUMBER": "color: red;",
    "PLUS": "color: purple;",
    "MINUS": "color: purple;",
    "MUL": "color: purple;",
    "DIV": "color: purple;",
    "LPAREN": "color: gray;",
    "RPAREN": "color: gray;"
}


def highlight(tokens):
    html = ""
    for token in tokens:
        if token.kod == 'EOF':
            continue

        style = STYLES.get(token.kod, "color: black;")

        html += f'<span style="{style}">{token.wartosc}</span> '

    return html


def wrap_html(content):
    return f"""<html>
<head>
<meta charset="UTF-8">
<title>Syntax Highlight - Zadanie 2</title>
</head>
<body>
<pre>
{content}
</pre>
</body>
</html>"""