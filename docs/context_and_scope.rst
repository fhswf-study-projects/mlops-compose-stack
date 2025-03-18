3. Context and Scope
============================

This section describes the technical framework and the dataset used in this project.
The developed **MLOps pipeline** ensures that machine learning models can be efficiently trained,
managed, and deployed.

==================================
3.1 Adult Income Context
==================================

The **Adult Income Dataset** contains demographic and income-related information.
The goal is to build a classification model that predicts whether an individual's
income is above or below 50.000$.

To better understand the dataset, several Jupyter Notebook analyses are available:

.. raw:: html

    <details>
      <summary>📊 Click to Expand: Environment for Exploration</summary>
      <iframe src="_static/notebooks/00_Umgebung einrichten-en.html" width="100%" height="600px" style="border:none;"></iframe>
    </details>

.. raw:: html

   <details>
   <summary>📊 Click to Expand: Data Exploration & Validation</summary>
   <iframe src="_static/notebooks/01_Daten_Exploration_und_Validierung-en.html" width="100%" height="600px" style="border:none;"></iframe>
   </details>

.. raw:: html

   <details>
   <summary>📊 Click to Expand: Data Preparation</summary>
   <iframe src="_static/notebooks/02_Daten_Vorverarbeitung-en.html" width="100%" height="600px" style="border:none;"></iframe>
   </details>

==========================
3.2 Technical Context
==========================

.. raw:: html
   :file: _images/context_view.html


🖥️ **Streamlit User Interface:**

- A simple web frontend where users can enter their data.

🚀 **FastAPI (Backend):**

- Receives user inputs and processes them.
- Communicates with the Data Processor to generate predictions.
- Returns the prediction result to the user.

🧠 **Data Processor (Core Component):**

- Trains and stores ML models.
- Performs predictions.
- Stores all data processing steps in MinIO and manages model versions with MLflow.

📦 **MLflow (Model Management):**

- Manages different model versions.
- Stores model metrics and artifacts.

🗄️ **MinIO (Data Versioning):**

- Stores different dataset versions.
- Ensures reproducibility of the pipeline.


**Why is this Context Important?**

This MLOps pipeline is designed to ensure that machine learning models are not
just trained once but can be continuously improved and efficiently deployed.


