from PyPDF2 import PdfReader

reader = PdfReader("file.pdf")

text = ""

for page in reader.pages:
    text += page.extract_text()

print(text)