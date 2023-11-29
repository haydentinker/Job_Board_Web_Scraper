import PyPDF2


resume=open('resume.pdf','rb')

pdfReader=PyPDF2.PdfReader(resume)

page=pdfReader.pages[0]

print(page.extract_text())