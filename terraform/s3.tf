resource "aws_s3_bucket" "crypto_bucket" {
  bucket = "crypto-pipeline-gui"

  tags = {
    Name        = "Crypto Pipeline Bucket"
    Environment = "Dev"
  }
}

