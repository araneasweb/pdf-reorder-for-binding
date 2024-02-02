import PyPDF2
import math
import sys

def cyclic_shift_pattern(n):
    pattern = [4, 1, 2, 3]
    return pattern[(n - 1) % len(pattern)] + 4 * math.floor((n-1)/4)

def rearrange_pdf(input_path, output_path):
    with open(input_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        pdf_writer = PyPDF2.PdfWriter()
        for i in range(num_pages):
            new_page_number = cyclic_shift_pattern(i + 1) - 1
            pdf_writer.add_page(pdf_reader.pages[new_page_number])

        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python rearrange_pdf.py INPUT_PATH OUTPUT_PATH")
    else:
        input_path = sys.argv[1]
        output_path = sys.argv[2]
        rearrange_pdf(input_path, output_path)
