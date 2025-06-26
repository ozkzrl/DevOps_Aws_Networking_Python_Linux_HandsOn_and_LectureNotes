# Hands-on VPC-01 : Configuring of VPC

Purpose of the this hands-on training is to create VPC and configure VPC with components.

## Learning Outcomes

At the end of the this hands-on training, students will be able to;

- learn how to create VPC,

- learn how to create subnet,

- learn how to set route tables as public and private,


## Outline

- Part 1 - Creating VPC, Subnet and Subnet associations



## Part 1 - Creating VPC, Subnet and Subnet associations

STEP 1: Create VPC

- First, go to the VPC and select Your VPC section from the left-hand menu, click create VPC.

- `Resources to create` :

```text
VPC only 

Note: After you  create VPC and all other components, show how you can do it easly via the option of "VPC, subnets, etc."
```

- create a vpc named "ondia-vpc" with `10.8.0.0/16` CIDR
    - no ipv6 CIDR block
    - tenancy: default

- click create

- explain the vpc descriptions

- enable DNS hostnames for the vpc 'ondia-vpc'

  - select 'ondia-vpc' on VPC console ----> Actions ----> Edit VPC settings 
    
  - Click "Enable DNS Hostnames"
  - Click save 

STEP 2: Create an internet gateway named 'ondia-igw'

- Go to the Internet Gateways from left hand menu

- Create Internet Gateway
   - Name Tag "ondia-igw" 
   - Click create button

-  attach the internet gateway 'ondia-igw' to the vpc 'ondia-vpc'
  - Actions ---> attach to VPC
  - Select VPC named "ondia-vpc"
  - Push "Attach Internet gateway"

STEP 3 : Configuring Route Table

- Go to the Route Tables from left hand menu

- rename the route table of the vpc 'ondia-vpc' as 'ondia-default-rt'

- select Routes on the sub-section

- click edit routes

- click add route

- add a route
    - destination ------> 0.0.0.0/0 (any network, any host)
    - As target;
      - Select Internet Gateway
      - Select 'ondia-igw'
      - save routes

- explain routes in the ondia-default-rt

STEP 4: Create Subnets
- Go to the Subnets from left hand menu
- Push create subnet button

1. 
Name tag          :ondia-az1a-public-subnet
VPC               :ondia-vpc
Availability Zone :us-east-1a
IPv4 CIDR block   :10.8.1.0/24

2. 
Name tag          :ondia-az1a-private-subnet
VPC               :ondia-vpc
Availability Zone :us-east-1a
IPv4 CIDR block   :10.8.2.0/24

3. 
Name tag          :ondia-az1b-public-subnet
VPC               :ondia-vpc
Availability Zone :us-east-1b
IPv4 CIDR block   :10.8.4.0/24

4. 
Name tag          :ondia-az1b-private-subnet
VPC               :ondia-vpc
Availability Zone :us-east-1b
IPv4 CIDR block   :10.8.5.0/24

5. 
Name tag          :ondia-az1c-public-subnet
VPC               :ondia-vpc
Availability Zone :us-east-1c
IPv4 CIDR block   :10.8.7.0/24

6. 
Name tag          :ondia-az1c-private-subnet
VPC               :ondia-vpc
Availability Zone :us-east-1c
IPv4 CIDR block   :10.8.8.0/24

- explain the subnet descriptions and reserved ips (why 251 instead of 256)

STEP 5: Route Tables

- Go to the Route Tables from left hand menu

- Select 'ondia-default-rt' and click the Subnet Association from sub-section

- show the default subnet associations on the route table 
ondia-default-rt (internet access is available even on private subnets)
- push the create route table button

- create a private route table (not allowing access to the internet) 
  - name: 'ondia-private-rt'
  - VPC : 'ondia-vpc'
  - click create button

- show the routes in the route table ondia-private-rt,

- click Subnet association button and show the route table ondia-private-rt with private subnets

- Click Edit subnet association
- select private subnets;
  - ondia-az1a-private-subnet
  - ondia-az1b-private-subnet
  - ondia-az1c-private-subnet
  - and click save

- create a public route table (allowing access to the internet) 

- push the create route table button
  - name: 'ondia-public-rt'
  - VPC : 'ondia-vpc'
  - click create button

- show the routes in the route table ondia-public-rt,

- click Subnet association button and show the route table 

-Show the default route table subnet association . There are only 3 subnet implicitly.

- ondia-public-rt with public subnets

- Click Edit subnet association

- select public subnets;
  - ondia-az1a-public-subnet
  - ondia-az1b-public-subnet
  - ondia-az1c-public-subnet
  - and click save

- select Routes on the sub-section of ondia-public-rt

- click edit routes

- click add route

- add a route
    - destination ------> 0.0.0.0/0 (any network, any host)
    - As target;
      - Select Internet Gateway
      - Select 'ondia-igw'
      - save routes    
      
STEP 6: enable Auto-Assign Public IPv4 Address for public subnets

- Go to the Subnets from left hand menu

  - Select 'ondia-az1a-public-subnet' subnet ---> Action ---> Edit subnet settings  ---> select 'Enable auto-assign public IPv4 address' ---> Save

  - Select 'ondia-az1b-public-subnet' subnet ---> Action ---> Edit subnet settings  ---> select 'Enable auto-assign public IPv4 address' ---> Save

  - Select 'ondia-az1c-public-subnet' subnet ---> Action ---> Edit subnet settings  ---> select 'Enable auto-assign public IPv4 address' ---> Save

- Create two instances . One is in the Private and the other one is in Public subnet. Show the public and private IPs of instances. 

- Compare the IP of instance and Subnet CIDR block.


