# Hands-on Linux-03 : Managing Users and Groups

Purpose of the this hands-on training is to teach the students how to manage users and groups.

## Learning Outcomes

At the end of the this hands-on training, students will be able to;

- explain users and groups in linux.

- manage users and groups.

## Outline

- Part 1 - Basic User Commands

- Part 2 - User Management

- Part 3 - User Passwords

- Part 4 - Group Management

## Part 1 - Basic User Commands
​
- whoami.
​
```bash
whoami
sudo su
pwd
whoami
su ec2-user
sudo su -
pwd
```
​
- who.
​
```bash
exit
who
who # open a new shell and retry who command to see the users who logged in.
```
​
- w.
​
```bash
w
who
```
​
- id.
​
```bash
id
id root
sudo su
useradd user1
id user1
```
​
- su.
​
```bash
su ec2-user
su user1
sudo su user1
pwd
exit
sudo su - user1
pwd
```
​
- passwd.
​
```bash
exit
sudo su
useradd user2
passwd user2    # give a password to user2
su - user2
passwd
exit
su user2
```
​
## Part 2 - User management
​
- /etc/passwd.
​
```bash
exit
cat /etc/passwd
tail -3 /etc/passwd
```
​
- useradd.
​
```bash
sudo useradd user3
cd /home
ls
cd /etc
ls login*
cat login.defs
sudo nano login.defs    # change the CREATE_HOME variable's value to "no"
sudo useradd user4
cd /home && ls
cat /etc/passwd
sudo useradd -m user5    # force to system to create a home directory for user with -m option.
cd /home && ls
sudo useradd -m -d /home/user6home user6    # change the user's home directory name with -d option.
ls
sudo useradd -m -c "this guy is developer" user7    # give a descrpition to user with -c option.
cat /etc/passwd
cat /etc/passwd | grep user7
```
​
- userdel.
​
```bash
cat /etc/passwd
sudo userdel user5
cat /etc/passwd
cd /home && ls
sudo userdel -r user1    # delete user and its home directory with -r option.
cd /home && ls
```
​
- usermod.
​
```bash
cat /etc/passwd
sudo usermod -c "this guy will be an aws solution architect" user7
cat /etc/passwd
sudo usermod --help
sudo usermod -l Superuser user2    # change the name of the user2 with -l option.
cat /etc/passwd
```
​
## Part 3 - User Passwords
​
- passwd-etc/shadow-etc/login.defs.
​
```bash
  sudo su
  useradd user8
  passwd user8
  cd /etc
  cat shadow
  cat login.defs
```
​
## Part 4 - Group Management
​
- groups.
​
```bash
groups
sudo groupadd linux
sudo groupadd aws
sudo groupadd python
cat /etc/group
groups
sudo usermod -a -G linux ec2-user    # append ec2-user in linux group.
cat /etc/group
groups
sudo usermod -G aws ec2-user    # this command deletes all groups that ec2-user in except default group of ec2-user and add ec2-user to aws group.
cat /etc/group
sudo groupmod -n my-linux linux    # change the name of the linux group.
cat /etc/group
groups
cat /etc/group
sudo groupdel python
cat /etc/group
sudo gpasswd -a user7 aws    # add a user to a group.
cat /etc/group
sudo gpasswd -d user7 aws    # delete a user to a group.
cat /etc/group
```

### Optional Part 

## useradd examples

```bash
sudo useradd -m -d /home/paul123 -c "devops engineer" paul

tail -2 /etc/passwd

su - paul

passwd paul 

sudo passwd paul
```


```bash
useradd -m -d /home/otto -c "solution architect" -u 1010 -p 123450 otto

su - otto   

passwd otto

sudo passwd otto
```

```bash
echo "P4sSw0rD" | openssl passwd -6 -stdin

useradd -m -d /home/dummy -g idiots -p $(echo "P4sSw0rD" | openssl passwd -6 -stdin) -u 1030 dummy

useradd -m -d /home/idiot -g idiots -p $(read -sp Password: pw ; echo $pw | openssl passwd -6 -stdin) -c "devops engineer" -u 1050 idiot

su - idiot

passwd idiot
```

### Password encryption

- https://docs.openssl.org/1.1.1/man1/passwd/


### openssl rand – Generate random numbers and passwords

```bash
openssl rand -hex 20

openssl rand -base64 20

openssl rand -out output.txt -base64 20
```

- https://www.misterpki.com/openssl-rand/

- https://docs.openssl.org/3.0/man1/openssl-rand/


## Add Multiple Users

- Create a `text` file named `user_list.txt`.

```txt
alice
bob
charlie
david
```

```bash
for i in `cat ./user_list.txt` ; do sudo useradd $i ; done
```

- https://phoenixnap.com/kb/linux-user-create


## Linux adduser Command with Examples

- open Ubuntu Server and run these commands

```bash
sudo adduser user1
```

```text
https://phoenixnap.com/kb/linux-adduser#:~:text=The%20adduser%20command%20in%20Linux,prompts%20when%20creating%20new%20accounts.
```


## How do I add new user AWS accounts with SSH access to my Amazon EC2 Linux instance?

```text
https://repost.aws/knowledge-center/new-user-accounts-linux-instance

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/describe-keys.html#retrieving-the-public-key
```

