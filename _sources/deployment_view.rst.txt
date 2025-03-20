7. Deployment View
============================

============================
7.1 Infrastructure Overview
============================

The system is deployed on a self-hosted server using Docker Compose. Services are organized into different profiles:

- **Tech Stack:** Core infrastructure services (Nginx, RabbitMQ, PostgreSQL, MinIO, MLflow, Prometheus, Loki, Tempo, Mimir, Grafana).
- **Application Services**: Streamlit UI, FastAPI Backend (Pipeline API), Data Processor.
The server runs all containers in an isolated Docker network, exposing only necessary ports through an Nginx reverse proxy
with automated Let's Encrypt SSL certificates.

============================
7.2 Deployment Diagram
============================

.. mermaid::

    graph TD
        subgraph Self-Hosted Server
            subgraph Docker Network
                subgraph Reverse Proxy
                    Nginx[Nginx Proxy] -->|SSL Certificates| Acme[Acme Companion]
                end

                subgraph Core Services
                    DB[PostgreSQL]
                    MQ[RabbitMQ]
                    S3[MinIO]
                    MLflow[MLflow Server]
                    Logs[Prometheus + Loki + Tempo + Mimir] --> Grafana[Grafana]
                end

                subgraph Application Services
                    UI[Streamlit UI] -->|API Calls| API[FastAPI Backend]
                    API -->|Model Requests| DP[Data Processor]
                    DP -->|Fetch Model| MLflow
                    DP -->|Store Data| S3
                    API -->|Queue Tasks| MQ
                end
            end
        end

================================
7.3 Network and Hosting Details
================================

- All services are deployed in Docker containers.
- The Nginx reverse proxy exposes public services using HTTPS (port 443).
- Internal communication happens within the Docker network.
- Persistent data (DB, MinIO, MLflow) is stored in Docker volumes.
- There is a staging and a production view of the services.

.. list-table:: Deployment Services
   :header-rows: 1
   :widths: 25 40 15 15 10

   * - **Service**
     - **Host/URL - Production**
     - **Host/URL - Staging**
     - **Port**
     - **Exposed?**
   * - Nginx Proxy
     - /
     - /
     - 443
     - Privat
   * - RabbitMQ
     - `https://rabbitmq.mlops.dns64.de/`
     - `https://rabbitmq.staging.mlops.iot64.de/`
     - 15672
     - Public
   * - PostgreSQL
     - `postgres`
     - `postgres`
     - 5432
     - Private
   * - MinIO
     - `https://s3.mlops.iot64.de/`
     - `https://s3.staging.mlops.iot64.de/`
     - 9001
     - Public
   * - MLflow
     - `https://mlflow.mlops.iot64.de/`
     - `https://mlflow.staging.mlops.iot64.de/`
     - 5000
     - Public
   * - Prometheus
     - /
     - /
     - 9090
     - Private
   * - Grafana
     - `https://monitoring.mlops.iot64.de/`
     - `https://monitoring.staging.mlops.iot64.de/`
     - 3000
     - Public
   * - FastAPI Backend
     - `https://api.mlops.dns64.de/`
     - `https://api.staging.mlops.dns64.de/`
     - 8000
     - Public
   * - Streamlit UI
     - `https://app.mlops.dns64.de/`
     - `https://app.staging.mlops.dns64.de/`
     - 8501
     - Public

================================
7.4 Deployment Process
================================

1. CI/CD Pipeline

- All services are built and published as Docker images via GitHub Actions.
- Images are pushed to GitHub Container Registry (GHCR).
- The latest version is deployed using Docker Compose.
- Startup Sequence

2. Nginx Proxy starts first.

- Database (PostgreSQL) and RabbitMQ must be ready before application services start.
- MinIO (S3 storage) must be running before MLflow can store artifacts.
- Monitoring & Logging

3. Prometheus collects system metrics.

- Loki stores logs from all services.
- Tempo handles distributed tracing.
- Grafana visualizes logs, metrics, and traces.

====================================
7.5 Scaling and Future Improvements
====================================

- The system can be extended to Kubernetes for better scalability.
- A load balancer can distribute API requests for high availability.
- Auto-scaling workers can be introduced for handling data processing.