# Extract text from pdf
#!pip install pypdf2
import PyPDF2

pdf = open("./files/NIPS-2017-attention-is-all-you-need-Paper.pdf", "rb")
reader = PyPDF2.PdfReader(pdf)
page = reader.pages[0]
print(page.extract_text())