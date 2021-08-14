# Take-home-assignment 
A simple Flask-Kubernetes-Docker web application that allows the user to upload a .CSV file. On successful file upload, the application should perform the following validations:
Checks whether the uploaded is a .CSV and not any other format.
Check whether the .CSV file has exactly 10 rows and 3 columns.
Checks whether the data is present in each cell (.CSV file is "complete"). A "complete" sample test.csv is available in this repository for testing purposes.
<br>

# Contents
* [Features](#features)
* [Technologies & Stack](#techstack)
* [Set-up & Installation](#installation)
* [Google Cloud Deployment Steps](#deployment)


## <a name="features"></a> Features

Homepage - page where you can upload file
<br>


Validate_file - throws response message after validating the file
<br>


## <a name="techstack"></a> Technologies and Stack
**Backend:**
Python, Flask <br>
**Frontend:**
HTML, Jinja, CSS <br>

## <a name="installation"></a> Code Set-up & Installation
Install a code editor such as [VS code](https://code.visualstudio.com/download) or [Sublime Text](https://www.sublimetext.com/).<br>
Install [Python3](https://www.python.org/downloads/mac-osx/)<br>
Install [pip](https://pip.pypa.io/en/stable/installing/), the package installer for Python <br>

Clone or fork repository:
```
$ git clone https://github.com/rlavanya9/take-home-assign.git
```
Create and activate a virtual environment inside the directory:
```
$ virtualenv myproject
$ source myproject/bin/activate
```
Install dependencies:
```
$ pip3 install -r requirements.txt
```
In server.py, get the file uploaded and do all the file validations
Run the app from the command line:
```
$ python3 server.py
```

## <a name="deployment"></a> Google Cloud Deployment Steps
1. Set the PROJECT_ID env
```
rangaswamy_lavanya@cloudshell:~ (gothic-depth-322803)$ export PROJECT_ID="$(gcloud config get-value project -q)"
Your active configuration is: [cloudshell-20755]
```
2. Checkout git repo
```
rangaswamy_lavanya@cloudshell:~ (gothic-depth-322803)$ git clone https://github.com/rlavanya9/take-home-assign.git
```
3. Build docker image 
```
rangaswamy_lavanya@cloudshell:~ (gothic-depth-322803)$ docker build -t gcr.io/${PROJECT_ID}/nextera:v1 .
```
4. Authenticate gcloud CLI to access Google Container Registry
```
rangaswamy_lavanya@cloudshell:~ (gothic-depth-322803)$ gcloud auth configure-docker
```
5. Push docker image
```
rangaswamy_lavanya@cloudshell:~ (gothic-depth-322803)$ docker push gcr.io/${PROJECT_ID}/nextera:v1
```
6. List the created docker image
```
rangaswamy_lavanya@cloudshell:~ (gothic-depth-322803)$ docker image ls
```
7. Enable Kubernetes Engine in Google Cloud UI
8. Creating Kubernetes Cluster
```
rangaswamy_lavanya@cloudshell:~ (gothic-depth-322803)$ gcloud container clusters create nextera-cluster --num-nodes=3 --zone=us-west2-b
Creating cluster nextera-cluster in us-west2-b...done.
Created [https://container.googleapis.com/v1/projects/gothic-depth-322803/zones/us-west2-b/clusters/nextera-cluster].
To inspect the contents of your cluster, go to: https://console.cloud.google.com/kubernetes/workload_/gcloud/us-west2-b/nextera-cluster?project=gothic-depth-322803
kubeconfig entry generated for nextera-cluster.
NAME             LOCATION    MASTER_VERSION  MASTER_IP      MACHINE_TYPE  NODE_VERSION    NUM_NODES  STATUS
nextera-cluster  us-west2-b  1.20.8-gke.900  35.236.87.153  e2-medium     1.20.8-gke.900  3          RUNNING
```
9. Check for created Kubernetes Cluster:
```
rangaswamy_lavanya@cloudshell:~ (gothic-depth-322803)$ kubectl get all
NAME                 TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.103.240.1   <none>        443/TCP   3m8s
```
10. Check for Created Nodes:
```
rangaswamy_lavanya@cloudshell:~ (gothic-depth-322803)$ kubectl get nodes
NAME                                             STATUS   ROLES    AGE     VERSION
gke-nextera-cluster-default-pool-b80effc1-48vf   Ready    <none>   3m38s   v1.20.8-gke.900
gke-nextera-cluster-default-pool-b80effc1-hn55   Ready    <none>   3m38s   v1.20.8-gke.900
gke-nextera-cluster-default-pool-b80effc1-lrdv   Ready    <none>   3m38s   v1.20.8-gke.900
rangaswamy_lavanya@cloudshell:~ (gothic-depth-322803)$
```
11. Enable kubernetis Engine in Google Cloud UI
12. Goto workload deploy and connect with the container created in Google Cloud UI
13. Goto service and click on proxy port then run the command given in terminal
14. Get the public link