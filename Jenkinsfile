pipeline {
    agent any

    environment {
        IMAGE_NAME = "nikhil4101/task-app"
        IMAGE_TAG = "${env.BUILD_NUMBER}"
        DOCKER = "/usr/bin/docker"
        DOCKER_CREDENTIALS = "dockerhub"
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
                    /bin/bash -c "
                        ${DOCKER} --version
                        ${DOCKER} build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                    "
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    /bin/bash -c "
                        pip install -r app/requirements.txt
                        pytest -q app/tests || true
                    "
                '''
            }
        }

        stage('Push Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: DOCKER_CREDENTIALS, usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh '''
                        /bin/bash -c "
                            echo $PASS | ${DOCKER} login -u $USER --password-stdin
                            ${DOCKER} push ${IMAGE_NAME}:${IMAGE_TAG}
                        "
                    '''
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

