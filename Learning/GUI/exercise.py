import easygui as gui
from PyPDF2 import PdfFileReader, PdfFileWriter

input_path = gui.fileopenbox(
    title="Select a PDF file",
    default="*.pdf",
)

if input_path is None:
    exit()

while True:
    start_page = gui.enterbox(
        title="PDF page selector",
        msg="Enter start page",
    )
    if start_page is None:
        exit()
    start_page = int(start_page)
    if start_page < 0:
        gui.msgbox(
            title="Error",
            msg="Start page can't be negative."
        )
    else:
        break

while True:
    end_page = gui.enterbox(
        title="PDF page selector",
        msg="Enter end page"
    )
    if end_page is None:
        exit()
    end_page = int(end_page)
    if end_page < start_page:
        gui.msgbox(
            title="Error",
            msg="End page can't be less than start page"
        )
    else:
        break

while True:
    output_path = gui.filesavebox(
        title="Save file",
        default="*.pdf",
    )
    if output_path is None:
        exit()
    if output_path == input_path:
        gui.msgbox(
            title="Error",
            msg="Unable to overwrite file, choose a different name"
        )
    else:
        break

pdf_reader = PdfFileReader(input_path)
pdf_writer = PdfFileWriter()

for i in range(start_page, end_page + 1):
    page = pdf_reader.pages[i - 1]
    pdf_writer.add_page(page)

with open(output_path, 'wb') as output_file:
    pdf_writer.write(output_file)
