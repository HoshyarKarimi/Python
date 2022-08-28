import easygui as gui
from PyPDF2 import PdfFileReader, PdfFileWriter


while True:
    input_path = gui.fileopenbox(
        msg="Select a PDF to rotate...",
        default="*.pdf"
    )
    if input_path is None:
        exit()
    magic_number = {'pdf': bytes([0x25, 0x50, 0x44, 0x46])}
    with open(input_path, mode='rb') as fd:
        file_head = fd.read(4)
    if not file_head.startswith(magic_number['pdf']):
        gui.msgbox("Invalid PDF file!")
    else:
        break

choices = ('90', '180', '270')
degrees = gui.buttonbox(
    msg="Rotate the PDF clockwise by how many degrees?",
    title="Choose rotation...",
    choices=choices
)
degrees = int(degrees)

output_path = gui.filesavebox(
    title="Save the rotated PDF as...",
    default="*.pdf",
)


while input_path == output_path:
    gui.msgbox("Cannot overwrite original file!")
    output_path = gui.filesavebox(
        title="Save the rotated PDF as...",
        default="*.pdf",
    )

if output_path is None:
    exit()

input_file = PdfFileReader(input_path)
output_pdf = PdfFileWriter()

for page in input_file.pages:
    page = page.rotate_clockwise(degrees)
    output_pdf.add_page(page)

with open(output_path, mode='wb') as output_file:
    output_pdf.write(output_file)
