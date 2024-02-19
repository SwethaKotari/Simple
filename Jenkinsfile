pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'python3 --version' // Make sure Python is installed and accessible
                bat 'python3 -m pip install -r requirements.txt' // Install any required dependencies
                
            }
        }
        
        stage('Test') {
            steps {
                bat 'python3 -m pytest' // Run tests using pytest
                
            }
        }

        stage('Deploy') {
            steps {
                // Add deployment steps here (e.g., copy files to server, run deployment script)
                bat 'python3 deploy_script.py'
                
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
