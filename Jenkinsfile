pipeline {
    agent any
    stages{
        stage("connect Jenkins")
        {
            steps
            {
                rtServer (
                    id: 'Artifactory-1',
                    url: 'https://gayatriwankhade.jfrog.io/artifactory',
                    // If you're using username and password:
                    username: 'gayatridwankhade@gmail.com',
                    password: 'Gayatri@123',
                    )
            }

        }
        stage("upload file")
        {
            steps{
                rtUpload (
                        serverId: 'Artifactory-1',
                        spec: '''{
                            "files": [
                                {
                                "pattern": "C:\Users\User\Desktop\145989_Gayatri_Wankhade",
                                "target": "https://gayatriwankhade.jfrog.io/artifactory/default-docker-virtual/"
                                }
                                ]
                                }''',
          )
    }
}