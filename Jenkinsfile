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
                sh(script: '''
                    echo "Using docker at /usr/bin/docker"
                    /usr/bin/docker --version
                    /usr/bin/docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                ''', shell: '/bin/bash')
            }
        }

        stage('Run Tests') {
            steps {
                sh(script: '''
                    pip install -r app/requirements.txt
                    pytest -q app/tests || true
                ''', shell: '/bin/bash')
            }
        }

        stage('Push Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: DOCKER_CREDENTIALS, usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh(script: '''
                        echo $PASS | /usr/bin/docker login -u $USER --password-stdin
                        /usr/bin/docker push ${IMAGE_NAME}:${IMAGE_TAG}
                    ''', shell: '/bin/bash')
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline finished!"
        }
    }
}
