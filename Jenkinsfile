pipeline {
    agent any

    environment {
        APP_NAME       = "colorful-flask-devops-app"
        DOCKER_REGISTRY = "docker.io"
        DOCKER_IMAGE   = "YOUR_DOCKERHUB_USERNAME/colorful-flask-devops-app"
        DOCKER_TAG     = "${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout') {
            steps {
                echo "Checking out source code..."
                checkout scm
            }
        }

        stage('Build & Test (Python)') {
            steps {
                echo "Running basic application validation..."
                sh '''
                  python3 --version
                  python3 -m py_compile main.py
                  echo "Python syntax check passed"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh '''
                  docker build -t $DOCKER_IMAGE:$DOCKER_TAG .
                  docker tag $DOCKER_IMAGE:$DOCKER_TAG $DOCKER_IMAGE:latest
                '''
            }
        }

        stage('Push Docker Image') {
            environment {
                DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
            }
            steps {
                echo "Pushing image to Docker Hub..."
                sh '''
                  echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
                  docker push $DOCKER_IMAGE:$DOCKER_TAG
                  docker push $DOCKER_IMAGE:latest
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully"
            echo "Docker Image: $DOCKER_IMAGE:latest"
        }
        failure {
            echo "❌ Pipeline failed"
        }
        always {
            sh 'docker logout || true'
        }
    }
}
