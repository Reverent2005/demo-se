pipeline {
    agent any

    environment {
        IMAGE_REPO = 'reverent/demo-se'
        IMAGE_TAG = "${BUILD_NUMBER}" 
        
        GITHUB_CREDS_ID = 'github-creds'
        DOCKERHUB_CREDS_ID = 'dockerhub-creds'
    
        DOCKER_IMAGE_REF = '' 
    }
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
                    
                    sh '. venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh 'export PYTHONPATH=.:src:$PYTHONPATH && . venv/bin/activate && python -m pytest tests/'
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                script {
                    def dockerImage = docker.build("reverent/demo-se:temp", ".")
                    
                    def imageId = dockerImage.id
                    
                    sh "docker tag ${imageId} ${IMAGE_REPO}:latest" 
                    
                    sh "docker tag ${imageId} ${IMAGE_REPO}:${IMAGE_TAG}" 
                    
                    
                    env.DOCKER_IMAGE_REF = "${IMAGE_REPO}:latest" 
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo "Pushing Docker image..."
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    script {
                        sh "docker login -u ${DOCKER_USER} -p ${DOCKER_PASS}"
                        
                        sh "docker push ${IMAGE_REPO}:${IMAGE_TAG}" 
                        sh "docker push ${IMAGE_REPO}:latest"
                        
                        // Log out after use
                        sh "docker logout"
                    }
                }
            }
        }
    }
}