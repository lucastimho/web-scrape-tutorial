import PyPDF2

f = open("Working_Business_Proposal.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(f)
print(pdf_reader.numPages)
page_one = pdf_reader.getPage(0)
page_one_text = page_one.extractText()
print(page_one_text)
# page_one
# pdf_writer = PyPDF2.PdfFileWriter()
# pdf_writer.addPage(page_one)
# pdf_output = open("Some_BrandNew_Doc.pdf", "wb")
# pdf_writer.write(pdf_output)
# f.close()
# pdf_output.close()
pdf_text = []
for num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(num)
    pdf_text.append(page.extractText())
print(pdf_text)
f.close()
