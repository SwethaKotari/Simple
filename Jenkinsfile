pipeline {
    agent any
    stages {
        stage('version') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('sum') {
            steps {
                sh 'python3 example1.py'
            }
        }
    }
}
