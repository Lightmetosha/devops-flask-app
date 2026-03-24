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

        stage('Show Branch') {
            steps {
                sh 'git branch || true'
            }
        }

        stage('Check Python') {
            steps {
                sh 'python3 --version || true'
            }
        }

        stage('Show App File') {
            steps {
                sh 'head -n 20 app.py'
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
