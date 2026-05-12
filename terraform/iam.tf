# IAM Role for Lambda Execution
resource "aws_iam_role" "lambda_role" {
  name = "crypto-pipeline-lambda-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}

# Attach already existing AWS managed policies to the Lambda role.
# This one allows the Lambda function to write logs to CloudWatch.
resource "aws_iam_role_policy_attachment" "lambda_basic" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# And this one allows the Lambda function to access VPC resources, which is necessary for connecting to RDS.
resource "aws_iam_role_policy_attachment" "lambda_vpc" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaVPCAccessExecutionRole"
}

# Custom inline policy that allows the Lambda function to read/write objects in the S3 bucket.
resource "aws_iam_role_policy" "lambda_s3" {
  name = "crypto-pipeline-lambda-s3"
  role = aws_iam_role.lambda_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = [
        "s3:PutObject",
        "s3:GetObject",
      ]
      Resource = [
        "arn:aws:s3:::crypto-pipeline-gui/*" # Dont forget to replace with your actual bucket name
        
      ]
    }]
  })
}