# mlops-compose-stack

## Overview

The `mlops-compose-stack` is a customizable stack designed to streamline the development and deployment of machine learning projects using Docker Compose. It provides a standardized environment to ensure consistency across various stages of the ML lifecycle.

## Features

- **Modular Architecture**: Allows for easy customization and scalability.
- **Pre-configured Services**: Includes essential services like MLflow for experiment tracking and other tools to facilitate MLOps practices.
- **Seamless Integration**: Designed to work effortlessly with existing CI/CD pipelines and cloud environments.

## Environment Variables
The following environment variables must be set for the stack to function correctly:

Here's the corrected table with accurate descriptions and default values:  

| Variable                          | Description                                             | Default                  |
|-----------------------------------|---------------------------------------------------------|--------------------------|
| `RABBITMQ_DEFAULT_USER`           | Default username for RabbitMQ authentication            | None                     |
| `RABBITMQ_DEFAULT_PASSWORD`       | Default password for RabbitMQ authentication            | None                     |
| `PG_USER`                         | Username for the PostgreSQL database                    | None                     |
| `PG_PASSWORD`                     | Password for the PostgreSQL database                    | None                     |
| `PG_DATABASE`                     | Name of the PostgreSQL database                         | None                     |
| `PG_MLFLOW_USER`                  | Username for the MLflow PostgreSQL database             | None                     |
| `PG_MLFLOW_PASSWORD`              | Password for the MLflow PostgreSQL database             | None                     |
| `PG_MLFLOW_DATABASE`              | Name of the MLflow PostgreSQL database                  | None                     |
| `PG_CELERY_USER`                  | Username for the Celery PostgreSQL database             | None                     |
| `PG_CELERY_PASSWORD`              | Password for the Celery PostgreSQL database             | None                     |
| `PG_CELERY_DATABASE`              | Name of the Celery PostgreSQL database                  | None                     |
| `OTEL_USER`                       | Username for OpenTelemetry backend authentication       | None                     |
| `OTEL_PASSWORD`                   | Password for OpenTelemetry backend authentication       | None                     |
| `MLFLOW_BUCKET_NAME`              | Name of the bucket where MLflow stores artifacts        | `mlflow`                 |
| `DVC_BUCKET_NAME`                 | Name of the bucket used for DVC storage                 | `raw-data`               |
| `CELERY_DATA_HOLDER_BUCKET_NAME`  | Name of the bucket used for data exchange in Celery     | `celery-data-holder`     |
| `MINIO_ACCESS_KEY`                | Access key for MinIO storage                            | None                     |
| `MINIO_SECRET_ACCESS_KEY`         | Secret access key for MinIO storage                     | None                     |
| `MINIO_ROOT_USER`                 | Root username for MinIO                                 | None                     |
| `MINIO_ROOT_PASSWORD`             | Root password for MinIO                                 | None                     |

[All needed environment variables can copied from the file.](.env.example)

## Getting Started

Follow these steps to set up the project:

### Prerequisites

- **Docker**: Ensure Docker is installed on your machine.
- **Docker Compose**: Verify that Docker Compose is available.

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/fhswf-study-projects/mlops-compose-stack.git
   cd mlops-compose-stack
   ```


2. **Set Up Environment Variables**:

   ```bash
   cp .env.example .env
   # Modify the .env file as needed
   ```


3. **Initialize Submodules**:

   ```bash
   git submodule update --init --recursive
   ```


4. **Build and Start Services**:

   ```bash
   docker compose -f compose.yaml -f compose.develop.yaml up --build
   ```

## Project Structure


```plaintext
mlops-compose-stack/
├── .github/
│   └── workflows/
├── collector/
├── configs/
├── .env.example
├── .gitignore
├── .gitmodules
├── Dockerfile.mlflow
├── LICENSE
├── README.md
├── compose.deploy.yaml
├── compose.develop.yaml
├── compose.yaml
└── layout.code-workspace
```


- **`.github/workflows/`**: CI/CD pipeline configurations.
- **`collector/`**: Configuration for OpenTelemetry metrics/logs/traces collectior.
- **`configs/`**: Configuration files for various services.
- **`Dockerfile.mlflow`**: Dockerfile for setting up MLflow.
- **`compose.yaml`**: Primary Docker Compose configuration.
- **`layout.code-workspace`**: VSCode workspace configuration.

## Customization

To tailor the stack to your needs:

- **Modify Services**: Adjust the `compose.yaml` to add or remove services.
- **Update Configurations**: Change settings in the `configs/` directory as required.
- **Extend Functionality**: Incorporate additional tools or scripts in the `collector/` directory.

## Contributing

We welcome contributions! Please fork the repository and submit pull requests for any enhancements or bug fixes.
