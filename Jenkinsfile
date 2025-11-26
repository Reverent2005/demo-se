pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/reverent2005/demo-se.git'
            }
        }
        stage('Build') {
            steps {
                script {
                    // Assuming you have a requirements.txt file for dependencies
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Run the tests
                    sh 'pytest tests/'
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh 'docker build -t reverent/demo-se:latest .'
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    // Push the Docker image to Docker Hub
                    sh 'docker push reverent/demo-se:latest'
                }
            }
        }
    }
}