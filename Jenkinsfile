pipeline {
    agent any

    environment {
        PYTHON = "python3"
        PATH = "/opt/homebrew/bin:${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Setup Virtual Environment') {
            steps {
                sh '''
                    ${PYTHON} -m venv venv
                    source venv/bin/activate
                    ${PYTHON} -m pip install --upgrade pip --break-system-packages
                    ${PYTHON} -m pip install -r requirements.txt
                    ${PYTHON} -m playwright install
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                    source venv/bin/activate
                    ${PYTHON} -m pytest --alluredir=allure-results -n auto
                '''
            }
        }
        stage('Generate Allure Report') {
            steps {
                sh '''
                    source venv/bin/activate
                    allure generate allure-results --clean -o allure-report
                '''
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'allure-results/**'
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}
