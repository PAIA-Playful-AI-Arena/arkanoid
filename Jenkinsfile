pipeline {
    agent {
        label 'HP_Docker_Agent'
    }
    environment {
        game = 'arkanoid'
        REPO = "https://github.com/PAIA-Playful-AI-Arena/${game}.git"
        registry = 'ghcr.io/paia-playful-ai-arena'
    }

    // tools {
    // }

    stages {
      stage('get the latest tag'){
        steps{
          script {


                    def latestTag = sh(
                            script: 'git describe --tags `git rev-list --tags --max-count=1`',
                            returnStdout: true
                        ).trim()
                    echo "Latest tag: ${latestTag}"
                    // Store the latest tag in an environment variable
                    env.LATEST_TAG = latestTag
                }
        }
      }
      stage('build and deploy') {
            steps {
                echo 'build'
                script {
                  sh    "docker buildx ls"
                  sh """docker buildx build --builder=container --platform linux/amd64,linux/arm64 \
                    -t ${env.registry}/${game}:${env.LATEST_TAG} \
                    -f ./Dockerfile . --push
                  """
                }
                // sh "docker build -t ${game}:${env.LATEST_TAG} -f ./Dockerfile ."
            }
        }
        stage('finish') {
            steps {
                echo 'finish'
            }
        }
    }
}
