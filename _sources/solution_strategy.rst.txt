4. Solution Strategy
============================

The Solution Strategy defines the fundamental design decisions, technology choices,
and best practices that guide the development of the MLOps pipeline.
These decisions ensure that the system meets technical, organizational,
and functional requirements effectively.

==================================
4.1 Guiding Principles
==================================

The project follows these key principles:

- **Reproducibility:** The entire pipeline (from data processing to deployment) must be easily reproducible across different environments.

- **Scalability:** The system should handle increasing data loads and future model iterations without significant rework.

- **Automation:** Continuous Integration and Continuous Deployment (CI/CD) should minimize manual interventions and improve efficiency.

- **Modularity:** Each component (data processing, model training, API, UI) is developed independently, ensuring flexibility and maintainability.

- **Open Source & Transparency:** The project is released under GPLv3, ensuring community collaboration and knowledge sharing.

==================================
4.2 Architectural Approach
==================================

- Microservices-Based Architecture
   - The system is split into independent services, such as FastAPI (backend), Streamlit (frontend)
     and a separate data-processor.
   - This allows independent scaling and development.

- Cloud & Local Compatibility
   - The system should be deployable both on local machines and on cloud platform such as Azure, AWS or GCP.
     It should be also possible to run the system on a own server.

- Data & Model Versioning
   - MinIO (object storage) is used to store processed or raw datasets for example. It should maintain
     different dataset versions.

- Docker
   - Docker ensures reproducible infrastructure deployment via a sing docker-compose file.


=================================
4.3 Technology Stack
=================================

.. list-table::
   :header-rows: 1
   :widths: 30 30 70

   * - Component
     - Technology
     - Justification
   * - **Programming Language**
     - Python
     - Wide ML & MLOps support
   * - **Model Training & Tracking**
     - Scikit-learn and MLflow
     - Standard ML pipelines
   * - **Data Processing (Backend)**
     - Pandas, NumPy ...
     - Efficient data handling
   * - **Version Control**
     - Git (GitHub)
     - One of the standards
   * - **Infrastructure**
     - Docker
     - Scalable & reproducible deployments
   * - **Frontend**
     - Streamlit
     - Lightweight UI for ML apps
   * - **Backend**
     - FastAPI
     - Fast and scalable API, also easy to develop
   * - **CI/CD**
     - Github Actions
     - Automated testing & deployment
   * - **Logging**
     - Loki
     - Collects logs from all services (FastAPI, Streamlit, MLflow, etc.)
   * - **Visualization and Monitoring**
     - Grafana
     - Displays logs, metrics, and traces from Loki, Tempo, and Mimir, also triggers the threshold
   * - **Distributed Tracing**
     - Tempo
     - Captures request traces across multiple services for debugging
   * - **Metrics storage**
     - Mimir
     - Stores system metrics like CPU, memory, request latency, etc.


=================================
4.4 Risk Management
=================================


.. list-table::
   :header-rows: 1
   :widths: 30 30

   * - Risk
     - Mitigation Strategy
   * - **Incompatibility across environments**
     - Docker ensures consistency
   * - **Data/model loss**
     - MinIO & MLflow for versioning