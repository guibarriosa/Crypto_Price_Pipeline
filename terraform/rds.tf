resource "aws_db_instance" "crypto_db" {
  identifier           = "rds-crypto-db"
  allocated_storage    = 10
  db_name              = "crypto_db"
  engine               = "mysql"
  engine_version       = "8.0"
  instance_class       = "db.t3.micro"
  username             = "gui"
  password             = var.db_password
  parameter_group_name = "default.mysql8.0"
  skip_final_snapshot  = true

  vpc_security_group_ids = [aws_security_group.rds_sg.id]
  db_subnet_group_name   = aws_db_subnet_group.crypto_subnets.name

  publicly_accessible = true
  
}

resource "aws_db_subnet_group" "crypto_subnets" {
  name       = "crypto_db_subnets"
  subnet_ids = module.vpc.public_subnets

  tags = {
    Name = "Crypto DB Subnet Group"
  }
}
