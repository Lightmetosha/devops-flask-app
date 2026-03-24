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
                sh 'docker build -t my-flask-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop flask-container || true'
            }
        }

        stage('Remove Old Container') {
            steps {
                sh 'docker rm flask-container || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh '''
                docker run -d -p 5000:5000 --restart always --name flask-container \
                  -e APP_NAME="Lightme Number Game" \
                  -e APP_ENV="production" \
                  -e SECRET_KEY="change-this-secret-key" \
                  my-flask-app
                '''
            }
        }

        stage('Check Running Containers') {
            steps {
                sh 'docker ps'
            }
        }
    }

    post {
        success {
            echo 'Pipeline finished successfully and container deployed'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}
