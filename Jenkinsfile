pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'python --version' // Make sure Python is installed and accessible
                
            }
        }
        
        stage('Test') {
            steps {
                bat 'python example1.py'
                
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded! Your code is built, tested, and deployed successfully.'
        }
        failure {
            echo 'Pipeline failed! Please check the build, test, or deployment logs for errors.'
        }
    }
}
