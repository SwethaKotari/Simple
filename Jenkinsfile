pipeline {
    agent any
    stages {
        stage('version') {
            steps {
                bat 'python --version'
            }
        }
        stage('sum') {
            steps {
                bat 'python3 example1.py'
            }
        }
    }
}
