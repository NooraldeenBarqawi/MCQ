# MCQ
![Screenshot 2023-12-05 210537](https://github.com/NooraldeenBarqawi/MCQ/assets/100937529/7636a938-64e0-44df-b785-f72ad4937d14)

Sequence Diagram for DevOps

Streamlit App Deployment with Azure Container Registry and GitHub Actions

Introduction

This document outlines the process of deploying a Streamlit app containerized using Docker on Azure Container Registry (ACR) and automated using GitHub Actions.
 
1. Created an Azure Container Registry:

Navigated to the Azure Portal and initiated the creation of a new ACR resource.
Assigned a unique name to the ACR and selected the appropriate subscription and resource group.
Configured access control for the ACR.
2. Built and Pushed Docker Image:

Utilized the Dockerfile provided with the Streamlit app to build the Docker image.
Tagged the Docker image with the ACR repository URL and a unique tag.
Executed the docker push command to push the Docker image to the designated ACR repository.
3. Created GitHub Actions Workflow:

Created a new GitHub repository to house the Streamlit app.
Accessed the Actions tab within the GitHub repository.
Established a new workflow file (e.g., deploy.yml) for automated deployment.
Defined the workflow steps, encompassing:
Checking out the code from the repository.
Setting up the Docker environment.
Retrieving the Docker image from ACR.
Deploying the Docker image to Azure App Service.


4. Connected GitHub Actions to Azure App Service:

Integrated the azure/webapp-deploy@v2 action into the GitHub Actions workflow for deployment tasks.
Supplied the Azure App Service connection details, including subscription ID, resource group name, and app service name.
Configured deployment parameters, such as the deployment method and target environment.
5. Triggered Automated Deployment:

Initiated a commit and push of any changes made to the Streamlit app code.
GitHub Actions automatically detected the changes and initiated the deployment workflow.
The workflow built the Docker image, pushed it to ACR, and deployed it to Azure App Service.
Sequence Diagram
 
