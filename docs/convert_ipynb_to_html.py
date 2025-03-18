import nbconvert
import os
import logging

try:
    exporter = nbconvert.HTMLExporter()
    logging.info(os.listdir())
    all_notebooks = [book for book in os.listdir('_static\\notebooks') if ".ipynb" in book]
    for notebook in all_notebooks:

        body, _ = exporter.from_filename(f"_static\\notebooks\\{notebook}")

        new_nb_name = notebook.replace(".ipynb", ".html")
        with open(f"_static\\notebooks\\{new_nb_name}", "w", encoding="utf-8") as f:
            f.write(body)
except Exception as e:
    logging.error(f"FAILED TO DOCUMENT NOTEBOOKS: {e}")
