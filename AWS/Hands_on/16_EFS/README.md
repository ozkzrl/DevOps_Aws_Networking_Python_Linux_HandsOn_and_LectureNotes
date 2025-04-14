# Hands-on EFS-01 : How to Create EFS & Attach the EFS to the multiple EC2 Linux Instances

## Outline

- Part 1 - Prep(EC2 SecGrp, EFS SecGrp, EC2 Linux Instance)

- Part 2 - Creating EFS

- Part 3 - Attach the EFS to the multiple EC2 Linux instances


## Part 1 - Prep (EC2 SecGrp, EFS SecGrp, EC2 Linux Instance)

### Step 1 - Create EC2 SecGrp:

- Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

- Choose the Security Groups on left-hand menu

- Click the `Create Security Group`.

```text
Security Group Name  : EC2 SecGrp
Description          : EC2 SecGrp
VPC                  : Default VPC
Inbound Rules:
    - Type: SSH ----> Source: Anywhere
Outbound Rules: Keep it as default
Tag:
    - Key   : Name
      Value : EC2 SecGrp
```

### Step 2 - Create EFS SecGrp:

- Click the `Create Security Group`.

```text
Security Group Name  : EFS SecGrp
Description          : EFS SecGrp
VPC                  : Default VPC
Inbound Rules:
    - Type: NFS ----> Port: 2049 ------>Source: sg-EC2 SecGrp
Outbound Rules: Keep it as default
Tag:
    - Key   : Name
      Value : EFS SecGrp
```

### Step 3 - Create EC2 :

- Configure First Instance in N.Virginia

```text
AMI             : Amazon Linux 2023
Instance Type   : t2.micro
Network         : default
Subnet          : default
Security Group  : EC2 SecGrp
Tag             :
    Key         : Name
    Value       : EFS-Instance-1
```

- Configure Second Instance in N.Virginia

```text
AMI             : Amazon Linux 2023
Instance Type   : t2.micro
Network         : default
Subnet          : default
Security Group  : EC2 SecGrp
Tag             :
    Key         : Name
    Value       : EFS-Instance-2
```

## Part 2 - Creating EFS

Open the Amazon EFS console at https://console.aws.amazon.com/efs/.

- Click "Create File System" 

- Click "Customize" 
```text
General:
Name                    : FirstEFS
Storage class           : Standart
Automatic backups       : Uncheck "Enable automatic backups"
Lifecycle management    : Select "None"
Encryption              : Enable encryption of data at rest
```
```text
Performance settings:
Keep default settings
```

- Click "Next"
```text
Network: 
Virtual Private Cloud (VPC) : Default VPC (Keep default)
Mount targets               : 
  - Clear "default sg" from all AZ
  - Add "EFS SecGrp" to all AZ
```
- Show that you can only add one mount point for each AZ though it has multiple subnets (for example custom VPC) 
- Click "Next"

```text

File system policy - optional:
Keep default settings.
```
- Click "Next"
```text

Review and create:
Review settings
```
- Click "Create"


## Part 3 - Attach the EFS to the multiple EC2 Linux instances

### STEP-1: Configure the EC2-1 instance


- Go EC2 console

- Connect to EC2-1 with SSH.
```bash
ssh -i .....pem ec2-user@..................
```
- Update the installed packages and package cache on your instance.

```bash
sudo dnf update -y
```
- Change the hostname 

```bash
sudo hostnamectl set-hostname paulFirst
```

- type "bash" to see new hostname.

```bash
bash
```

- Install the "Amazon-efs-utils Package" on Amazon Linux

```bash
sudo yum install -y amazon-efs-utils
```

- Create Mounting point 

```bash
sudo mkdir efs
```

- Go to the EFS console and click  on "FirstEFS" . Then click "Attach" button seen top of the "EFS" page.

- On the pop up window, copy the script seen under "Using the EFS mount helper" option: "sudo mount -t efs -o tls fs-60d485e2:/ efs"

- Turn back to the terminal and mount EFS using the "EFS mount helper" to the "efs" mounting point

```bash
sudo mount -t efs -o tls fs-xxxxxx:/ efs
sudo mount -t efs -o tls fs-abcd123456789ef0:/ efs/

sudo mount -t efs -o tls fs-0d9c4301e5a4c7241:/ efs
```
- Check if EFS is mounted

```bash
df -hT
```

- Check the "efs" folder

```bash
ls
```
- Go the "efs" folder and create a new file with Nano editor.

```bash
cd efs
sudo nano example.txt
```
- Write something, save and exit;
```bash
"hello from first EC2"
CTRL X+Y
```

- check the example.txt

