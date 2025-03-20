10. Quality Requirements
============================

This chapter defines the quality attributes that the system must meet.
These requirements ensure the system is reliable, maintainable, performant,
and secure, supporting both University and technical needs.
There are now concrete quality requirements for this project.

.. list-table:: Quality Attributes
   :header-rows: 1
   :widths: 20 80 20

   * - **Quality Attribute**
     - **Description**
     - **Priority (High, Medium, Low)**
   * - Performance
     - The system must handle high-concurrency workloads and provide fast response times.
     - High
   * - Scalability
     - The architecture must scale horizontally and vertically to support growing workloads.
     - High
   * - Availability
     - The system should have high uptime, minimizing service disruptions.
     - High
   * - Security
     - Data access must be controlled and encrypted.
     - High
   * - Maintainability
     - The system must support continuous integration and automated deployments for easy updates.
     - Medium
   * - Observability
     - Logs, metrics, and traces must be collected for real-time monitoring and debugging.
     - Medium
   * - Usability
     - The user-facing components (Streamlit UI, API) should be intuitive and easy to use.
     - Medium
