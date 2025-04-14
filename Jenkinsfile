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
        stage('Install Dependencies') {
            steps {
                sh "${env.PYTHON} -m pip install --upgrade pip"         // Upgrade python package manager
                sh "${env.PYTHON} -m pip install -r requirements.txt"   // Install all libs from requirments.txt
                sh "${env.PYTHON} -m playwright install"                // Install Playwright browsers
            }
        }
        stage('Run Tests') {
            steps {
                sh "${env.PYTHON} -m pytest --alluredir=allure-results -n auto"
            }
        }
        stage('Allure Report') {
            steps {
                sh "allure generate allure-results --clean -o allure-report"
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'allure-results/**'
        }
    }
}
