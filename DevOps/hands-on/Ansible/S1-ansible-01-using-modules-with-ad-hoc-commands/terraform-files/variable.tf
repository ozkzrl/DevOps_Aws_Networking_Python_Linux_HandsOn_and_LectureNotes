variable "tags" {
  default = ["control_node", "node_1", "node_2"]
}
variable "mykey" {
  default = "my-key"
}
variable "user" {
  default = "my-user"
}

variable "amznlnx2023" {
  default = "ami-0de716d6197524dd9"
}

variable "ubuntu" {
  default = "ami-020cba7c55df1f615"
}

variable "instype" {
  default = "t3.micro"
}

# variable "aws_secret_key" {
#  default = "xxxxx"
# }

# variable "aws_access_key" {
#  default = "xxxxx"
# }