pipeline {
    agent any
    stages {
        stage('version') {
            steps {
                bat 'python3 --version'
            }
        }
        stage('sum') {
            steps {
                bat 'python3 example1.py'
            }
        }
    }
}
