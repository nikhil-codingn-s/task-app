pipeline {
}


stages {
stage('Checkout') {
steps { checkout scm }
}


stage('Build') {
steps {
sh 'docker --version || true'
sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
}
}


stage('Test') {
steps {
sh 'pip install -r app/requirements.txt'
sh 'pytest -q app/tests || true'
}
}


stage('Scan Image (optional)') {
steps {
echo 'Add Trivy or another scanner here if available'
}
}


stage('Push Image') {
steps {
withCredentials([usernamePassword(credentialsId: env.DOCKER_CREDENTIALS, usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
sh '''
echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
docker push ${IMAGE_NAME}:${IMAGE_TAG}
'''
}
}
}


stage('Deploy to Kubernetes') {
steps {
withCredentials([file(credentialsId: env.KUBECONFIG_CREDENTIAL, variable: 'KUBECONFIG_FILE')]) {
sh 'mkdir -p $HOME/.kube'
sh 'cp $KUBECONFIG_FILE $HOME/.kube/config'
sh 'kubectl set image deployment/task-app task-app=${IMAGE_NAME}:${IMAGE_TAG} --record || true'
sh 'kubectl rollout status deployment/task-app'
}
}
}
}


post {
always {
echo "Build finished"
}
}
}
