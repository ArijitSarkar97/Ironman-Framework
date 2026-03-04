pipeline {
    agent any

    environment {
        VENV = "venv"
        ALLURE_RESULTS = "allure-results"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat """
                python -m venv %VENV%
                """
            }
        }

        stage('Install Dependencies') {
            steps {
                bat """
                %VENV%\\Scripts\\pip install --upgrade pip
                %VENV%\\Scripts\\pip install -r requirements.txt
                """
            }
        }

        stage('Run Pytest with Allure') {
            steps {
                bat """
                %VENV%\\Scripts\\pytest -vs -m pratish --alluredir=%ALLURE_RESULTS%
                """
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: "${ALLURE_RESULTS}"]]
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}