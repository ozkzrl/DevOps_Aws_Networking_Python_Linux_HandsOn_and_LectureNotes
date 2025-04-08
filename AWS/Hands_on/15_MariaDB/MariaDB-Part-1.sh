# Part 1 - Creating EC2 Instance and Installing MariaDB Server

# Launch EC2 Instance.

# AMI: Amazon Linux 2023
# Instance Type: t2.micro
# Security Group
#   - SSH           -----> 22    -----> Anywhere
#   - MYSQL/Aurora  -----> 3306  -----> Anywhere

# Connect to EC2 instance with SSH.

# Update dnf package management and install MariaDB server.
sudo dnf update -y
sudo dnf install mariadb105-server -y

# Warning:If you want to install mariadb on Amazon Linux 2 AMI, you should
# use this command: sudo yum install mariadb-server -y

# Start MariaDB service.
sudo systemctl start mariadb

# Check status of MariaDB service.
sudo systemctl status mariadb

# Enable MariaDB service, so that MariaDB service will be activated on restarts.
sudo systemctl enable mariadb


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-lamp-amazon-linux-2023.html