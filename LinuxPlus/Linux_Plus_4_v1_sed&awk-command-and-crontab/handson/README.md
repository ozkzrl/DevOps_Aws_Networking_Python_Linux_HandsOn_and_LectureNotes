# Hands-on Linux-10 : sed & awk command and crontab

Purpose of the this hands-on training is to teach the students how to use sed & awk command and crontab.

## Learning Outcomes

At the end of the this hands-on training, students will be able to;

- use sed & awk command and crontab.

## Outline

- Part 1 - sed command

- Part 2 - awk command

- Part 3 - crontab

- Part 4 - SCP – Secure Copy Protocol

## Part 1 - sed command

- Sed is a stream editor. A stream editor is used to perform a lot of function on a file like searching, find and replace, insertion or deletion.

- Create a folder and name it `sed-awk-command`.

```bash
mkdir sed-awk-command && cd sed-awk-command
```

- Create a file named `sed.txt`. 

```txt
Linux is an OS. Linux is life. Linux is a concept.
I like linux. You like linux. Everyone likes linux.
Linux is free. Linux is good. Linux is hope.
```

### Replacing or substituting string

The following sed command replaces the word “linux” with “ubuntu” in the file.

```bash
sed 's/linux/ubuntu/' sed.txt
```
- `s` specifies the substitution operation. 
- The `/` are delimiters. 
- The `linux` is the search pattern and the `ubuntu` is the replacement string.

**Output:**
```bash
Linux is an OS. Linux is life. Linux is a concept.
I like unutu. You like linux. Everyone likes linux.
Linux is free. Linux is good. Linux is hope.
```
> Pay attention that, by default, the sed command replaces the `first occurrence` of the pattern in each line.


### 

### Replacing the any occurrence of a pattern in a line 
Use the /1, /2 etc flags to replace the first, second occurrence of a pattern in a line. The following command replaces the third occurrence of the word “linux” with “ubuntu” in a line.

```bash
sed 's/linux/ubuntu/3' sed.txt
```

**Output:**
```bash
Linux is an OS. Linux is life. Linux is a concept.
I like linux. You like linux. Everyone likes ubuntu.
Linux is free. Linux is good. Linux is hope.
```

### Replacing a string by ignoring case distinctions.

By, default sed command do not ignore case distinctions. For this `i` pattern can be used.

```bash
sed 's/linux/ubuntu/i' sed.txt
```

**Output:**
```bash
ubuntu is an OS. Linux is life. Linux is a concept.
I like ubuntu. You like linux. Everyone likes linux.
ubuntu is free. Linux is good. Linux is hope.
```

#### Replacing all the occurrence of the pattern in a line 

`g flag` (global replacement) defines the sed command to replace all the occurrences of the string in the line.

```bash
sed 's/linux/ubuntu/g' sed.txt
```

**Output:**
```bash
Linux is an OS. Linux is life. Linux is a concept.
I like ubuntu. You like ubuntu. Everyone likes ubuntu.
Linux is free. Linux is good. Linux is hope.
```

- We can do the same by ignoring case distinctions. Use the combination of `/i` and `/g`.

```bash
sed 's/linux/ubuntu/ig' sed.txt
```

**Output:**
```bash
ubuntu is an OS. ubuntu is life. ubuntu is a concept.
I like ubuntu. You like ubuntu. Everyone likes ubuntu.
ubuntu is free. ubuntu is good. ubuntu is hope.
```

#### Replacing from any occurrence to all occurrences in a line

We can replace all the patterns from the any occurrence of a pattern in a line by using the combination of /1, /2 etc and /g. The sed command below replaces the second, third, and so on “linux” word with “ubuntu” word in a line.

```bash
sed 's/linux/ubuntu/2ig' sed.txt
```

**Output:**
```bash
Linux is an OS. ubuntu is life. ubuntu is a concept.
I like linux. You like ubuntu. Everyone likes ubuntu.
Linux is free. ubuntu is good. ubuntu is hope.
```

#### Replacing string on a specific line number

We can limit the sed command to replace the string on a specific line number. The following command only replaces the second line.

```bash
sed '2 s/linux/ubuntu/ig' sed.txt
```

**Output:**
```bash
Linux is an OS. Linux is life. Linux is a concept.
I like ubuntu. You like ubuntu. Everyone likes ubuntu.
Linux is free. Linux is good. Linux is hope.
```

- Create a `text` file named `life.txt`. 

```txt
life isn't meant to be easy, life is meant to be lived.

Try to learn & understand something new everyday in life.
Respect everyone & most important love everyone.

Don’t hesitate to ask for love & don’t hesitate to show love too.
Life is too short to be shy.

In life, experience will help you differentiating right from wrong.

#Embrace every moment, for life is a collection of memories.
#Don’t dwell on mistakes; use them as stepping stones to grow.
Keep kindness at the core of your actions; it’s what makes life fulfilling.

```

