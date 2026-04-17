terraform {
  backend "s3" {
    bucket = "crypto-pipeline-tfstates"
    key    = "terraform/terraform.tfstate"
    region = "us-east-1"
  }
  
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 6.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

