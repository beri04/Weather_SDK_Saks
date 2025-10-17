pipeline{
    agent any

    stages{
        stage('Clone Repository'){
            steps{
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