from PyPDF2 import PdfFileWriter, PdfFileReader 
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
import os, sys
import csv


def put_watermark(watermark_text, input_file_path, output_file_path):

    c = canvas.Canvas("watermark.pdf") 
    c.setFont("Helvetica", 24)
    c.setFillGray(0.5,0.5)
    c.saveState() 
    c.translate(500,100) 
    c.rotate(45) 
    c.drawCentredString(0, 300, watermark_text) 
    c.restoreState() 
    c.save() 

    input_file = PdfFileReader(input_file_path) 
    output_writer = PdfFileWriter() 
    total_pages = input_file.getNumPages()

    for single_page in range(total_pages):
        page = input_file.getPage(single_page)
        watermark = PdfFileReader("watermark.pdf")
        page.mergePage(watermark.getPage(0))
        output_writer.addPage(page)

    with open(output_file_path, "wb") as outputStream:
        output_writer.write(outputStream)
    os.remove("watermark.pdf")


def read_csv(csv_file_path):
    with open(csv_file_path) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            put_watermark(row[0], input_file_path, str(row[0]) + ".pdf")


if __name__ == '__main__':

    csv_file_path = sys.argv[1]
    input_file_path = sys.argv[2]
    read_csv(csv_file_path)

