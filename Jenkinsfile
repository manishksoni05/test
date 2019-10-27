pipeline {
    agent any

    stages {
        stage('j1.py') {
            agent any
            steps {
                /root/.jenkins/workspace/test/j1.py
            }
        }
        stage('j2.py') {
            agent any
            steps {
                /root/.jenkins/workspace/test/j1.py
            }
        }
    }
}
