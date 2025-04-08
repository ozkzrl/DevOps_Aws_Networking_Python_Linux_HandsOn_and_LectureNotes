# Part 4 - Creating a Client Instance and Connecting to MariaDB Server Instance Remotely

# Launch EC2 Instance (Ubuntu 24.04) and name it as MariaDB-Client on Ubuntu.

# AMI: Ubuntu 24.04
# Instance Type: t2.micro
# Security Group
#   - SSH           -----> 22    -----> Anywhere

# Connect to EC2 instance with SSH.

# Update instance.
sudo apt update && sudo apt upgrade -y

# Install the mariadb-client.
sudo apt-get install mariadb-client -y

# Connect the ondiadb on MariaDB Server on the other EC2 instance (pw:ondia1234).
mysql -h ec2-54-209-152-220.compute-1.amazonaws.com -u ondiauser -p

mysql -h ec2-54-209-152-220.compute-1.amazonaws.com -u root -p

# Show that ondiauser can do same db operations on MariaDB Server instance.
SHOW DATABASES;
USE ondiadb;
SHOW TABLES;
SELECT * FROM employees;
SELECT * FROM offices;
SELECT first_name, last_name, salary, city, state FROM employees INNER JOIN offices ON employees.office_id=offices.office_id WHERE employees.salary > 100000;

# Close the mysql terminal.
EXIT;

# DO NOT FORGET TO TERMINATE THE INSTANCES YOU CREATED!!!!!!!!!!

Ref: https://mariadb.org/documentation/
https://mariadb.com/docs/skysql/connect/clients/mariadb-client/
https://aws.amazon.com/compare/the-difference-between-mariadb-vs-mysql/

