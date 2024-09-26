from PyPDF2 import PdfMerger

# Create a PdfMerger object
merger = PdfMerger()

# Paths to the PDF files you want to merge
pdf1 = "output1-bookmarks.pdf"
pdf2 = "output2-bookmarks.pdf"

# Append both PDFs to the merger object
merger.append(pdf1)
merger.append(pdf2)

# Write out the merged PDF
output_pdf = "gcp_notes_sketch.pdf"
with open(output_pdf, "wb") as output_file:
    merger.write(output_file)

# Close the PdfMerger object
merger.close()

print(f"Successfully merged {pdf1} and {pdf2} into {output_pdf}")
