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