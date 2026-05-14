resource "aws_lambda_function" "crypto_pipeline" {
  function_name = "crypto-pipeline-function"
  description   = "Extracts prices from CoinGecko, stores in S3 and RDS"

  s3_bucket = aws_s3_bucket.crypto_bucket.bucket 
  s3_key    = "lambda/lambda_package.zip" # This should match the key of the zip file you upload to S3

  runtime = "python3.11"
  handler = "main.handler"  

  role = aws_iam_role.lambda_role.arn

  timeout     = 30   
  memory_size = 256 

  # Dont forget to set these variables in your github secrets or terraform variables file
  environment {
    variables = {
      DB_HOST     = aws_db_instance.crypto_db.address 
      DB_PORT     = "3306"
      DB_NAME     = var.db_name
      DB_USER     = var.db_user
      DB_PASSWORD = var.db_password
      S3_BUCKET   = aws_s3_bucket.crypto_bucket.bucket 
    }
  }

  vpc_config {
    subnet_ids         = module.vpc.private_subnets
    security_group_ids = [aws_security_group.lambda_sg.id]
  }

  tags = {
    Name = "Crypto Pipeline Lambda Function"
  }

  depends_on = [
    aws_iam_role_policy_attachment.lambda_basic,
    aws_iam_role_policy_attachment.lambda_vpc,
    aws_iam_role_policy.lambda_s3,
  ]
}