# import pdfplumber

# with pdfplumber.open("teste.pdf") as pdf:
#     for page in pdf.pages:
#         page_text = page.extract_text()
#         if page_text.split('\n')[0] == 'RESUMO':
#             print(page_text)

import pymupdf  # PyMuPDF
import re
import urllib.request
import sys

# def extrair_resumo(link, name):
#     file_name = name + ".pdf"
#     urllib.request.urlretrieve(link, file_name)
#     with pymupdf.open(file_name) as doc:
#         for page in doc:
#             texto = page.get_text()
#             linhas = [l.strip() for l in texto.splitlines() if l.strip()]
#             if linhas and linhas[0].upper() == "RESUMO":
#                 corpo = "\n".join(linhas[1:])
#                 m = re.search(r"(Palavras[- ]chave:.*)", corpo, re.S | re.I)
#                 if m:
#                     corpo = corpo[:m.end()]
#                 return corpo
#     return None

def extrair_resumo(file_name):
    with pymupdf.open(file_name) as doc:
        for page in doc:
            texto = page.get_text()
            linhas = [l.strip() for l in texto.splitlines() if l.strip()]
            if linhas and linhas[0].upper() == "RESUMO":
                corpo = "\n".join(linhas[1:])
                m = re.search(r"(Palavras[- ]chave:.*)", corpo, re.S | re.I)
                if m:
                    corpo = corpo[:m.end()]
                return corpo
    return None

print(extrair_resumo(sys.argv[1]))