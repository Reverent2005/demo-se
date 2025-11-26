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
                    // FIX: Export both the current directory (.) and the src directory to PYTHONPATH
                    sh 'export PYTHONPATH=.:src:$PYTHONPATH && . venv/bin/activate && python -m pytest tests/'
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Use the Jenkins Docker Pipeline step for building
                    def dockerImage = docker.build("reverent/demo-se:latest", ".")
                    
                    // Store the image reference for the next stage
                    env.DOCKER_IMAGE = dockerImage.toString() 
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    // Securely log in using stored credentials and push the image
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-creds') {
                        docker.image(env.DOCKER_IMAGE).push() // Use the reference from the previous stage
                    }
                }
            }
        }
    }
}