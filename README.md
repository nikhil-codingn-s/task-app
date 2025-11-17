task-app-devops

A demo Flask Task Management app with a full DevOps pipeline (Jenkins → Docker → Docker Hub → Kubernetes).
This repo contains the application, Dockerfile, Jenkins pipeline, and Kubernetes manifests to build, push, and deploy the app automatically.

Table of contents

1.Overview

2.Architecture

3.Features

4.Tech stack

5.Prerequisites

6.Local run (dev)

7.Build & push (manual)

8.Jenkins CI/CD (pipeline summary)

9.Kubernetes deployment (Minikube)

10.Files & repo structure

11.Troubleshooting

12.Next steps / improvements

13.License

Overview

task-app is a simple Flask-based REST app (task list) used to demonstrate a complete CI/CD pipeline:

1.Build and test with Jenkins

2.Dockerize and push to Docker Hub

3.Deploy to Kubernetes (Minikube) and expose via NodePort/Ingress

This project is meant for learning and for inclusion in your portfolio as a DevOps sample.

Architecture
flowchart LR
  Dev[NIKHIL TN]
  GH[https://github.com/nikhil-codingn-s/task-app]
  Jenkins[Jenkins (CI/CD)]
  DockerLocal[Docker Engine]
  DockerHub[Docker Hub registry]
  Minikube[Minikube Kubernetes]
  Browser[Browser]

  Dev -->|push| GH
  GH -->|webhook / poll| Jenkins
  Jenkins -->|build & test| DockerLocal
  DockerLocal -->|push image| DockerHub
  Jenkins -->|kubectl set-image| Minikube
  Minikube --> Browser

Features

1.Flask REST API (GET /tasks)

2.Dockerized app with multi-stage friendly Dockerfile

3.Jenkins Pipeline (Declarative Jenkinsfile) to build, test, push, and deploy

3.Kubernetes manifests (Deployment + Service)

4.Minikube-ready for local testing

Tech Stack

1.Python (Flask)

2.Docker

3.Jenkins (Pipeline)

4.Kubernetes (Minikube)

5.GitHub

6.Docker Hub

Prerequisites (local)

1.Git

2.Docker (running)

3.Jenkins (optional locally; we used Jenkins in Docker)

4.kubectl

5.minikube


Docker Hub
