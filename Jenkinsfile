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
                script {
                    if (isUnix()) {
                        sh "python3 -m venv ${VENV}"
                    } else {
                        bat "python -m venv %VENV%"
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    if (isUnix()) {
                        sh """
                        source ${VENV}/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                        """
                    } else {
                        bat """
                        ${VENV}\\Scripts\\pip install --upgrade pip
                        ${VENV}\\Scripts\\pip install -r requirements.txt
                        """
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                %VENV%\\Scripts\\pytest -vs -m arsha --alluredir=%ALLURE_RESULTS%
                """
                script {
                    if (isUnix()) {
                        sh """
                        source ${VENV}/bin/activate
                        pytest -vs --alluredir=${ALLURE_RESULTS}
                        """
                    } else {
                        bat """
                        ${VENV}\\Scripts\\pytest -vs -m arsha --alluredir=%ALLURE_RESULTS%
                        """
                    }
                }
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure includeProperties: false, results: [[path: "${ALLURE_RESULTS}"]]
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}