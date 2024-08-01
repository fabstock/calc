pipeline {
    agent any
    
    environment {
        // Définissez les variables d'environnement, si nécessaire
        GIT_REPO = 'https://github.com/fabstock/calc.git'
        BRANCH_NAME = 'master'
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout du dépôt depuis GitHub
                git url: "${GIT_REPO}", branch: "${BRANCH_NAME}"
            }
        }
        
        stage('Build') {
            steps {
                // Construction du projet (par exemple, avec Maven)
                //sh 'mvn clean install'
                echo build
            }
        }
        
        stage('Test') {
            steps {
                // Exécution des tests (si applicable)
                //sh 'mvn test'
                echo test
            }
        }
        
        stage('Archive Artifacts') {
            steps {
                // Archivage des artefacts de construction
                //archiveArtifacts artifacts: '**/target/*.jar', allowEmptyArchive: true
                archiveArtifacts artifacts: '**/documentations/*.md', allowEmptyArchive: true
            }
        }
    }
    
    post {
        always {
            // Actions à effectuer après chaque exécution, qu'elle soit réussie ou non
            echo 'Pipeline finished.'
        }
        success {
            // Actions à effectuer si le pipeline est réussi
            echo 'Pipeline succeeded!'
        }
        failure {
            // Actions à effectuer si le pipeline échoue
            echo 'Pipeline failed!'
        }
    }
}
