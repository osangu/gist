data "aws_vpc" "playground_vpc" {
  filter {
    name = "tag:Name"
    values = ["playground_vpc"]
  }
}

data "aws_subnets" "private_subnets" {
  filter {
    name = "tag:is-public"
    values = ["False"]
  }
}

data "aws_eks_cluster" "playground" {
  name = "playground-eks"
}

data "aws_eks_cluster_auth" "playground" {
  name = "playground-eks"
}

