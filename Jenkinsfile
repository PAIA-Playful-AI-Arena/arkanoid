pipeline {
    agent {
        label 'HP_Docker_Agent'
    }
    environment {
        game = 'arkanoid'
        REPO = "https://github.com/PAIA-Playful-AI-Arena/${game}.git"
        registry = 'paiatech'
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
            def branch = sh(
                script:'git branch --show-current',
                returnStdout: true
              ).trim()
            echo "Latest tag: ${latestTag}"
            echo "Current branch: ${branch}"

            // Store the latest tag in an environment variable
            env.tag = latestTag
            env.branch = branch
                }
        }
      }
      stage('build and deploy') {
            steps {
                echo 'build'
                script {
                  sh "docker buildx ls"
                  sh """docker buildx build --builder=mybuilder --platform linux/amd64,linux/arm64 \
                    -t ${env.registry}/${game}:${env.tag} \
                    -t ${env.registry}/${game}:${env.branch} \
                    -f ./Dockerfile . --push
                  """
                }
                // sh "docker build -t ${game}:${env.tag} -f ./Dockerfile ."
            }
        }
        stage('finish') {
            steps {
                echo 'finish'
            }
        }
    }
}
