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
