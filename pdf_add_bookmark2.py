import fitz  # PyMuPDF

# Open the PDF
pdf_document = "gcp_Illustrations.pdf"
doc = fitz.open(pdf_document)

# Define a Table of Contents (TOC) structure
# Format: [level, title, page number, ...]
toc = [
    [1, "Cloud Storage", 2],  # Page numbers are 1-based (so page 1 is the first page)
    [1, "Cloud Pub/Sub", 3],
    [1, "Dataproc", 4],  # Level 2 is a nested bookmark (child of Chapter 3)
    [1, "Dataflow", 5],
    [1, "BigQuery", 6],
    [1, "Data Catalog", 7],
    [1, "Data Fusion", 8],
    [1, "Cloud Composer", 9],
    [1, "Looker", 10]
]

# Set the table of contents (bookmarks)
doc.set_toc(toc)

# Save the modified PDF
doc.save("output2-bookmarks.pdf")
doc.close()

print("Bookmarks added successfully!")
