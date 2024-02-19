pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'python --version' // Make sure Python is installed and accessible
                bat 'python -m pip install -r requirements.txt' // Install any required dependencies
                
            }
        }
        
        stage('Test') {
            steps {
                bat 'python -m pytest' // Run tests using pytest
                
            }
        }

        stage('Deploy') {
            steps {
                // Add deployment steps here (e.g., copy files to server, run deployment script)
                bat 'python deploy_script.py'
                
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
