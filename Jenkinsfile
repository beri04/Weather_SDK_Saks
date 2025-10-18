pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-cred')
        IMAGE_NAME = "saks04/weather-sdk"
        TAG = "latest"
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo "📥 Cloning Weather SDK repository..."
                git branch: 'main', url: 'https://github.com/beri04/Weather_SDK_Saks.git'
            }
        }

        stage('Verify Docker Setup') {
            steps {
                echo "🔍 Checking Docker version and info..."
                sh 'docker version'
                sh 'docker info'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "🏗️ Building Docker image: $IMAGE_NAME:$TAG ..."
                sh 'docker build -t $IMAGE_NAME:$TAG .'
            }
        }

        stage('Run Tests') {
            steps {
                echo "🧪 Running the image locally for testing..."
                sh 'docker run --rm $IMAGE_NAME:$TAG'
            }
        }

        stage('Login to DockerHub') {
            steps {
                echo "🔐 Logging into Docker Hub..."
                sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
            }
        }

        stage('Push Docker Image') {
            steps {
                echo "🚀 Pushing Docker image to Docker Hub..."
                sh 'docker push $IMAGE_NAME:$TAG'
            }
        }

        stage('Clean Up') {
            steps {
                echo "🧹 Cleaning up local Docker images..."
                sh 'docker rmi $IMAGE_NAME:$TAG || true'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully! Image pushed to Docker Hub → https://hub.docker.com/r/saks04/weather-sdk'
        }
        failure {
            echo '❌ Pipeline failed. Check the logs for details.'
        }
    }
}
