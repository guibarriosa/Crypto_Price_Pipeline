resource "aws_db_instance" "crypto_db" {
  identifier           = "rds-crypto-db"
  allocated_storage    = 10
  db_name              = var.db_name
  engine               = "mysql"
  engine_version       = "8.0"
  instance_class       = "db.t3.micro"
  username             = var.db_user
  password             = var.db_password
  parameter_group_name = "default.mysql8.0"
  skip_final_snapshot  = true

  vpc_security_group_ids = [aws_security_group.rds_sg.id]
  db_subnet_group_name   = aws_db_subnet_group.crypto_subnets.name

  publicly_accessible = true
  
  tags = {
    Name = "Crypto Pipeline RDS"
  }

}

resource "aws_db_subnet_group" "crypto_subnets" {
  name       = "crypto-db-subnets"
  subnet_ids = module.vpc.public_subnets

  tags = {
    Name = "Crypto DB Subnet Group"
  }
}
