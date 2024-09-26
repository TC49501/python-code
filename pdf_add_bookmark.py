import fitz  # PyMuPDF

# Open the PDF
pdf_document = "gcp-notes-sketch.pdf"
doc = fitz.open(pdf_document)

# Define a Table of Contents (TOC) structure
# Format: [level, title, page number, ...]
toc = [
    [1, "Where 2 run", 1],  # Level 1 is the top-level bookmark
    [1, "VPC Network", 2],  # Page numbers are 1-based (so page 1 is the first page)
    [1, "Load Balancing", 3],
    [1, "Cloud CDN", 4],  # Level 2 is a nested bookmark (child of Chapter 3)
    [1, "Cloud DNS", 5],
    [1, "Database & Storage", 6],
    [1, "ETL Pipeline", 7],
    [1, "AI / ML", 8],
    [1, "Cloud Operations", 9],
    [1, "Cloud Security", 10],
    [1, "Cloud Build", 11]
]

# Set the table of contents (bookmarks)
doc.set_toc(toc)

# Save the modified PDF
doc.save("output1-bookmarks.pdf")
doc.close()

print("Bookmarks added successfully!")
