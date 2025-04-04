# Hands-on IAM-01 

Purpose of the this hands-on training is to give basic understanding of how to use IAM and IAM components.

## Learning Outcomes

At the end of the this hands-on training, students will be able to;

- understand root user and IAM user

- create IAM user 

- explain the credentials 

- create a settings for IAM user

- create a group

- anatomy of the policy and attaching policy to identities. 

- make troubleshooting about credentials

- create role and attach to EC2

## Outline

- Part 1 - Creating IAM user and arrange user settings

- Part 2 - Creating Groups

- Part 3 - Troubleshooting about credentials

- Part 4 - Creating role and attaching to EC2


## Part 1 - Creating IAM user and arrange user settings

- Log in  as a Root user. !!!! Please use "your individual root account."

- Show the Dashboard of IAM 

- Show IAM users "sign-in link" and customize it as alias . Tell the student to write down the account alias.

- Create IAM user with Administrator access for your daily work :

    - Explain that  unless it is needed,  students won't use root account anymore.
    - Explain policy Administrator access*  policy and policy format

- Click on newly created User---->>> Security Credentials show the credentials. 

- Create bill settings: Since we'll not use root account for daily work, we also need to check our billing from IAM user console .So we need to make some setting for this issue. 

     - Right top of the page click your name ----> Select My account -->> IAM User and Role Access to Billing Information--->> Edit--->>

- Sign Out and Sign in  with newly created IAM user with "Amazon IAM user". 

- Check the users and Billing services to be accessible or not.

## Part 2 - Creating Groups and Users

### Step 1  - Creating users of Database and Database Group

- Create group called Database (RDS FullAccess)
- Explain why we use group
- Explain inline policy and group relation
- Assign users to the Database Group

### Step 2 Create users of Developer and Developer Group

- Create group called Developer (S3 and EC2 FullAccess)
- Assign users to the Developer Group
- Ask the status of the user without policy when you delete the group which has policy 


##  Part 3 - Troubleshooting about credentials

### Step 1 - What if you forget the password 

- Click User>>>>> Select user---->>Security Credential--->> Console Password---> Click "Manage"--->>Set  password >>>> Custom password

### Step 2-  What if you forgot your secret access keys key 

-  Click User>>>>> Select user---->>Security Credential--->> Go Access keys ---> Deactivate---->> Delete --->>>Create new 


##  Part 4 - Creating role and attaching to EC2

- Create a role :

```text
Trusted Entity : AWS services
Use case       : EC2
Permission     : S3FullAccess
Name           : FirstRoleS3Full
```
- Launch an Instance **without role**:

  - AMI             : Amazon Linux 2023
  - Instance Type   : t2.micro
  - IAM role        : "None"
  - Security Group: : HTTP & SSH Allowed
  - User data       :

```text
#!/bin/bash

dnf update -y
dnf install -y httpd
cd /var/www/html
aws s3 cp s3://paul-iam-handson/index.html .
aws s3 cp s3://paul-iam-handson/mariobross.avif .
systemctl enable httpd
systemctl start httpd 
```

- Launch an Instance with  **FirstRoleS3Full** role:

  - AMI             : Amazon Linux 2023
  - Instance Type   : t2.micro
  - IAM role        : FirstRoleS3Full
  - Security Group: : HTTP & SSH Allowed
  - User data       :

```text
#!/bin/bash

dnf update -y
dnf install -y httpd
cd /var/www/html
aws s3 cp s3://paul-iam-handson/index.html .
aws s3 cp s3://paul-iam-handson/mariobross.avif .
systemctl enable httpd
systemctl start httpd 
```

- Show that the instance without role wasn't able to access S3 bucket. So the web page couldn't fetch the index.html and cat.jpg file.