- Create a `text` file named `names.txt`.
​
```txt
James Anderson
Sarah Johnson
Michael Brown
Emily Davis
David Wilson
Jessica Miller
Daniel Moore
Laura Taylor
Ashley White
```

# Delete lines that contain the word "life" from the file life.txt

```bash
sed '/life/d' life.txt
```
- Deletes all lines in life.txt that contain the word "life", regardless of case (for example, "life," "Life," "LIFE," etc.)

```bash
sed '/life/Id' life.txt
```
-  Delete all empty lines (lines with no content) in the life.txt file

```bash
sed '/^$/d' life.txt
```

- Delete lines that start with the hash symbol (#), which is commonly used to denote comments in many configuration files or scripts

```bash
sed '/^#/d' life.txt
```

- Delete empty lines and lines that start with a # symbol

```bash
sed '/^$/d;/^#/d' life.txt
```

- Replace all spaces with tab characters (\t) in the names.txt file

```bash
sed 's/ /\t/g' names.txt
```

- Delete line 5 of life.txt

```bash
sed '5d' life.txt
```

- Delete a last line

```bash
sed '$d' life.txt
```

- Delete line from range x to y

```bash
sed '3,6d' life.txt
sed '3d;6d' life.txt
```

- Delete from nth to last line

```bash
sed '4,$d' life.txt
```

# View/Print the files (cat - tail - head alternative) 

- Viewing a file from x to y range (prints lines 2 through 5 of the names.txt file)

```bash
sed -n '2,5p' names.txt
```

- View the entire file except the given range

```bash
sed '2,5d' names.txt
```

- Sed Command in Linux/Unix with examples
```bash
https://www.geeksforgeeks.org/sed-command-in-linux-unix-with-examples/

https://www.geeksforgeeks.org/sed-command-linux-set-2/
```

## Part 2 - awk command

- Awk is a text pattern scanning and processing language, created by Aho, Weinberger & Kernighan (hence
the name). It searches one or more files to see if they contain lines that matches with the specified patterns and then performs the associated actions. 

- While the sed program works well with character-based processing, the awk program works well with delimited field processing.

- Create a file named `awk.txt`. 

```txt
This is line 1
This is line 2
This is line 3
This is line 4
This is line 5
```

### Syntax of awk command

> awk options 'selection _criteria {action }' file

- By default Awk prints every line of data from the specified file.

```bash
awk '{print}' awk.txt
```

**Output:**
```bash
This is line 1
This is line 2
This is line 3
This is line 4
This is line 5
```

### Print the lines which matches with the given pattern

```bash
awk '/This/ {print}' awk.txt
```

**Output:**
```bash
This is line 1
This is line 2
This is line 3
This is line 4
This is line 5
```

### Splitting a Line Into Fields

By default, the awk command splits the record delimited by a whitespace character.  Awk assigns some variables for each data field as below:

$0 for the whole line.
$1 for the first field.
$2 for the second field.
$n for the nth field.

```bash
awk '{print $2}' awk.txt
```

**Output:**
```bash
is
is
is
is
is
```

We can display more field. The example below only display two field.

```bash
awk '{print $2,$4}' awk.txt
```

**Output:**
```bash
is 1
is 2
is 3
is 4
is 5
```

- We can change delimiter by using –F option. First, update the awk.txt as below.

```txt
This is part 1 of line 1 : This is part 2 of line 1
This is part 1 of line 2 : This is part 2 of line 2
This is part 1 of line 3 : This is part 2 of line 3
This is part 1 of line 4 : This is part 2 of line 4
This is part 1 of line 5 : This is part 2 of line 5
```

- Let's separate the fields by `:`.

```bash
awk -F: '{print $2}' awk.txt
```

**Output:**
```bash
 This is part 2 of line 1
 This is part 2 of line 2
 This is part 2 of line 3
 This is part 2 of line 4
 This is part 2 of line 5
```

- We can use awk command as filter. 

```bash
ls -l | awk '{print $9}'
```

**Output:**
```bash
awk.txt
sed.txt
```

- We can find any string in any specific column. 

```bash
awk '{ if($7 == "3") print $0;}' awk.txt
```

**Output:**
```bash
This is part 1 of line 3 : This is part 2 of line 3
```

# First and last field
```bash
awk -F: '{print $1,$NF}' /etc/passwd
```

# With line number
```bash
awk -F: '{print NR, $0}' /etc/passwd
```

# Second last field
```bash
awk -F: '{print $(NF-1)}' /etc/passwd
```

# Custom string 
```bash
awk -F: '{print $1 "=" $6}' /etc/passwd
```

- Example 

```bash
ls -l | awk '{ if($7 == "27") print $9;}'
for i in $(ls -l | awk '{ if($7 == "24") print $9;}'); do rm "$i"; done
```

- AWK command in Unix/Linux with examples

```bash
https://www.geeksforgeeks.org/awk-command-unixlinux-examples/

https://quickref.me/awk
```
## Part 3 - crontab

- Crontab, stands for `cron table`, which is a list of commands scheduled to run at regular time intervals on the system. 

- If we need to schedule any task on Linux, we should basically edit the crontab file. We can do that using the below command.

```bash
crontab -e              # edit the crontab file
crontab -l              # list current cron tasks
crontab -u username -e  # edit other users's crontab file
```

- Editing the crontab file is not complex, but we should first learn how to set a date and time using 5 * on that file. There are six fields that we use on every cron task line. Those are explained in detail in the below picture.

![crontab format](./crontab-format.png)

- The quick and simple editor for cron schedule expressions

```bash
 https://crontab.guru/
 ```

- Let’s see few examples;

```bash
* * * * * <shell command>   # execute cron job every minute
0 1 * * * <shell command>   # execute cron job every day at 1 a.m.
* * * 1 * <shell command>   # execute every minute in January
* * * * 6 <shell command>   # execute every minute on every saturday
0 1,15 * jan,jun mon,fri <command> # execute at every 1 a.m. and 3
                                     p.m. every monday and friday on
                                     january and june
```

- We can also use some regular expressions to define the date part.

```bash
* = Any/All values           # e.g. *
- = Range of values          # e.g. 1-5 
, = Multiple/List of values  # e.g. 1,2,3
/ = Step values              # e.g. */3
```

- Finally let’s create some crontab tasks. Create a cron task writes the system date information every day at 1 p.m. to the date.log file.

```bash
crontab -e
* * * * * date >> /home/ec2-user/date.log
```

- Create a cron task updates and upgrades our server every Sunday at 3 a.m.

```bash
0 3 * * sun sudo yum update -y
```

-  List the cron tasks.

```bash
crontab -l
```


# Installing CronTab on Amazon Linux 2023 EC2

- Step 1: Install the ‘cronie’ package.

```bash
sudo yum install cronie -y
```
- Step 2: Enable the ‘cronie’ service.

```bash
sudo systemctl enable crond.service
```
- Step 3: Start the ‘cronie’ service.

```bash
sudo systemctl start crond.service
```

- The status of the ‘cronie’ service should now reflect as ‘active’:

```bash
sudo systemctl status crond | grep Active
 Active: active (running) since Tue 2023-04-11 16:47:06 UTC; 18s ago
```


# Send Alerts To Slack With Bash Shell Script

- https://easyoradba.com/2018/10/29/send-alerts-to-slack-with-bash-shell-script/

-  Create an APP in Slack

1. Go to https://api.slack.com/slack-apps

2. Go to Your Apps

3. Create New App
```bash
- From Scratch
- App Name : crontab-demo
- Pick a workspace to develop your app in: AWS 19/TR
```

4. Create the Slack App and a webhook
```bash
 - Go to incoming webhooks and Activate incoming webhooks
 - Add New Webhook to Workspace > 
 - You can see the sample of your webhook cURL then
   forexample: " curl -X POST -H 'Content-type: application/json' --data '{"text":"Hello, World!"}' https://hooks.slack.com/services/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 "
                 
```

```bash
today_date=$(date +"%Y_%m_%d_%H_%M") #(date "+%Y-%m-%d")
messages="Successful process....! $today_date - backup is ready"
curl -X POST -H 'Content-type: application/json' --data "{\"text\":\"$messages\"}" https://hooks.slack.com/services/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
```

## Part 4 - SCP – Secure Copy Protocol

- scp (secure copy) command in Linux system is used to copy file(s) between servers in a secure way. The SCP command or secure copy allows the secure transferring of files between the local host and the remote host or between two remote hosts.

```bash
scp [file_name] remoteuser@remotehost:/remote/directory
```

```txt
file_name = The name of the file that needs to be copied.
remoteuser =The username of the remote host.
remotehost = The IP address or hostname of the remote host.
/remote/directory = The directory where the file should be copied on the remote machine.
```

# Local to Remote server

```bash
echo "Hello World" > test.txt

scp -i "key.pem" test.txt ec2-user@<public_ip>:/home/ec2-user/
```


# Remote to Local server


```bash
echo "Hello World" > test.txt

scp -i "key.pem" ec2-user@<public_ip>:/home/ec2-user/test1.txt .
```


# Download the folder in EC2 (with its subfolders and files) to local;

```bash
scp -r Directory_name user@hostname:destination_file

scp -i "pemkey" -r ec2-user@<public_ip>:/home/ec2-user/Project .
```

```txt
pemkey = type your own key with pem extension
-r = this flag is used to copy an entire directory and its contents.
.(dot) = copies these files to your current location
```

- How to Securely Copy Files in Linux | scp Command

```bash
https://www.geeksforgeeks.org/scp-command-in-linux-with-examples/
```