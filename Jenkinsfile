pipeline{
    agent any

    environment{
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-cred')
        IMAGE_NAME = "saks04/weather-sdk"
        TAG = "latest"
    }

    stages{
        stage('Clone Repository'){
            steps{
                echo "Fetching from github⌛"
                git branch: 'main', url:'https://github.com/beri04/Weather_SDK_Saks'
            }
        }
        stage('Verify Docker Version'){
            steps{
                sh 'docker version'
                sh 'docker info'
            }
        }
        stage('Build Docker Image'){
            steps{
                sh 'docker build -t weather_sdk .'
            }
        }
        stage('Run Tests'){
            steps{
                sh 'docker run weather_sdk'
            }
        }
        stage('Login to DockerHub') {
            steps {
                echo "🔐 Logging in to Docker Hub..."
                sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
            }
        }

        stage('Push Docker Image') {
            steps {
                echo "🚀 Pushing image to Docker Hub..."
                sh 'docker push $IMAGE_NAME:$TAG'
            }
        }
    }
    post{
        success{
            echo 'Pipeline Completed successfully!'
        }
        failure{
            echo 'Pipeline failed'
        }
    }
}