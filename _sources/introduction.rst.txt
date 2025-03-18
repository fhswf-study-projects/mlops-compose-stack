1. Introduction and Goals
===========================
We use arc42-template as a standard documentation layout (`ARC42 <https://arc42.org/overview>`_). This documentation
is especially for new developers and all new contributors of this project. This section will describe the goal and give
an small overview.


===============================
1.1 Task Description
===============================

**What is FH-SWF MLOPS?**

- MLOPs-Project is a study project for "Fachhochschule Südwestfalen" to learn the concepts of MLOPs.
- Uses  `Adult-Income-Dataset  <https://www.kaggle.com/datasets/wenruliu/adult-income-dataset/data>`_
  within the MLOPs-Pipeline. The target is to make prediction for income (>50.000$/a or <50.000$&/a). So
  a solution for a binary classification problem.
- The goal is to create a End-to-End MLOPs solution, using best practices.

**Essential Features**

- Data preparation (exploration, cleaning and versioning).
- Model: Feature-Engineering, evaluation and hyperparameter-tuning.
- API: FastAPI as a middleman to handle different jobs.
- Uses CI/CD pipeline for fast and continuous deployment.
- Frontend: Streamlit as a frontend-solution, a input-form to make predictions.
- Quality: Tests, Monitoring concepts and documentation.

**Technical and theoretical Requirements**

- **Git** for versioncontrol of all services.
- **MLflow** for tracking, model versioning and artifact handling.
- **FastAPI** for backend.
- **Docker** for Containerisation.
- **Streamlit** for frontend.
- **Python** as a programming language.
- **Machine Learning** for modeling.

===============================
1.2 Quality-Target
===============================

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Quality Target
     - Motivation and Description
   * - **Maintainability**
     - The pipeline should be modular and well-documented to allow easy modifications and extensions.
   * - **Reproducibility**
     - The entire ML workflow, from data ingestion to model deployment, should be reproducible using version-controlled code and Docker containers.
   * - **Automation**
     - CI/CD pipelines should automate testing, deployment, and monitoring to minimize manual interventions.
   * - **Performance**
     - Model training and inference should be optimized to provide quick responses, especially in real-time applications.
   * - **User-Friendliness**
     - The API and frontend should be intuitive and accessible for non-technical users.
   * - **Reliability**
     - The system should be robust and capable of handling edge cases without crashing.
   * - **Threshhold**
     - The system should be able to retrigger the training, if the performance decreases and reaches a specific threshold.

===============================
1.3 Stakeholders
===============================

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Who?
     - Interest and Relation
   * - **A new Developer**
     -   - Needs a overview of this project.
         - Wants to develop new features.
         - Needs a easy access and a fast introduction to this project.
   * - **User**
     -   - Uses the application.
         - Needs an intuitive UI.
         - Expects reliability.
         - Wants to predict the Income (less or more then 50.000$/a?).
         - Needs almost real-time response.
   * - **Students**
     -   - Wants to understand the best-practices concept for MLOPs.
         - Needs an example (this one) to understand MLOPs concepts.
