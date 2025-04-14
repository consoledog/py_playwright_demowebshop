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
                // Create and activate a virtual environment, upgrade pip using the --break-system-packages flag,
                // install the dependencies, and install Playwright browsers.
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
                // Activate the virtual environment and run pytest.
                sh '''
                    source venv/bin/activate
                    ${PYTHON} -m pytest --alluredir=allure-results -n auto
                '''
            }
        }
        stage('Allure Report') {
            steps {
                // Activate the virtual environment if needed, then generate the Allure report.
                // (Adjust this if the allure CLI is installed system-wide.)
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
        }
    }
}