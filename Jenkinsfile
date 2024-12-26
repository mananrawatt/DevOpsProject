pipeline {
    agent any

    environment {

        JAVA_HOME = '/opt/homebrew/opt/openjdk@17/libexec/openjdk.jdk/Contents/Home'
        // PATH = "${JAVA_HOME}/bin:${env.PATH}"

        
        DOCKER_HOME = '/Applications/Docker.app/Contents/Resources/bin'
        // PATH = "${DOCKER_HOME}:${env.PATH}"
        PATH = "${DOCKER_HOME}:${JAVA_HOME}:${SONAR_SCANNER_HOME}:${env.PATH}"
        // PATH = "${DOCKER_HOME}:${JAVA_HOME}:${SONAR_SCANNER_HOME}::/opt/homebrew/bin:${env.PATH}" -> by this all the paths at once were given

        ANSIBLE_HOME = '/opt/homebrew/bin:${env.PATH}'
        
//      DOCKER_IMAGE = "mannanrawat/devops-automation:2.0"
        //DOCKER_IMAGE = "mannanrawat/devops-automation:${env.BUILD_ID.replaceAll('[^a-zA-Z0-9]', '_')}"
        
        // Sanitize BUILD_ID to remove any characters that are not allowed in Docker image names
        SANITIZED_BUILD_ID = env.BUILD_ID.replaceAll('[^a-zA-Z0-9]', '_')
        DOCKER_IMAGE = "mannanrawat/devops-automation:${SANITIZED_BUILD_ID}"

        DOCKERHUB_USERNAME = "mananrawat788@gmail.com"
        DOCKERHUB_PASSWORD = "docker12@M"

        versionTag = "v${env.BUILD_NUMBER}"  // Dynamically create a version tag using Jenkins' build number
        
        //MINIKUBE_KUBECONFIG_CREDENTIALS = credentials('minikube-kubeconfig')
        MINIKUBE_KUBECONFIG_CREDENTIALS = 'minikube-kubeconfig'

        MINIKUBE_BIN = '/opt/homebrew/bin/minikube'
        KUBECONFIG_FILE = 'kubeconfig'

        //Minikube token to maintain connectivity
        MINIKUBE_TOKEN = credentials('MINI_JEN_TOKEN')

        //SONAR-QUBE
        SONAR_TOKEN = credentials('SonarQubeToken')
        // SQ-PATH = "$PATH:/opt/homebrew/opt/sonar-scanner/bin"
    }

    tools {
        // Ensure 'Docker' matches the name configured in Jenkins Global Tool Configuration
        dockerTool 'DOCKER_HOME'
    }

    stages {
        stage('Checkout') {
            steps {
                // checkout scm
                git branch: 'development',
                    url: 'https://github.com/mananrawatt/DevOpsProject.git'

                 // Output the current branch using git
                echo "------------------------------------------"
                sh 'git branch'
                echo "------------------------------------------"
            }
        }



        // stage('Run Ansible Playbook') {
        //     steps {
        //         script {
        //             sh '''
        //                 cd "/Users/mananrawat/Desktop/Project/UPDATED CODEE/DevOpsProject/Ansible"
        //                 ${ANSIBLE_HOME} -i inventory.ini start_sonaq.yml
        //             '''
        //             }
        //         }
        //     }
        


        
        stage('Check Java Version') {
            steps {
                sh 'java -version' // Check the Java version
            }
        }
        stage('Check Ansible Version') {
            steps {
                // withEnv(['ANSIBLE_CONFIG=/Users/mananrawat/.ansible.cfg']) {
                // sh '/opt/homebrew/bin/ansible --version' // Check the Ansible version
                // sh 'which ansible'
                // sh 'ansible --version'
                script {
                    // Use ANSIBLE_HOME for the specific step requiring Ansible, means for this particular stage we have configured this
                    withEnv(["PATH=${ANSIBLE_HOME}"]) {
                        // Run your commands that require ansible
                        sh 'which ansible'  // This should now correctly find ansible
                    }
                }
            }
        }

        stage('Connect to Minikube') {
            steps {
                script {
                    sh "kubectl config set-credentials mini-jen --token=${MINIKUBE_TOKEN}"
                    echo "------------------------------------------"
                    echo "Connectivity Succesfully Achieved!!"
                    echo "------------------------------------------"
                }
            }
        }

        stage('Cluster Details'){
            steps{
                script{
                    sh '''
                        echo "------------------------------------------"
                        kubectl version
                        echo "------------------------------------------"
                        kubectl cluster-info
                        echo "------------------------------------------"
                    '''
                }
            }
        }

        stage('Status of Nodes & Pods'){
            steps{
                script{
                    sh '''
                    echo "------------------------------------------"
                    echo "------------------------------------------"
                        kubectl get no
                        echo "------------------------------------------"
                        kubectl get ns
                        echo "------------------------------------------"
                        kubectl get po
                        echo "------------------------------------------"
                        kubectl get deploy
                        echo "------------------------------------------"
                        echo "------------------------------------------"
                    '''
                }
            }
        }
        
    

        stage('Setup') {
                steps {
                //     sh "chmod +x ${MINIKUBE_BIN}"
                //     sh "${MINIKUBE_BIN} start --driver=docker"
                //     sh "${MINIKUBE_BIN} kubectl config use-context minikube"
                //     script {
                //         env.KUBECONFIG = "${env.WORKSPACE}/${KUBECONFIG_FILE}" // Assuming kubeconfig is in the workspace
                //     }
                // }
                     withCredentials([file(credentialsId: 'minikube-kubeconfig', variable: 'KUBECONFIG_FILE')]) {
                        sh "chmod +x ${MINIKUBE_BIN}"
                        sh "${MINIKUBE_BIN} start --driver=docker"
                        sh "export KUBECONFIG=${KUBECONFIG_FILE}"
                        sh "${MINIKUBE_BIN} kubectl config use-context minikube"
                     }
                
                }
            }
        stage('Initialize') {
            steps {
                script {
                    // Dynamically create a version tag using Jenkins' build number
                    //def versionTag = "v${env.BUILD_NUMBER}"  // This ensures the tag is unique and increments with each build
                    echo "Generated Version Tag: ${versionTag}"  // For debugging purposes
                }
            }
        }


        // stage('Run Ansible Playbook') {
        //     steps {
        //         script {
        //             dir('/Users/mananrawat/Desktop/Project/UPDATED CODEE/DevOpsProject/Ansible') {
        //             // Run the Ansible playbook
        //             sh 'ansible-playbook -i inventory.ini start_sonaq.yml'
        //             // // Execute the Ansible playbook
        //             // sh '''
        //             //     ansible-playbook -i inventory.ini start_sonaq.yml
        //             // '''
        //             }
        //         }
        //     }
        // }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // Build all Docker images in this stage with direct image paths
                    echo "Building Login Service Docker Image"
                    docker.build("mannanrawat/login-service:${versionTag}")

                    echo "Building Jenkins Service Docker Image"
                    docker.build("mannanrawat/jenkins-service:lts-${versionTag}")

                    echo "Building Kubernetes Service Docker Image"
                    docker.build("mannanrawat/kubernetes-details:${versionTag}")

                    echo "Building Minikube Controller Docker Image"
                    docker.build("mannanrawat/minikube-controller:${versionTag}")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                     // Login to Docker Hub
                    sh "echo ${DOCKERHUB_PASSWORD} | docker login -u ${DOCKERHUB_USERNAME} --password-stdin"
                    
                    // Push all Docker images in this stage
                    echo "Pushing Login Service Docker Image"
                    sh "docker push mannanrawat/login-service:${versionTag}"
                    
                    echo "Pushing Jenkins Service Docker Image"
                    sh "docker push mannanrawat/jenkins-service:lts-${versionTag}"

                    echo "Pushing Kubernetes Service Docker Image"
                    sh "docker push mannanrawat/kubernetes-details:${versionTag}"

                    echo "Pushing Minikube Controller Service Docker Image"
                    sh "docker push mannanrawat/minikube-controller:${versionTag}"
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    withSonarQubeEnv('SonarQube') {
                        // Set JAVA_HOME explicitly if needed
                        env.JAVA_HOME = '/opt/homebrew/opt/openjdk@17/libexec/openjdk.jdk/Contents/Home'
                
                        // Ensure the path to the sonar-scanner is included
                        sh """
                        export PATH=/opt/homebrew/opt/sonar-scanner/bin:\$PATH
                        echo "JAVA_HOME is set to: \$JAVA_HOME"
                        echo "Current Java version:"
                        java -version
                        sonar-scanner --version
                        sonar-scanner \
                            -Dsonar.projectKey=DevOpsPythonProject \
                            -Dsonar.host.url=http://localhost:9000 \
                            -Dsonar.login=\${SONAR_TOKEN}
                        """
                    }
                }
            }
        }

        
        stage('Manual Approval for Deployment') {
            steps {
                input message: 'Do you want to deploy manually? Click Proceed to continue.', ok: 'Proceed'
            }
        }
    
        stage('Deployment') {
            steps {
                script {
                    echo "Current Working Directory: ${env.WORKSPACE}"
                    echo "KUBECONFIG: ${env.KUBECONFIG}"
                
                    // Check if the YAML file exists
                    sh '''
                        ls -l "/Users/mananrawat/Desktop/Project/UPDATED CODEE/DevOpsProject/Deployment/jenkins.yaml"
                    '''

                      // Check if namespace exists or create it
                    sh '''
                        kubectl get ns main  
                    '''
            
                    // Set the Kubernetes context if necessary
                    sh 'kubectl config use-context minikube'
                    echo "------------------STARTING DEPLOYMENT-------------------"
                        sh '''
                            kubectl apply -f "/Users/mananrawat/Desktop/Project/UPDATED CODEE/DevOpsProject/Deployment"/jenkins.yaml --namespace=main   --validate=false
                        '''

                    echo "------------------DEPLOYMENT SUCCESSFUL-------------------"
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
            // script {
            //     // Capture build log and send to Elasticsearch
            //     def buildLog = currentBuild.rawBuild.getLog(1000).join('\n')
            //     sendLogToElasticsearch(buildLog)
            // }
        }
    }
}
// Custom function to send logs to Elasticsearch
// def sendLogToElasticsearch(logData) {
//     httpRequest httpMode: 'POST',
//                 contentType: 'APPLICATION_JSON',
//                 requestBody: """
//                     {
//                         "timestamp": "${new Date().format("yyyy-MM-dd'T'HH:mm:ss'Z'", TimeZone.getTimeZone('UTC'))}",
//                         "job": "${env.JOB_NAME}",
//                         "build_number": ${env.BUILD_NUMBER},
//                         "status": "${currentBuild.currentResult}",
//                         "message": "${logData.replaceAll('"', '\\"')}"
//                     }
//                 """,
//                 url: 'https://localhost:9200/jenkins-pipeline-logs/_doc'
// }
