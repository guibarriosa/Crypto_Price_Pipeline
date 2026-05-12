# Variable for SG, allowing MySQL access to RDS from a specific IP address.
variable "my_ip" {
  type = string
  description = "IP public of who's gonna acess RDS"
}

# Variables for RDS and Lambda connection.
variable "db_password" {
  type = string
}

variable "db_user" {
  type = string
}

variable "db_name" {
  type = string
}

