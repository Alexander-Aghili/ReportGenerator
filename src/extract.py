import PyPDF2

def extract_pdf_text(pdf_location: str, savefile: str = None) -> str:
    reader = PyPDF2.PdfReader(pdf_location)
    extract_text = ''
    for page in reader.pages:
        extract_text += page.extract_text()

    if savefile is not None:
        with open(savefile, 'w') as file:
            file.write(extract_text)

    return extract_text

