6. Runtime View
============================

**Prediction and Feedback**


.. mermaid::

    sequenceDiagram
        participant User
        participant Streamlit UI
        participant FastAPI Backend
        participant Data Processor
        participant MLflow
        participant Prometheus
        participant Grafana
        participant MinIO

        Data Processor ->> MLflow: First training and versioning the model
        Data Processor ->> MinIO: Versioning training data and all steps
        User ->> Streamlit UI: Enter input data
        Streamlit UI ->> FastAPI Backend: Send request
        FastAPI Backend ->> Data Processor: Forward request
        Data Processor ->> MLflow: Fetch latest model
        MLflow -->> Data Processor: Return model
        Data Processor ->> Data Processor: Preprocess and predict
        Data Processor -->> FastAPI Backend: Return prediction
        FastAPI Backend -->> Streamlit UI: Send response
        Streamlit UI -->> User: Display prediction

        User ->> Streamlit UI: Provide feedback (correct/incorrect)
        Streamlit UI ->> FastAPI Backend: Send feedback data
        FastAPI Backend ->> Prometheus: Send feedback data to Prometheus
        Prometheus -->> Grafana: Track and visualize feedback metrics
        Grafana ->> FastAPI Backend: Feedback if threshold reached via webhook
        FastAPI Backend ->> Data Processor: Retrain model if threshold met
        Data Processor ->> MinIO: Versioning new training data and all steps
        Data Processor ->> MLflow: Log new model version
        MLflow -->> Data Processor: Save new model version


This scenario describes how a user interacts with the system via the Streamlit UI to request a machine learning prediction.
The User give also a feedback, if the prediction was right or not.

**Prediction Interaction**

#. The user inputs data via the Streamlit UI.
#. The Streamlit UI sends the request to the FastAPI backend.
#. The FastAPI backend forwards the request to the Data Processor.
#. The Data Processor loads the latest model from MLflow.
#. The Data Processor preprocesses the data and performs inference.
#. The prediction is returned to the FastAPI backend.
#. The FastAPI backend sends the prediction result back to the Streamlit UI.
#. The user sees the predicted result.

**Feedback Interaction**

#. After receiving the prediction, the user provides feedback (correct or incorrect) through the Streamlit UI.
#. The feedback is sent to FastAPI via the backend, which forwards it to Prometheus.
#. Prometheus collects feedback metrics (e.g., accuracy) and monitors them.
#. Grafana visualizes the feedback and tracks the metrics over time, monitoring whether the threshold is met
   (for example, if the accuracy drops below a certain threshold). Grafana also send a webhook to the API,
   if the threshold met a specific value.
#. Threshold Detection: If the feedback threshold is reached (for example, if a certain number of incorrect predictions occur),
   Prometheus alerts the system, triggering model retraining.
#. Retraining the Model: The Data Processor retrains the model and logs the new model version in MLflow.