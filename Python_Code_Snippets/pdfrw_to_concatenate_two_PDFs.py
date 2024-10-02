from pdfrw import PdfReader, PdfWriter, IndirectPdfDict

def concatenate(paths, output):
    # This Function will create a new pdf file by concatenate two PDFs together
    writer = PdfWriter()

    for path in paths:
        reader = PdfReader(path)
        writer.addpages(reader.pages)
    
    writer.trailer.Info = IndirectPdfDict(
        Title = 'Combining PDF title',
        Auther = 'Michel Driscoll',
        Subject = 'PDF Combinations',
        Creator = 'The Concatenator'
    )

    writer.write(output)

if __name__ == '__main__':
    paths = ['/workspaces/PYTHON/Python_Code_Snippets/Sample.pdf','/workspaces/PYTHON/Python_Code_Snippets/Sample_pdf2.pdf']
    concatenate(paths,'concatenate.pdf')





