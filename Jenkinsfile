pipeline {
    agent any

    environment {
        // Define repository name and tag variables
        IMAGE_REPO = 'reverent/demo-se'
        IMAGE_TAG = "${BUILD_NUMBER}" // Use Jenkins' built-in BUILD_NUMBER
        
        // Define credential IDs (assuming these IDs are set in Jenkins Credentials Manager)
        GITHUB_CREDS_ID = 'github-creds'
        DOCKERHUB_CREDS_ID = 'dockerhub-creds'
        
        // This variable will hold the reference to the built image (set in the script block)
        DOCKER_IMAGE_REF = '' 
    }
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
                    // FIX: Use the dedicated Jenkins Docker Pipeline step
                    def dockerImage = docker.build("reverent/demo-se:temp", ".")
                    
                    // Tag and store the reference (using your previous logic structure)
                    dockerImage.tag("${IMAGE_REPO}:latest")
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