resource "aws_s3_bucket" "crypto_bucket" {
  bucket = "crypto-pipeline-gui" # Insert your S3 bucket name here.

  force_destroy = true 

  tags = {
    Name        = "Crypto Pipeline Bucket"
    Environment = "Dev"
  }
}

