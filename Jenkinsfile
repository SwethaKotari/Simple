pipeline {
    agent any
    stages {
        stage('version') {
            steps {
                bat 'python --version'
            }
        }
        stage('Bulid') {
            steps {
                bat 'python example1.py'
            }
        }
    }
}
