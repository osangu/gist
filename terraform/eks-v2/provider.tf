terraform {
  required_version = "~> 1.3"
  required_providers {
    tls = {
      source  = "hashicorp/tls"
      version = "3.4.0"
    }
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.38"
    }
  }
  backend "s3" {
    bucket         = ""
    key            = ""
    region         = ""
    dynamodb_table = ""
  }
}

provider "aws" {
  region     = ""
  access_key = ""
  secret_key = ""
}
