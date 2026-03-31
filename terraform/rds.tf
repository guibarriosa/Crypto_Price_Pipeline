resource "aws_db_instance" "crypto_db" {
  identifier           = "rds-crypto-db"
  allocated_storage    = 10
  db_name              = "crypto_db"
  engine               = "mysql"
  engine_version       = "8.0"
  instance_class       = "db.t3.micro"
  username             = "gui"
  password             = "barriosa123"
  parameter_group_name = "default.mysql8.0"
  skip_final_snapshot  = true
  

}

