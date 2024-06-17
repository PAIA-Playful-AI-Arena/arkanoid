pipeline {
    agent {
        label 'HP_Docker_Agent'
    }
    environment {
        game = 'arkanoid'
        REPO = "https://github.com/PAIA-Playful-AI-Arena/${game}.git"
        registry = 'paiatech'
    }

    stages {
      stage('get the latest tag'){
        steps{
          script {
            def latestTag = sh(
                    script: 'git describe --tags `git rev-list --tags --max-count=1`',
                    returnStdout: true
                ).trim()
            echo "Latest tag: ${latestTag}"

            def fullBranch = env.GIT_BRANCH
            echo "full branch: ${fullBranch}"
            // Extract the branch name
            def branch = fullBranch.replaceFirst('^origin/', '')
            echo "Current branch by replace: ${branch}"

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
                  if (branch == 'main' && env.tag) {
                    sh """docker buildx build --builder=mybuilder --platform linux/amd64,linux/arm64 \
                      -t ${env.registry}/${game}:${env.tag} \
                      -t ${env.registry}/${game}:${env.branch} \
                      -f ./Dockerfile . --push
                      """
                  }else{
                    sh """docker buildx build --builder=mybuilder --platform linux/amd64,linux/arm64 \
                      -t ${env.registry}/${game}:${env.branch} \
                      -f ./Dockerfile . --push
                    """
                  }

                }
            }
        }
        stage('finish') {
            steps {
                echo 'finish'
            }
        }
    }
}
