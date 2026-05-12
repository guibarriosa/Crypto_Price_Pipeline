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

  # For development purposes, we can set the RDS instance to be publicly accessible. 
  # In production, you would typically set this to false and access the database through 
  # a bastion host or SSM.
  publicly_accessible = true
  
  tags = {
    Name = "Crypto Pipeline RDS"
  }

}

# Here we create a DB subnet group for our RDS, which specifies the subnets where our instance can be launched. 
# In a production environment, you would typically use private subnets for your RDS instance.
resource "aws_db_subnet_group" "crypto_subnets" {
  name       = "crypto-db-subnets"
  subnet_ids = module.vpc.public_subnets

  tags = {
    Name = "Crypto DB Subnet Group"
  }
}
