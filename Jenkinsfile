def pythonList = [
  "py39",
  "py310",
  "py311"
]

pipeline {
  environment {
    projectName = "silverpeak-prometheus"
    githubToken = credentials('githubToken')
    silverpeakOrch = credentials('silverpeak-orch')
    silverpeakToken = credentials('silverpeak-token')
    artifactsRepo = "github.com/ipHeaders/artifacts.git"
  }
    agent any
    options {
        disableConcurrentBuilds()
    }
    stages {
       stage('Building docker image') {
         agent any
         steps{
           script {
            echo "Building ${env.JOB_NAME}..."
            sh 'dir'
            pythonList.each(){
                docker.build("${env.projectName}:${it}","-f ${env.WORKSPACE}/docker/${it}.Dockerfile ${env.WORKSPACE}/docker/") //Docker Pipeline plugin
             }
           }
         }
       }
       stage('testing:py39') {
         agent {
            docker {
              image "${env.projectName}:py39"
              }
            }
         steps{
            sh 'python3 --version'
            sh 'poetry --version'
            sh 'git clone https://$githubToken:x-oauth-basic@$artifactsRepo'
            sh 'poetry install'
            sh ('poetry run spexporter -f $WORKSPACE/artifacts/$projectName/test_vars.yml -k $silverpeakToken -o $silverpeakOrch -d -b')
        }
     }
       stage('testing:py310') {
         agent {
            docker {
              image "${env.projectName}:py310"
              }
            }
         steps{
            sh 'python3 --version'
            sh 'poetry --version'
            sh 'git clone https://$githubToken:x-oauth-basic@$artifactsRepo'
            sh 'poetry install'
            sh ('poetry run spexporter -f $WORKSPACE/artifacts/$projectName/test_vars.yml -k $silverpeakToken -o $silverpeakOrch -d -b')
        }
     }
       stage('testing:py311') {
         agent {
            docker {
              image "${env.projectName}:py311"
              }
            }
         steps{
            sh 'python3 --version'
            sh 'poetry --version'
            sh 'git clone https://$githubToken:x-oauth-basic@$artifactsRepo'
            sh 'poetry install'
            sh ('poetry run spexporter -f $WORKSPACE/artifacts/$projectName/test_vars.yml -k $silverpeakToken -o $silverpeakOrch -d -b')
        }
     }
       stage('Poetry Build') {
         agent {
            docker {
              image 'poetry:latest'
              } 
           }
         steps{
          script {
             sh 'dir'
             sh 'poetry check'
             sh 'poetry build'
             sh 'poetry publish --dry-run'     
           }
         }
       }
     } 
    post {
        success {
            echo 'The build was successful.'
        }
        failure {
            echo 'The build has failed.'
        }
        always {
            echo 'The pipeline has reach the end.'
            cleanWs()
            dir("${env.WORKSPACE}") {
                deleteDir()
            }
        }
   }
}