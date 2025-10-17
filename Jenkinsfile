pipeline{
    agent any

    stages{
        stage('Clone Repository'){
            steps{
                git 'https://github.com/beri04/Weather_SDK_Saks'
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