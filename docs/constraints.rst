2. Constraints
==============================

The solution design is subject to several constraints that impact its architecture and implementation.
This section outlines these constraints and their motivations.

===============================
2.1 Technical
===============================

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Constraint
     - Explanation, Background
   * - **Moderate Hardware Requirements**
     - The solution should run on a standard consumer-grade laptop to ensure accessibility.
   * - **Deployment on Cloud and Local Environments**
     - The pipeline should be deployable both on cloud platforms (e.g., Azure) and local environments

       (Windows/Linux/Mac) to ensure flexibility in different infrastructures.
   * - **Implementation in Python**
     - Python is chosen as the primary language due to its widespread use in Machine Learning,

       support for MLOps tools, and ease of integration with frameworks like FastAPI, Streamlit, and MLflow.
   * - **Usage of Open-Source Tools**
     - All dependencies should be open-source and freely available to ensure

       accessibility for all students without licensing costs. This includes libraries like

       Scikit-learn, MLflow, and Docker.

===============================
2.2 Organization
===============================

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Constraint
     - Explanation, Background
   * - **Team**
     - Team of 5 student of Fachhochschule Südwestfalen, M.Sc. Data Science.
   * - **Schedule**
     - Around 2 months for implementation of the whole MLOPs-Pipeline.
   * - **Deadline**
     - 23.03.2025
   * - **Development Tools**
     - Architecture and design will be drafted using Python code.

       The primary tools used will be VS Code and PyCharm and Jupiter Notebooks.
   * - **Configuration and Version Control**
     - Git will be used for version control, and the project will be hosted on GitHub for easy

       access and collaboration. Documentation and code will be tracked and versioned within the

       same repositories.
   * - **Tests and CI/CD**
     - Git workflows will be used on a self-hosted runner for the CI/CD Pipelines. But also for testing

       and automated processes like automated documentation delivery.
   * - **Release as Open Source**
     - The project's source code will be released as open-source under the GNU GENERAL PUBLIC LICENSE to

       encourage collaboration and allow others to contribute. The project will be hosted on

       GitHub for open access: `GitHub Organization <https://github.com/fhswf-study-projects>`_.

**Why Are These Constraints Important?**

By adhering to these constraints, the project ensures scalability,
accessibility, reproducibility, and maintainability—key principles of a robust MLOps pipeline.