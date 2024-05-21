pipeline {
    agent {
        label 'HP_Docker_Agent'
    }

    
    environment {
    //   GITLAB_API_TOKEN = credentials('JENKINS_20240327')
      REPO = "https://github.com/PAIA-Playful-AI-Arena/arkanoid.git"
      
      
    }

    // tools {
    // }

    stages {
        stage('begin'){
            steps {
                echo 'begin';
                // deleteDir();
                sh 'ls -al';
            }
        }

        stage('checkout') {
            steps {
                script {
                    echo 'checkout'
                }
            }
        }
        stage('build'){
            steps {
                echo 'build';
            }
        }
        stage('deploy'){
            steps {
                echo 'deploy';
            }
        }
        
        stage('finish'){
            steps {
                echo 'finish';
            }
        }
        
    }
}
