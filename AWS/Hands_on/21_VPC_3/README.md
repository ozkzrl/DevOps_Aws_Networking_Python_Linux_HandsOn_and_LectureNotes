# Hands-on VPC-03 : 

## Part 5 - Creating VPC peering between two VPCs (Default and Custom one)

## STEP 1 : Prep---> Launching Instances


- Launch two Instances. First instance will be in "ondia-az1a-private-subnet" of "ondia-vpc-a",and the other one will be in your "Default VPC". 

- In addition, since the private EC2 needs internet connectivity to set user data, we also need NAT Gateway.

### A. Configure Public Windows instance in **Default VPC.

```text
AMI             : Microsoft Windows Server 2022 Base
Instance Type   : t2.micro
Network         : **Default VPC
Subnet          : Default Public Subnet a
Security Group  : 
    Sec.Group Name : WindowsSecGrb
    Rules          : RDP --- > 3389 ---> Anywhere
Tag             :
    Key         : Name
    Value       : Windows public

PS: For MAC, "Microsoft Remote Desktop" program should be installed on the computer.
```

### B. Since the private EC2 needs internet connectivity to set user data, we use NAT Gateway

- Click Create Nat Gateway button in left hand pane on VPC menu

- click Create NAT Gateway.

```bash
Name                      : ondia-nat-gateway-2

Subnet                    : ondia-az1a-public-subnet

Elastic IP allocation ID  : Second Elastic IP
```
- click "Create Nat Gateway" button

### C. Modify Route Table of Private Instance's Subnet

- Go to VPC console on left hand menu and select Route Table tab

- Select "ondia-private-rt" ---> Routes ----> Edit Rule ---> Add Route
```
Destination     : 0.0.0.0/0
Target ----> Nat Gateway ----> ondia-nat-gateway-2
```
- click save routes

WARNING!!! ---> Be sure that NAT Gateway is in active status. Since the private EC2 needs internet connectivity to set user data, NAT Gateway must be ready.

### D. Since we need http connection we need to change Private Sec.Grb.

Security Group    : 
    Sec.Group Name : Private-Sec-Group
    Rules          : TCP  ---> 22 ---> Anywhere
                     HTTP ---> 80 ---> Anywhere


### E. Configure Private instance in 'ondia-az1a-private-subnet' of 'ondia-vpc-a'.

```text
AMI             : Amazon Linux 2023
Instance Type   : t2.micro
Network         : ondia-vpc-a 
Subnet          : ondia-az1a-private-subnet
user data       : 
```

```bash
#!/bin/bash

dnf update -y
dnf install nginx -y
dnf install -y wget
systemctl enable nginx
cd /usr/share/nginx/html
chmod o+w /usr/share/nginx/html
rm index.html
wget https://raw.githubusercontent.com/awsdevopsteam/route-53/master/index.html
wget https://raw.githubusercontent.com/awsdevopsteam/route-53/master/ken.jpg
systemctl start nginx
```

```text
Security Group    : 
    Sec.Group Name : Private-Sec-Group
    
Tag             :
    Key         : Name
    Value       : Private EC2 for peering 
```

- Go to instance named 'Windows public' and push the connect button ----> Download Remote Desktop File

- Decrypt your ".pem key" using "Get Password" button
  - Push "Get Password" button
  - Select your pem key using "Choose File" button ----> Push "Decrypt Password" button
  - copy your Password and paste it "Windows Remote Desktop" program as a "administrator password"

- Open the internet explorer of windows machine and paste the private IP of EC2 named 'Private EC2 for peering'

- It is not able to connect to the website 


## STEP 2: Setting up Peering


- Go to 'Peering connections' menu on the left hand side pane of VPC

- Push "Create Peering Connection" button

```text
Peering connection name tag : First Peering
VPC(Requester)              : Default VPC
Account                     : My Account
Region                      : This Region (us-east-1)
VPC (Accepter)              : ondia-vpc-a
```
- Hit "Create peering connection" button

- Select 'First Peering' ----> Action ---> Accept Request ----> Accept Request

- Go to route Tables and select default VPC's route table ----> Routes ----> Edit routes
```
Destination: paste "ondia-vpc" CIDR blok
Target ---> peering connection ---> select 'First Peering' ---> Save routes
```

- select ondia-private-rt's route table ----> Routes ----> 
Edit routes
```
Destination: paste "default VPC" CIDR blok
Target ---> peering connection ---> select 'First Peering' ---> Save routes
```

- Go to windows EC2 named 'Windows public', write IP address on browser and show them to website with KEN..


