# Accuknox-app-deployment-and-scripts
Accuknox DevOps Trainee Practical Assessment
Overview

This repository contains solutions for the Accuknox DevOps Trainee Practical Assessment. It demonstrates containerization, Kubernetes deployment, CI/CD automation, and system/application health monitoring. The project also includes an optional zero-trust security policy implementation using KubeArmor.

The assessment is divided into three problem statements:

Problem Statement 1: Containerization & Kubernetes Deployment of Wisecow Application

Objective:
Containerize and deploy the Wisecow application
 on a Kubernetes cluster (Kind/Minikube) with secure TLS communication and implement CI/CD automation.

Deliverables:

Dockerfile for building the Wisecow application image.

Kubernetes manifest files for deployment, service exposure, and TLS configuration.

GitHub Actions workflow for automated build, push, and deployment of Docker images.

End-to-end deployment of the Wisecow app accessible over HTTPS.

Problem Statement 2: Automation Scripts

Two Python/Bash scripts have been implemented for monitoring and automation:

Application Health Checker

Monitors the uptime and HTTP status of specified applications.

Detects if the application is up or down.

Logs results with timestamps.

System Health Monitoring Script

Monitors CPU usage, memory usage, disk space, and running processes.

Sends console alerts when metrics exceed defined thresholds.

Optional scripts such as automated backup or log analysis can also be added for extended functionality.

Problem Statement 3: Zero-Trust KubeArmor Policy (Optional)

Objective:

Implement a zero-trust security policy for the Kubernetes workload deployed in Problem Statement 1 using KubeArmor
.

Enforce access restrictions and monitor policy violations.

Capture and store screenshots of policy violations for validation.

Deliverables:

KubeArmor policy YAML file.

Screenshot showcasing detected policy violations.

Technologies Used

Containerization: Docker

Orchestration: Kubernetes (Minikube/Kind)

CI/CD: GitHub Actions

Monitoring & Security: Python, KubeArmor

TLS: HTTPS secure communication for Wisecow application
