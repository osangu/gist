/*
bootstrap_cluster_creator_admin_permissions
- 클러스터 생성할 때 단 한번만 적용됨.
- 그래서 enable_cluster_create_damin_permissions로 사용하는 것을 권장함

access_entries
- EKS API를 사용해서 인가할 때 사용.
- Console의 Acccess 항목에서 확인 가능


https://github.com/terraform-aws-modules/terraform-aws-eks/issues/3082
- configMap 대신 EKS API를 지향하는 듯 싶다.
*/


module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 20.31"

  cluster_name = "playground-eks"

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
  cluster_endpoint_public_access_cidrs = [""] # your ip

  cloudwatch_log_group_retention_in_days = 3

  # enable_cluster_creator_admin_permissions = false
  # bootstrap_cluster_creator_admin_permissions = false
  authentication_mode = "API_AND_CONFIG_MAP"
  access_entries = {
    your_account = {
      principal_arn = "arn:aws:iam::your_iam:user/your_account"
      policy_associations = {
        admin = {
          policy_arn = "arn:aws:eks::aws:cluster-access-policy/AmazonEKSAdminPolicy"
          access_scope = {
            type = "cluster"
          }
        }
        admin_view = {
          policy_arn = "arn:aws:eks::aws:cluster-access-policy/AmazonEKSAdminViewPolicy"
          access_scope = {
            type = "cluster"
          }
        }
      }
    }
  }
}
