pipeline {
    agent any
    stages {
        stage('version') {
            steps {
                echo 'Buliding'
            }
        }
        stage('sum') {
            steps {
                bat 'python3 example1.py'
            }
        }
    }
}
