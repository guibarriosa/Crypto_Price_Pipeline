resource "aws_lambda_function" "crypto_pipeline" {
  function_name = "crypto-pipeline-function"
  description   = "Extrai preços de crypto da CoinGecko, guarda em S3 e RDS"

  s3_bucket = "crypto-pipeline-gui"
  s3_key    = "lambda/lambda_package.zip"

  runtime = "python3.11"
  handler = "main.handler"  

  role = aws_iam_role.lambda_exec.arn

  timeout     = 30   # segundos — a API CoinGecko pode ser lenta
  memory_size = 128  # MB — ajusta conforme necessário

  environment {
    variables = {
      DB_HOST     = aws_db_instance.crypto_db.address 
      DB_PORT     = "3306"
      DB_NAME     = var.db_name
      DB_USER     = var.db_user
      DB_PASSWORD = var.db_password
      S3_BUCKET   = "crypto-pipeline-gui"
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
  ]
}