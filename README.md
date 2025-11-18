🚀 Task Manager App – CI/CD with Jenkins, Docker & Kubernetes

A fully automated CI/CD DevOps project integrating:

1.Flask Python backend

2.Docker image build & push (Docker Hub)

3.Jenkins CI/CD Pipeline

4.Kubernetes deployment (Minikube)

5.NodePort service exposure

6.WSL → Windows HTTP forwarding

🏗 Architecture
 
Developer → GitHub → Jenkins → Docker Build → Docker Hub → Deploy to K8s → Minikube → User

⚙️ Technologies Used

1.Python + Flask

2.Docker / Docker Hub

3.Jenkins Pipeline

4.Minikube + kubectl

5.WSL2 (Ubuntu 24.04)

6.Windows PortProxy Forwarding

📦 Docker Commands
Build:
docker build -t nikhil4101/task-app:latest .
Run:
docker run -p 5000:5000 nikhil4101/task-app:latest
Push:
docker push nikhil4101/task-app:latest

🔁 Jenkins CI/CD Pipeline

The Jenkinsfile:

1.Checks out code

2.Builds Docker image

3.Pushes to Docker Hub

4.Deploys to Kubernetes (coming soon)

☸ Kubernetes Deployment
Apply deployment & service:
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

Check pod:
kubectl get pods -n task-app

Expose service:
minikube ip

App URL:
http://<minikube-ip>:30080

💻 Local Dev (WSL → Windows)
Forward port:
netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=5000 connectaddress=172.x.x.x connectport=5000
Test:
http://localhost:5000

💼 Author

Nikhil T N
DevOps Engineer (Fresher)
GitHub: https://github.com/nikhil-codingn-s

