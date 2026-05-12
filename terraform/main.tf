terraform {
  backend "s3" {
    bucket = "crypto-pipeline-tfstates" # Insert your S3 bucket for backend here. Make sure this bucket exists before running the project.
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

