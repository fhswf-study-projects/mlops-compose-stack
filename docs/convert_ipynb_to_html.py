import nbconvert
import os
import logging

try:
    exporter = nbconvert.HTMLExporter()
    all_notebooks = [book for book in os.listdir('_static\\notebooks') if ".ipynb" in book]
    for notebook in all_notebooks:

        body, _ = exporter.from_filename(f"_static\\notebooks\\{notebook}")

        with open(f"_static\\notebooks\\{notebook.replace(".ipynb", ".html")}", "w", encoding="utf-8") as f:
            f.write(body)
except:
    logging.warning("FAILED TO DOCUMENT NOTEBOOKS")
