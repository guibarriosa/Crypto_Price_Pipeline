resource "aws_s3_bucket" "crypto_bucket" {
  bucket = "crypto-pipeline-gui"

  force_destroy = true 

  tags = {
    Name        = "Crypto Pipeline Bucket"
    Environment = "Dev"
  }
}

