rangaswamy_lavanya@cloudshell:~ (gothic-depth-322803)$ gcloud container clusters create nextera-cluster --num-nodes=3 --zone=us-west2-b
WARNING: Starting in January 2021, clusters will use the Regular release channel by default when `--cluster-version`, `--release-channel`, `--no-enable-autoupgrade`, and `--no-enable-autorepair` flags are not specified.
WARNING: Currently VPC-native is not the default mode during cluster creation. In the future, this will become the default mode and can be disabled using `--no-enable-ip-alias` flag. Use `--[no-]enable-ip-alias` flag to suppress this warning.
WARNING: Starting with version 1.18, clusters will have shielded GKE nodes by default.
WARNING: Your Pod address range (`--cluster-ipv4-cidr`) can accommodate at most 1008 node(s).
WARNING: Starting with version 1.19, newly created clusters and node-pools will have COS_CONTAINERD as the default node image when no image type is specified.
Creating cluster nextera-cluster in us-west2-b...done.
Created [https://container.googleapis.com/v1/projects/gothic-depth-322803/zones/us-west2-b/clusters/nextera-cluster].
To inspect the contents of your cluster, go to: https://console.cloud.google.com/kubernetes/workload_/gcloud/us-west2-b/nextera-cluster?project=gothic-depth-322803
kubeconfig entry generated for nextera-cluster.
NAME             LOCATION    MASTER_VERSION  MASTER_IP      MACHINE_TYPE  NODE_VERSION    NUM_NODES  STATUS
nextera-cluster  us-west2-b  1.20.8-gke.900  35.236.87.153  e2-medium     1.20.8-gke.900  3          RUNNING
rangaswamy_lavanya@cloudshell:~ (gothic-depth-322803)$ kubectl get all
NAME                 TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.103.240.1   <none>        443/TCP   3m8s
rangaswamy_lavanya@cloudshell:~ (gothic-depth-322803)$ kubectl get pods
No resources found in default namespace.
rangaswamy_lavanya@cloudshell:~ (gothic-depth-322803)$ kubectl get nodes
NAME                                             STATUS   ROLES    AGE     VERSION
gke-nextera-cluster-default-pool-b80effc1-48vf   Ready    <none>   3m38s   v1.20.8-gke.900
gke-nextera-cluster-default-pool-b80effc1-hn55   Ready    <none>   3m38s   v1.20.8-gke.900
gke-nextera-cluster-default-pool-b80effc1-lrdv   Ready    <none>   3m38s   v1.20.8-gke.900
rangaswamy_lavanya@cloudshell:~ (gothic-depth-322803)$