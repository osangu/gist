### Settings
- [Document](https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.11/)

1. IRSA
    - Install iam policy json to make AWS Policy
    ```shell
   # Difference at USA, China Region
    curl -o iam-policy.json https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.11.0/docs/install/iam_policy.json
    ```
   - Create Policy
     - Terraform  참고
   - Attach Policy to K8S serviceaccount
2. Install Cert Manager
   ```shell
    curl -o cert-manager.yaml https://github.com/cert-manager/cert-manager/releases/download/v1.12.3/cert-manager.yaml
    
   kubectl apply --validate=false -f cert-manger.yaml
   ```

3. Install v2_11_0_full.yaml
   

## Usage