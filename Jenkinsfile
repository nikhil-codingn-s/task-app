pipeline {
    agent any

    environment {
        IMAGE_NAME = "nikhil4101/task-app"
        IMAGE_TAG = "${env.BUILD_NUMBER}"
        DOCKER_CREDENTIALS = 'dockerhub'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    export PATH=$PATH:/usr/bin:/usr/local/bin
                    docker --version
                    docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    export PATH=$PATH:/usr/bin:/usr/local/bin
                    pip install -r app/requirements.txt
                    pytest -q app/tests || true
                '''
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: DOCKER_CREDENTIALS, usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh '''
                        export PATH=$PATH:/usr/bin:/usr/local/bin
                        echo $PASS | docker login -u $USER --password-stdin
                        docker push ${IMAGE_NAME}:${IMAGE_TAG}
                    '''
                }
            }
        }

        stage('Deploy (Coming Soon)') {
            steps {
                echo "Kubernetes deployment step will be added later"
            }
        }
    }

    post {
        always {
            echo "Pipeline finished!"
        }
    }
}

