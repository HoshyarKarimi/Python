import easygui as gui
from PyPDF2 import PdfFileReader, PdfFileWriter, errors
from pathlib import Path


input_path = gui.fileopenbox(
    msg="Select a PDF to rotate...",
    default="*.pdf"
)
if input_path is None:
    exit()


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

try:
    input_file = PdfFileReader(input_path)
except errors.PdfReadError:
    gui.msgbox(
        title="Error opening file",
        msg=f"{Path(input_path).name} is not a pdf file"
    )
    exit()
output_pdf = PdfFileWriter()

for page in input_file.pages:
    page = page.rotate_clockwise(degrees)
    output_pdf.add_page(page)

with open(output_path, mode='wb') as output_file:
    output_pdf.write(output_file)
