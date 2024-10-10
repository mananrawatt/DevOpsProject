pipeline {
    agent any

    environment {
        DOCKER_HOME = '/Applications/Docker.app/Contents/Resources/bin'
        PATH = "${DOCKER_HOME}:${env.PATH}"
        
//      DOCKER_IMAGE = "mannanrawat/devops-automation:2.0"
        //DOCKER_IMAGE = "mannanrawat/devops-automation:${env.BUILD_ID.replaceAll('[^a-zA-Z0-9]', '_')}"
        // Sanitize BUILD_ID to remove any characters that are not allowed in Docker image names
        SANITIZED_BUILD_ID = env.BUILD_ID.replaceAll('[^a-zA-Z0-9]', '_')
        DOCKER_IMAGE = "mannanrawat/devops-automation:${SANITIZED_BUILD_ID}"

        DOCKERHUB_USERNAME = "mananrawat788@gmail.com"
        DOCKERHUB_PASSWORD = "docker12@M"
        
        //MINIKUBE_KUBECONFIG_CREDENTIALS = credentials('minikube-kubeconfig')
        MINIKUBE_KUBECONFIG_CREDENTIALS = 'minikube-kubeconfig'

        MINIKUBE_BIN = '/opt/homebrew/bin/minikube'
        KUBECONFIG_FILE = 'kubeconfig'
    }

    tools {
        // Ensure 'Docker' matches the name configured in Jenkins Global Tool Configuration
        dockerTool 'DOCKER_HOME'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }


    stage('Setup') {
            steps {
                sh "chmod +x ${MINIKUBE_BIN}"
                sh "${MINIKUBE_BIN} start --driver=docker"
                sh "${MINIKUBE_BIN} kubectl config use-context minikube"
                script {
                    env.KUBECONFIG = "${env.WORKSPACE}/${KUBECONFIG_FILE}" // Assuming kubeconfig is in the workspace
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build all Docker images in this stage with direct image paths
                    echo "Building Login Service Docker Image"
                    docker.build("mannanrawat/login-service:latest")

                    echo "Building Jenkins Service Docker Image"
                    docker.build("mjenkins/jenkins:lts")

                    echo "Building Kubernetes Service Docker Image"
                    docker.build("mmannanrawat/kubernetes-details:latest")

                    echo "Building Minikube ControllerDocker Image"
                    docker.build("mannanrawat/minikube-controller:latest")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // // Login to Docker Hub
                     sh "echo ${DOCKERHUB_PASSWORD} | docker login -u ${DOCKERHUB_USERNAME} --password-stdin"
                     sh "docker build -t ${DOCKER_IMAGE} ."

                    // // Push the image
                    // // docker.image("${DOCKER_IMAGE}:${env.BUILD_ID}").push()
                    // // docker.image("${DOCKER_IMAGE}:${env.BUILD_ID}").push('latest')

                    // // Push the image with the build ID tag
                    // docker.image(DOCKER_IMAGE).push()

                    // // Push the image with the 'latest' tag
                    // docker.image("mannanrawat/devops-automation:latest").push()
                    
                    // // Login to Docker Hub
                    // sh "echo ${DOCKERHUB_PASSWORD} | ${dockerHome}/docker login -u ${DOCKERHUB_USERNAME} --password-stdin"

                    // // Push the image
                    // sh "${dockerHome}/docker push ${DOCKER_IMAGE}"
                    // sh "${dockerHome}/docker tag ${DOCKER_IMAGE} mannanrawat/devops-automation:latest"
                    // sh "${dockerHome}/docker push mannanrawat/devops-automation:latest"



                    // Push the image with build ID tag
                    sh "docker push ${DOCKER_IMAGE}"

                    // // Optionally tag and push as 'latest'
                    // sh "docker tag ${DOCKER_IMAGE} mananrawat/devops-automation:latest"
                    // sh "docker push mananrawat/devops-automation:latest"
                    
                }
            }
        }

        // stage('Test Connectivity to Minikube') {
        //     steps {
        //         script {
        //             env.KUBECONFIG = "${env.WORKSPACE}/${KUBECONFIG_FILE}"
        //             withEnv(["KUBECONFIG=${env.KUBECONFIG}"]) {
        //                 try {
        //                     sh "kubectl cluster-info"
        //                     sh "kubectl get nodes"
        //                 } catch (Exception e) {
        //                     echo "Error accessing Minikube: ${e.message}"
        //                     currentBuild.result = 'FAILURE'
        //                     error("Failed to connect to Minikube")
        //                 }
        //             }
        //         }
        //     }
        // }

        // stage('Deploy to Kubernetes') {
        //     steps {
        //         script {
        //             kubernetesDeploy(
        //             configs: 'k8s/deployment.yaml',
        //             kubeconfigId: 'kubeconfig'
        
        // stage('Deploy to Minikube') {
        //     steps {
        //         script {
        //             withKubeConfig([credentialsId: 'MINIKUBE_KUBECONFIG_CREDENTIALS']) {
        //                 sh 'kubectl apply -f k8s/deployment.yaml'

        // stage('Deploy to Kubernetes') {
        //     steps {
        //         withKubeConfig([credentialsId: env.KUBECONFIG_CREDENTIAL_ID, serverUrl: 'https://127.0.0.1:52582']) {
        //             sh 'kubectl apply -f k8s/deployment.yaml'
                    
        //         }
        //     }
        // }

        
        // stage('Deploy to Minikube') {
        //     steps {
        //         script {
        //             withKubeConfig([credentialsId: 'minikube-kubeconfig']) {
        //                 try {
        //                     sh "kubectl apply -f k8s/deployment.yaml --validate=false"
        //                     sh "kubectl apply -f k8s/service.yaml --validate=false"
        //                 } catch (Exception e) {
        //                     echo "Error deploying: ${e.message}"
        //                     currentBuild.result = 'FAILURE'
        //                     error("Deployment failed")
        //                 }
        //             }
        //         }
        //     }
        // }

        // stage('Deploy to Minikube') {
        //     steps {
        //         script {
        //             env.KUBECONFIG = "${env.WORKSPACE}/${KUBECONFIG_FILE}"
        //             withEnv(["KUBECONFIG=${env.KUBECONFIG}"]) {
        //                 try {
        //                     sh "kubectl apply -f k8s/deployment.yaml --validate=false"
        //                     sh "kubectl apply -f k8s/service.yaml --validate=false"
        //                 } catch (Exception e) {
        //                     echo "Error deploying: ${e.message}"
        //                     currentBuild.result = 'FAILURE'
        //                     error("Deployment failed")
        //                 }
        //             }
        //         }
        //     }
        // }

        stage('Manual Approval for Deployment') {
            steps {
                input message: 'Do you want to deploy manually? Click Proceed to continue.', ok: 'Proceed'
            }
        }

        stage('Manual Deployment') {
            steps {
                script {
                    echo "Deploy the application manually at this point."
                    echo "This can include any manual steps like copying files, running deployment scripts, etc."
                    // Add instructions or shell commands here for manual deployment if necessary
                    echo "Once manual deployment is done, you can continue."
                }
            }
        }
    
    


        stage('Run Backup Script') {
            steps {
                script {
                    sh './scripts/backup.sh'
                }
            }
        }

        stage('Run Cleanup Script') {
            steps {
                script {
                    sh './scripts/cleanup.sh'
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}

