import pdfplumber

# Path to the uploaded PDF file
pdf_path = "C:/Users/eliyaser/Downloads/sample.pdf"

# Open the PDF file and extract the text
with pdfplumber.open(pdf_path) as pdf:
    pdf_text = ''
    for page in pdf.pages:
        pdf_text += page.extract_text()

# Display a portion of the extracted text for review
print(pdf_text[:20000])
