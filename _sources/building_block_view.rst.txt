5. Building Block View
============================

==================================
5.1 Overview of Building Blocks
==================================

.. raw:: html
   :file: _images/technical_overview.html

Each service is built and published on GitHub via a CI/CD pipeline as a Docker container.
These containers are stored in GitHub Packages Registry and can be accessed
`HERE <https://github.com/fhswf-study-projects>`_. The Compose-Stack is responsible for deploying all
services onto the server, ensuring a fully functional MLOps pipeline. Each service is containerized
using Docker and orchestrated using Docker Compose, simplifying deployment and scaling.


The system is divided into multiple services, each managed in a separate GitHub repository.
Below is an overview of the repositories and their responsibilities:

.. list-table::
   :header-rows: 1
   :widths: 30 50 30

   * - Repository
     - Description
     - Link
   * - **Organization**
     - The organization site. Included all repositories for this project.
     - `Repository <https://github.com/fhswf-study-projects>`_
   * - **mlops-data-processor**
     - Core service responsible for data validation, preprocessing, and model inference.
     - `Repository <https://github.com/fhswf-study-projects/mlops-data-processor>`_
   * - **mlops-streamlit-ui**
     - Frontend interface for user interaction and predictions.
     - `Repository <https://github.com/fhswf-study-projects/mlops-streamlit-ui>`_
   * - **mlops-pipeline-api**
     - Backend API that receives user inputs and interacts with the data processor.
     - `Repository <https://github.com/fhswf-study-projects/mlops-pipeline-api>`_
   * - **docker-container-template**
     - A template for new services.
     - `Repository <https://github.com/fhswf-study-projects/docker-container-template>`_
   * - **mlops-compose-stack**
     - Deployment Stack, to bring all services together and deploy them (include LGTM, MinIO ...).
     - `Repository <https://github.com/fhswf-study-projects/mlops-compose-stack>`_

=====================================
5.2 Detailed Breakdown of Components
=====================================

Each service is managed in its own repository and interacts with others as follows:

- Frontend (streamlit-ui)
   - Calls FastAPI Backend requests predictions.
   - User can also give a feedback, if the prediction was True or False.
- Backend (fast-api):
   - Sends user input to Data-Processor and receives predictions.
- Backend (data-processor):
   - Uses a trained model to make predictions and fetches versioned data.
   - Also possible to trigger a new training-process, if the score falls below a specific threshold.
- Stack (compose-stack):
   - Uses CD pipelines to run and update different services.
   - Automated Documentation is implemented here as well.
   - There is a staging and a main service integration, where main is what user sees and staging is
     for testing new updates.
   - The includes all services, also LGTM-Stack (Loki, Grafana, Tempo and Mimir)