pipeline {
    agent {
        label 'HP_Docker_Agent'
    }

    
    environment {
    //   GITLAB_API_TOKEN = credentials('JENKINS_20240327')
      REPO = "https://github.com/PAIA-Playful-AI-Arena/arkanoid.git"
      registry="paiaimagestages.azurecr.io"
      registryCredential_ID="dockerRegistry-Azure-stage"
      
    }

    // tools {
    // }

    stages {

        stage('build'){
            steps {
                echo 'build';
                sh "docker build -t arkanoid:latest -f ./Dockerfile ."
            }
        }
        stage('deploy'){
            steps {
                echo 'deploy';
                docker.withRegistry('https://' + env.registry, env.registryCredential_ID) {

                        sh "docker tag arkanoid:latest ${env.registry}/arkanoid:latest"
                        dockerImage = docker.image("${env.registry}/arkanoid:latest")
                        dockerImage.push()
                }
            }
        }
        
        stage('finish'){
            steps {
                echo 'finish';
            }
        }
        
    }
}