WARNING!!! ---> Please do not terminate "NAT Gateway" and "Private WEB EC2" for next part.


## Part 6 - Create VPC Endpoint

# STEP 1: Prep

Security Group    : 
    Sec.Group Name : Public-Sec-Group (Bastion Host)
    Rules          : TCP --- > 22 ---> Anywhere
                     All ICMP IPv4  ---> Anywhere
                     HTTP--------> Anywhere

Security Group    : 
    Sec.Group Name : Private-Sec-Group (Private Web Server)
    Rules          : TCP  ---> 22  ---> Public-Sec-Group
                     HTTP --->80   ---> Public-Sec-Group
                     All ICMP IPv4 ---> Public-Sec-Group


### A. Create S3 Bucket 

- Go to the S3 service on AWS console
- Create a bucket of `ondia-vpc-endpoint` with following properties, 

```text
Object Ownership            : ACLs disabled
Block all public access     : Checked
Versioning                  : Disabled
Server access logging       : Disabled
Tags                        : 0 Tags
Default encryption          : Disabled
Object lock                 : Disabled

```
- Upload 'Guile.png' and 'Honda.png' files into the S3 bucket

### B. Configure Public Instance (Bastion Host)

```text
AMI             : Amazon Linux 2023
Instance Type   : t2.micro
Network         : ondia-vpc-a
Subnet          : ondia-az1b-public-subnet
Security Group  : Public-Sec-Group (Bastion Host)
Tag             :
    Key         : Name
    Value       : Public EC2 (Bastion Host)
```

### C. Create IAM role to reach S3 from "Private WEB EC2"

- Go to IAM Service from AWS console and select roles on left hand pane

- click create role
```
Trusted entity type: AWS Service
use case : EC2  
Permissions Policies: AmazonS3FullAccess ---> Next
Role Name : ondiaS3FullAccessforEndpoint
Role description: ondia S3 Full Access for Endpoint
click create button
```
Go to EC2 service from AWS console

Select "Private WEB EC2" ---> Actions ---> Security ---> Modify IAM Role  select newly created IAM role named 'ondiaS3FullAccessforEndpoint' ---> Apply

# STEP 2: Connect S3 Bucket from Private WEB Instance

### A. Connect to the Bastion host

- Go to terminal and connect to the Bastion host named 'Public EC2 (Bastion Host)'

- Using Bastion host connect to the EC2 instance in "private subnet" named 'Private WEB EC2 ' (using ssh agent or copying directly pem key into the EC2)

- Enable ssh-agent (start the ssh-agent in the background)

```bash
eval "$(ssh-agent)"
```
- Add your private key to the ssh agent on your `localhost`. `ssh-agent is a program that runs in background and stores your keys in memory`.

```bash
ssh-add ./[your pem file name]
```
- connect to the ec2-in-az1a-public-sn instance in public subnet
```bash
ssh -A ec2-user@ec2-3-88-199-43.compute-1.amazonaws.com
```
### B.Connect to the Private Instance

- once logged into the bastion host connect to 
the private instance in the private subnet:
```bash
ssh ec2-user@[Your private EC2 private IP]
```
### C. Use CLI to verify connectivity

- list the bucket in S3 and content of S3 bucket named "aws s3 ls "ondia-vpc-endpoint" via following command

```
aws s3 ls
aws s3 ls ondia-vpc-endpoint
```
- go to private route table named "ondia-private-rt" on VPC service

- select routes sub-menu ---> Edit routes ---> Delete "NAT Gateway"

- Go to the terminal and try to connect again S3 bucket via following command
```
aws s3 ls
```
- show that you are "not able to connect" to the s3 buckets list


## STEP 3: Create Endpoint

### A. Connect  to S3 via Endpoint

- go to the Endpoints menu on left hand pane in VPC

- click Create Endpoint
```text
Service Category : AWS services
Service Name     : com.amazonaws.us-east-1.s3
Service Type     : gateway
VPC              : ondia-vpc-a
Route Table      : choose private one or both 
```
- Create Endpoint

- Go to private route table named 'ondia-private-rt' and show the endpoint rule that is automatically created by AWS 

### B. Connect  to S3 via Endpoint

- Go to terminal, list the buckets in S3 and content of S3 bucket named "aws s3 ls 
"ondia-vpc-endpoint" via following command
```bash
aws s3 ls
aws s3 ls ondia-vpc-endpoint
```

- copy the 'Guile.png' and 'Honda.png' files from S3 bucket into the private EC2
```bash
aws s3 cp s3://ondia-vpc-endpoint/Guile.png .
aws s3 cp s3://ondia-vpc-endpoint/Honda.png .
```













