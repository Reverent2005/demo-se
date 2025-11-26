pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Ensure the correct branch is checked out
                git url: 'https://github.com/reverent2005/demo-se.git', branch: 'main'
            }
        }
        stage('Build') {
            steps {
                script {
                    // Create the virtual environment
                    sh 'python3 -m venv venv'
                    
                    // Activate the Venv and install dependencies in one command
                    sh '. venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // CRITICAL FIX: Activate Venv and run tests in the same command
                    sh '. venv/bin/activate && pytest tests/'
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