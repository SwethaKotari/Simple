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
                bat 'python example1.py'
            }
        }
    }
}
