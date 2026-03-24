pipeline {
    agent any

    stages {
        stage('Clone Info') {
            steps {
                echo 'Starting Jenkins pipeline from repository'
            }
        }

        stage('List Files') {
            steps {
                sh 'ls -la'
            }
        }

        stage('Check Docker') {
            steps {
                sh 'docker --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t jenkins-flask-app .'
            }
        }

        stage('Show Images') {
            steps {
                sh 'docker images | head'
            }
        }
    }

    post {
        success {
            echo 'Pipeline finished successfully'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}