import os
import fitz  # PyMuPDF
from PIL import Image

def convert_pdf_to_jpegs(pdf_path, output_directory):
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Open the PDF document
    pdf_document = fitz.open(pdf_path)

    # Create a directory for the PDF
    pdf_filename = os.path.splitext(os.path.basename(pdf_path))[0]
    pdf_output_directory = os.path.join(output_directory, pdf_filename)
    os.makedirs(pdf_output_directory, exist_ok=True)

    # Save each page as a JPEG image
    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        image = page.get_pixmap()
        pil_image = Image.frombytes("RGB", [image.width, image.height], image.samples)

        # Save the image as a JPEG file
        jpeg_filename = f"page_{page_number + 1}.jpg"
        jpeg_path = os.path.join(pdf_output_directory, jpeg_filename)
        pil_image.save(jpeg_path)

        print(f"Page {page_number + 1} saved: {jpeg_path}")

    # Close the PDF document
    pdf_document.close()

def convert_pdfs_in_directory(directory_path, output_directory):
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Process each PDF file in the input directory
    for filename in os.listdir(directory_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(directory_path, filename)

            convert_pdf_to_jpegs(pdf_path, output_directory)
            print(f"Conversion complete for {pdf_path}")

# Specify your input and output directories
input_directory = r"/media/usb1/Emby Server/Books"
output_directory = r"/media/usb1/Emby Server/Books"

# Convert PDFs in the input directory to JPEGs in separate directories in the output directory
convert_pdfs_in_directory(input_directory, output_directory)
