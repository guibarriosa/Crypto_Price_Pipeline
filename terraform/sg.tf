resource "aws_security_group" "rds_sg" {
  name        = "crypto-pipeline-rds-sg"
  description = "Security group for RDS instance"
  vpc_id = module.vpc.vpc_id

  ingress {
    from_port       = 3306
    to_port         = 3306
    protocol        = "tcp"
    cidr_blocks     = [var.my_ip]
    description     = "Allow MySQL access from specific IP"
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "Crypto Pipeline RDS SG"
  }
}

resource "aws_security_group" "lambda_sg" {
  name        = "crypto-pipeline-lambda-sg"
  description = "Security group for Lambda function"
  vpc_id      = module.vpc.vpc_id  

  egress {
    from_port       = 3306
    to_port         = 3306
    protocol        = "tcp"
    security_groups = [aws_security_group.rds_sg.id]  
  }

  egress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "Crypto Pipeline Lambda SG"
  }
}