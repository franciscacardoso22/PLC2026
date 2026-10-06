import re

# Ler o ficheiro markdown
with open("exemplo.md", "r", encoding="utf-8") as f:
    texto = f.read()

# Cabeçalhos (# até ###)
texto = re.sub(r"^### (.*)$", r"<h3>\1</h3>", texto, flags=re.MULTILINE)
texto = re.sub(r"^## (.*)$", r"<h2>\1</h2>", texto, flags=re.MULTILINE)
texto = re.sub(r"^# (.*)$", r"<h1>\1</h1>", texto, flags=re.MULTILINE)

# Imagens (antes dos links)
texto = re.sub(r"!\[(.*?)\]\((.*?)\)", r'<img src="\2" alt="\1"/>', texto)

# Links
texto = re.sub(r"\[(.*?)\]\((.*?)\)", r'<a href="\2">\1</a>', texto)

# Bold (antes do itálico)
texto = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", texto)

# Itálico
texto = re.sub(r"\*(.*?)\*", r"<i>\1</i>", texto)

# Listas numeradas (itens 1. texto -> <li>texto</li>)
texto = re.sub(r"^\d+\.\s+(.*)$", r"<li>\1</li>", texto, flags=re.MULTILINE)

# Envolver blocos contínuos de <li> em <ol>...</ol>
texto = re.sub(r"((?:<li>.*</li>\n?)+)", r"<ol>\n\1</ol>", texto)

# Guardar o resultado num ficheiro HTML
with open("resultado.html", "w", encoding="utf-8") as f:
    f.write(texto)

print("Conversão concluída. Gerado o ficheiro resultado.html")

