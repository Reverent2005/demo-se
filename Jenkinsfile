pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/reverent2005/demo-se.git', branch: 'main'
            }
        }
        stage('Build') {
            steps {
                script {
                    sh 'python3 -m venv venv'
                    
                    // 2. Activate the virtual environment and install dependencies
                    // Note: Use 'source venv/bin/activate' on Linux/WSL.
                    // && is used to ensure the next command runs in the activated environment.
                    sh '. venv/bin/activate && pip install -r requirements.txt'

                    // Optional: Deactivate (though the shell exits anyway)
                    // sh 'deactivate' 
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