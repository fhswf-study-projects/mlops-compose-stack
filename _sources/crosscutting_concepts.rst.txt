8. Crosscutting Concepts
===========================

This section describes all essential and interconnected concepts that influence multiple aspects of the system.
These concepts ensure security, maintainability, scalability, and consistency across the architecture.


.. raw:: html
   :file: _images/crosscutting_concepts.html

=================================
8.1 Security and Authentication
=================================

- All public-facing services (FastAPI, Streamlit UI, MinIO, MLflow, Grafana) are secured using SSL/TLS encryption.
- Nginx Proxy acts as a reverse proxy and handles TLS termination using Let's Encrypt certificates.
- Ensures end-to-end encrypted communication between users and backend services.
- Fast-API got a Token-based authentication via API key.

=================================
8.2 Observability and Monitoring
=================================

- Prometheus collects system metrics like CPU, memory, response times, and database performance.
- Grafana Dashboards visualize real-time system health and ML model performance.
- Each service (PostgreSQL, RabbitMQ, MinIO, MLflow, API) has health check endpoints, which is also monitored.
- If a service becomes unhealthy, alerts are triggered via Prometheus Alertmanager.
- Loki stores centralized logs, reducing the need for individual service log files.
- Structured logging (JSON format) allows easy searching and filtering.
- Tempo traces API calls, tracking latency bottlenecks across services.

=================================
8.3 Logging and Tracing
=================================

- Loki aggregates logs from FastAPI, Streamlit UI, and Data Processor.
- Logs are stored persistently and queried and visualized via Grafana.
- Each request receives a unique trace ID, linking logs across services.
- Helps detect slow API responses and identify failures.

=================================
8.4 Configuration Management
=================================

- Docker Compose and .env files manage secrets and configuration.
- Prevents hardcoding sensitive information (e.g., API keys, DB passwords).
- Services communicate using Docker internal DNS (rabbitmq, postgres, s3).
- No hardcoded IP addresses, ensuring flexible deployments.
- GitHub secrets to manage sensitive information (e.g., password, API keys).

=================================
8.5 Scalability and Resilience
=================================

- Asynchronous processing via RabbitMQ prevents blocking API requests.
- Retry mechanisms in place to handle transient failures.
- API services, Streamlit UI, and Data Processor can scale independently.
- Load balancing via Nginx Proxy distributes traffic evenly.
- Database services have automatic reconnection logic.
- MinIO supports replication to prevent data loss.

================================================
8.6 Continuous Integration and Deployment (CI/CD)
================================================

- GitHub Actions CI/CD automates build, test, and deployment workflows.
- Unit tests, integration tests, and API tests ensure stability.
- Automated documentation

================================================
8.7  Data Versioning and Management
================================================

- MLflow tracks and manages model versions, ensuring reproducibility.
- New models are automatically logged, compared, and deployed.
- MinIO (S3-compatible storage) stores datasets, logs, and model artifacts.