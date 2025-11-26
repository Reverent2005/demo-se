pipeline {
    agent any

    // Define credentials securely using the IDs created in Jenkins
    environment {
        // Use an ID for the username to reference the credentials later
        DOCKERHUB_ID = 'dockerhub-creds'
        IMAGE_REPO = 'reverent/demo-se'
        IMAGE_TAG_BUILD = "${IMAGE_REPO}:${BUILD_NUMBER}"
        IMAGE_TAG_LATEST = "${IMAGE_REPO}:latest"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Pulling code from GitHub..."
                // Use the credentials ID defined in the job/environment
                git branch: 'main',
                    url: 'https://github.com/Reverent2005/demo-se.git',
                    credentialsId: 'github-creds'
            }
        }

        stage('Build - Install & Test') {
            steps {
                echo "Setting up Python virtual environment and running tests..."
                // Use 'sh' for Linux/WSL environment
                // Use '.' to activate Venv and 'src' in PYTHONPATH for correct imports
                sh """
                    # 1. Setup Venv and install dependencies
                    python3 -m venv venv
                    . venv/bin/activate && pip install --upgrade pip
                    . venv/bin/activate && pip install -r requirements.txt
                    
                    # 2. Run Tests with Venv active and 'src' path set
                    export PYTHONPATH=.:src:\$PYTHONPATH
                    . venv/bin/activate && python -m pytest tests/ -v
                """
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                script {
                    // FIX: Use the Jenkins Docker Pipeline step for robust building in WSL
                    def dockerImage = docker.build("${IMAGE_REPO}:${IMAGE_TAG}", ".") // Note: Use the variable name from your environment block
                    
                    // Tag the image with the 'latest' tag
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
                        docker.image(env.DOCKER_IMAGE_REF).push() // Pushes all tags associated with the image reference
                    }
                }
            }
        }

        stage('Verify Docker Image') {
            steps {
                // Check local images for verification (uses 'sh' command)
                sh "docker images | grep ${IMAGE_REPO}"
            }
        }
    }

    post {
        success {
            echo "✓ Pipeline completed successfully!"
        }
        failure {
            echo "✗ Pipeline failed!"
        }
        always {
            cleanWs()
        }
    }
}