```bash
cat example.txt
```

### STEP-2: Configure the EC2-2 instance

-  Connect to EC2-2 with SSH.
```bash
ssh -i .....pem ec2-user@..................
```
- Update the installed packages and package cache on your instance.

```bash
sudo dnf update -y
```
- Change the hostname 

```bash
sudo hostnamectl set-hostname paulSecond
```
- type "bash" to see new hostname.

```bash
bash
```
- Install the "Amazon-efs-utils Package" on Amazon Linux

```bash
sudo yum -y install nfs-utils
sudo systemctl status nfs-server
sudo systemctl enable nfs-server
sudo systemctl start nfs-server
```

- Create Mounting point 

```bash
sudo mkdir efs
```

- Go to the EFS console and click  on "FirstEFS" . Then click "Attach" button seen top of the "EFS" page.

- On the pop up window, copy the script seen under "Using the EFS mount helper" option: "sudo mount -t efs -o tls fs-60d485e2:/ efs"

- Turn back to the terminal and mount EFS using the "EFS mount helper" to the "efs" mounting point

```bash
sudo mount -t nfs -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport file-system-id.efs.aws-region.amazonaws.com:/ /efs-mount-point
sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-0d9c4301e5a4c7241.efs.us-east-1.amazonaws.com:/ efs
```
- Check the "efs" folder
```bash
ls
```
- Check the example.txt. Show that you can also reach the same file.

```bash
cat example.txt
```

- Add something example.txt

```bash
sudo nano example.txt
"hello from second EC2"
CTRL X+Y
```
- Check the example.txt

```text
cat example.txt

"hello from first EC2"
"hello from second EC2"
```
- Connect from EC2-1 to the "efs" and show the example.txt:


```bash
cd efs
cat example.txt

"hello from first EC2"
"hello from second EC2"
```

***Don't forget to edit fstab to mount efs on reboot!!!***

#### If you dont want to use "Aumotatic" feauture on AWS management console, you can mount as written below
Setting up Automatic Mounting using /etc/fstab with the EFS Mount Helper

Your EC2 instance is now mounted to the EFS file system.
However, you'll notice that if you reboot your instance(EC2-1 & EC2-2), the file system does not remount to your instance.
We can use the `/etc/fstab` file with EFS mount helper to automatically remount the file system.
The `/etc/fstab` file contains information about file systems that should be mounted during instance booting.

1. Back up the /etc/fstab file.

```bash
sudo cp /etc/fstab /etc/fstab.bak
```

2.  Run the following command to open the `/etc/fstab` file in the nano editor.  
    
```bash
sudo nano /etc/fstab
```
    
3.  On a new line, paste in the following (remember to use the file system ID):  
    
```bash

fs-xxxxxx:/ /home/ec2-user/efs efs tls,_netdev

fs-0d9c4301e5a4c7241:/ /home/ec2-user/efs efs tls,_netdev

```

for NFS
```bash
file_system_id.efs.aws-region.amazonaws.com:/ mount_point nfs4 nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport,_netdev 0 0
```

4.  Save the changes to the file.
    
5.  Let's test the new entry to see if everything was setup correctly.  
    
```bash
sudo umount -a  # to unmount all volumes excluding root volume 
sudo mount -fav
```
All done! We now have the EC2 instance remounting the file system on reboot.



### STEP-3: Configure the EC2-3 instance with EFS while Launching

- Go to the EC2 console and click "Launch Instance"

- Configure third Instance in N.Virginia

```text
AMI             : Amazon Linux 2023
Instance Type   : t2.micro
Network         : Edit >>>>> Choose one of the default subnets
Configure Storage : Advanced

  File systems  >>>> Edit >>>Add file system-------> FirstEFS 
  (Note down the mnt point "/nt/efs/fs1")m
Security Group  : EC2 SecGrp
Tag             :
    Key         : Name
    Value       : EFS-Instance-auto
```
- Connect to `EFS-Instance-auto` with SSH

- Change the hostname 

```bash
ssh -i .....pem ec2-user@..................
```

```bash
sudo hostnamectl set-hostname paulThird
```

- type "bash" to see new hostname.

```bash
bash
```

- Go to the directory of mount target 

```bash
cd /mnt/efs/fs1/
```
- Show the example.txt:

```bash
cat example.txt

"hello from first EC2"
"hello from second EC2"
```
 - Add something example.txt

```bash
sudo nano example.txt
"hello from third EC2"
CTRL X+Y
```
- Check the example.txt

```bash
cat example.txt

"hello from first EC2"
"hello from second EC2"
"hello from third EC2"
```

- Terminate instances and delete file system from console.

