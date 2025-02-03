module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "18.31.0"

  cluster_name = "playground"

  vpc_id     = data.aws_vpc.playground_vpc.id
  subnet_ids = data.aws_subnets.private_subnets.ids

  eks_managed_node_groups = {
    dashboard_asg = {
      ami_type     = "AL2023_x86_64_STANDARD"
      max_size     = 3
      min_size     = 1
      desired_size = 1
      instance_types = ["t3.small"]
    }
  }

  cluster_addons = {
    coredns = {
      resolve_conflicts = "OVERWRITE"
    }
    vpc-cni = {
      resolve_conflicts = "OVERWRITE"
    }
    kube-proxy = {}
    aws-efs-csi-driver = {}
    eks-pod-identity-agent = {}
  }

  cluster_endpoint_public_access  = true
  cluster_endpoint_private_access = true
  cluster_endpoint_public_access_cidrs = ["0.0.0.0/0"] # change to you ip

  cloudwatch_log_group_retention_in_days = 3

  manage_aws_auth_configmap = true

  # After Create EKS
  aws_auth_users = [
    {
      userarn  = "arn:aws:iam::{}:user/{}"
      username = "{}"
      groups = ["system:masters"]
    }
  ]
}
