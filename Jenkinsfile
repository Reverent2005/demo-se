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
                echo "Building Docker image..."
                script {
                    // FIX: Use the Jenkins Docker Pipeline step for robust building in WSL
                    // Use a generic image name/tag for the build reference
                    def dockerImage = docker.build("reverent/demo-se:temp", ".")
                    
                    // Tag the built image with the desired names
                    dockerImage.tag("${IMAGE_REPO}:${IMAGE_TAG}")
                    dockerImage.tag("${IMAGE_REPO}:latest")
                    
                    // Store the image reference for the next stage
                    env.DOCKER_IMAGE_REF = dockerImage.toString() 
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo "Pushing Docker image..."
                script {
                    // FIX: Use secure registry wrapper and built image reference
                    docker.withRegistry('https://registry.hub.docker.com', DOCKERHUB_ID) {
                        docker.image(env.DOCKER_IMAGE_REF).push("${IMAGE_REPO}:${IMAGE_TAG}")
                        docker.image(env.DOCKER_IMAGE_REF).push("${IMAGE_REPO}:latest")
                    }
                }
            }
        }
    }
}