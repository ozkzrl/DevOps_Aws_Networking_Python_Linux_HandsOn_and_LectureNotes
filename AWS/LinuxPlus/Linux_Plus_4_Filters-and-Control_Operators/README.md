# Hands-on Linux-05 : Filters and Control Operators
​
Purpose of the this hands-on training is to teach the students how to use filters and control operators in Linux.
​
## Learning Outcomes
​
At the end of the this hands-on training, students will be able to;
​
- Use filter commands.
​
- Pipe commands.
​
- Use Control operators.
​
## Outline
- Part 1 - ​stdin, stdout, and stderr on Linux?

- Part 2 - Using Filters
​
- Part 3 - Using Control Operators
​
## Part 1 - ​stdin, stdout, and stderr on Linux?

- Create a `text` file named `error.sh`.
​
```bash
#!/bin/bash
echo "About to try to access a file that doesn't exist"
cat bad-filename.txt

#The first line of the script echoes text to the terminal window, via the stdout stream. The second line tries to access a file that doesn't exist. This will generate an error message that is delivered via stderr.
```
- Make the script executable with this command:

```bash
chmod +x error.sh
```

- Run the script with this command:

```bash
./error.sh
```
- Redirect the output to a file:

```bash
./error.sh > capture.txt

#The error message that is delivered via stderr is still sent to the terminal window. We can check the contents of the file to see whether the stdout output went to the file.
```
```bash
cat capture.txt
```
- The > redirection symbol works with stdout by default. You can use one of the numeric file descriptors to indicate which standard output stream you wish to redirect.

- To explicitly redirect stdout, use this redirection instruction:

```bash
1>
```
- To explicitly redirect stderr, use this redirection instruction:

```bash
2>
```

```bash
./error.sh 2> capture.txt
```
- Redirecting Both stdout and stderr

```bash
./error.sh 1> capture.txt 2> error.txt
```
- Check the contents of each file:

```bash
cat capture.txt
cat error.txt
```
- Redirecting stdout and stderr to the Same File

```bash
./error.sh > capture.txt 2>&1

# > capture.txt: Redirects the stdout stream to the capture.txt file. > is shorthand for 1>.
# 2>&1: This uses the &> redirect instruction. This instruction allows you to tell the shell to make one stream got to the same destination as another stream. In this case, we're saying "redirect stream 2, stderr, to the same destination that stream 1, stdout, is being redirected to."
```

- Check the `capture.txt` file

```bash
cat capture.txt
```

## Part 2 - Using Filters
​
**cat**

- concatenate files and print on the standard output
​
- Create a folder and name it filters.
​
```bash
mkdir filters
cd filters
```
- Create a `text` file named `days.txt`.
​
```bash
vim days.txt
```
​
```bash
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
```
- Display the content of days.txt.
```bash
cat days.txt
```
- Show what cat command does when used in a pipe.
​
```bash
cat days.txt | cat | cat | cat | cat
```
- Create a `text` file named `count.txt`.
​
```bash
nano count.txt
```
```text
one
two
three
four
five
six
seven
eight
nine
ten
eleven 
```
- Display the content of count.txt.

```bash
cat count.txt
```

**tee**

- Read from standard input and write to standard output and files
​
- Write the content of the count.txt file in reverse order to another file named temp.txt and display the content of temp.txt in reverse order.

```bash
tac count.txt | tee temp.txt | tac
```
- Check whether the temp.txt file created and display the content.
​
```bash
ls
cat temp.txt
```

**Append to the Given File -a or --append**

- It basically do not overwrite `temp.txt` file but append to `temp.txt` file

```bash
wc -l count.txt | tee -a temp.txt
```

- Write to Multiple File

```bash
ls -lh | tee file1.txt file2.txt file3.txt
```

**grep**
​
- Print lines that match patterns. The most common use of grep is to filter lines of text containing (or not containing) a certain string.

- Create a `text` file named `tennis.txt`.
​
```bash
cat > tennis.txt
​
Amelie Mauresmo, Fra
Justine Henin, BEL
Serena Williams, USA
Venus Williams, USA
```
>**press ctrl+d for EOF**
​
- Display the content of tennis.txt.

```bash
cat tennis.txt
```

- Display only the lines of tennis.txt that includes 'Williams'.
​
```bash
cat tennis.txt | grep Williams
```

- Display only the lines of tennis.txt that includes 'us'.
​
```bash
cat tennis.txt | grep us
```

- Display the owners column (3rd column) of all the files in current directory.
​

**cut**

- The cut filter can select columns from files, depending on a delimiter or a count of bytes (It can be used to cut parts of a line by delimiter, byte position, and character)

```bash
ls -l | cut -d' ' -f3
```

- Display the content of /etc/passwd directory.
​
```bash
cat /etc/passwd
```

- Display only the usernames.
​
```bash
cut -d: -f1 /etc/passwd
```

```bash
cut -d: -f1-3 /etc/passwd
```

- other examples

- Create a `text` file named `city.txt`.
​
```bash
nano city.txt
```

```text
New York
Los Angeles
San Francisco
Mexico City
Buenos Aires
Rio de Janeiro
Cape Town
Las Vegas
Kuala Lumpur
Hong Kong
```

```bash
cut -c1 city.txt

cut -c 1,2,4 city.txt

cut -c 1-3 city.txt

cut -c 1-3,6-8 city.txt

cut -b 1-3 city.txt
```

- In Linux, the cut command uses the -b (byte) and -c (character) flags. UTF-8 is an example of a multibyte character set. UTF-8 represents some characters with multiple bytes, especially non-Latin alphabets and special symbols, which typically require more than one byte.

- For example, although these characters appear as a single character, they correspond to multiple bytes:

```text
"ç" (Turkish character): 2 bytes
"ğ" (Turkish character): 2 bytes
"😊" (emoji): 4 bytes
"你" (Chinese character): 3 bytes
"€" (Euro symbol): 3 
```

**tr**
​
- The command 'tr' stands for 'translate’. It is used to translate, like from lowercase to uppercase and vice versa or new lines into spaces.

- Create a `text` file named `clarusway.txt`.
​
```bash
cat << EOF > clarusway.txt
Clarusway:Road to reinvent yourself.
EOF
```

- Display the content of clarusway.txt.
​
```bash
cat clarusway.txt
```

- In the content of clarusway.txt, replace or translate aer letters with 'QAZ'.
​
```bash
cat clarusway.txt | tr aer QAZ
```
​
- Write the content of count.txt on the same line.
​
```bash
cat count.txt | tr '\n' ' '
```
​
- Delete all the vowels in the content of clarusway.txt.
​
```bash
cat clarusway.txt | tr -d aeiou
```
​
- Write the whole content of clarusway.txt in capital letters.
​
```bash
cat clarusway.txt | tr [a-z] [A-Z]
```

**wc**
​
- Print line, word, and charecters for each file.

- Count the lines, words and letters of the content of count.txt.
​
```bash

wc count.txt

wc count.txt days.txt
```

- Find how many users are there in the computer.

```bash
wc -l /etc/passwd
```

**sort**
​
- The sort filter will default to an alphabetical sort. The sort filter will default to an alphabetical sort.

- Create a `text` file named `marks.txt`.
​
```bash
cat << EOF > marks.txt
aaron   70
julia   80
albert  90
james   60
kate    60
john    80
oliver  75
tom     54
victor  30
walter  60
jane    100
EOF
```

- Display the content of marks.txt.
​
```bash
cat marks.txt
```

- Sort the content of marks.txt.
​
```bash
sort marks.txt
```

- Sort the content of marks.txt in reverse order.
​
```bash
sort -r marks.txt
```

- Sorts files and directories in alphabetical order by their names (use the ninth column for sorting)
​
```bash
ls -l | sort -k9
```

**uniq**
​
- report or omit repeated lines. With the help of uniq command you can form a sorted list in which every word will occur only once.

- Create a `text` file named `trainees.txt`.
​
```bash
cat << EOF > trainees.txt
john
james
aaron
oliver
walter
albert
james
john
travis
mike
aaron
thomas
daniel
john
aaron
oliver
mike
john
EOF
```

- Display the content of trainees.txt.
​
```bash
cat trainees.txt
```

- Display only the unique names in the content of trainees.txt.
​
******before using uniq command, the file must be sorted******
​
```bash
sort trainees.txt | uniq
```

- Prefix lines by the number of occurrences

```bash
sort trainees.txt | uniq -c
```

- Display only duplicate lines

```bash
sort trainees.txt | uniq -d
```

**comm**

- Compare two sorted files line by line. By default, `comm` will always display three columns. 
First column indicates non-matching items of first file, second column indicates non-matching items 
of second file, and third column indicates matching items of both the files. 

- Both the files has to be in sorted order for 'comm' command to be executed.
​
- Create a `text` file named `file1.txt`.
​
```bash
cat << EOF > file1.txt
Aaron
Bill
James
John
Oliver
Walter
EOF
```

- Create another `text` file named `file2.txt`.
​
```bash
cat << EOF > file2.txt
Guile
James
John
Raymond
EOF
```

- Compare file1.txt and file2.txt.
​
******before using comm command, files must be sorted******
​
```bash
comm file1.txt file2.txt
```

- EXERCISE:
​
  - Create a file named `countries.csv`.
​
```bash
cat << EOF > countries.csv
Country,Capital,Continent
USA,Washington,North America
France,Paris,Europe
Canada,Ottawa,North America
Germany,Berlin,Europe
EOF
```
  - Cut only 'Continent' column | Remove header | Sort the output | List distinct values | Save it to 'continent.txt' and display on the screen.
​
```bash
********************************
```
## Part 2 - Using Control Operators
​
>**;**
​
- More than one command can be used in a single line with `;`.

- Write two seperate cat command on the same line using ;.
​
```bash
cat days.txt ; cat count.txt 
```

```bash
echo Hello ; echo World! 
```

>**&**

- When a line ends with an ampersand &, the shell will not wait for the command to finish. You will get your shell prompt back, and the command is executed in background. You will get a message when this command has finished executing in background.
​
- Run sleep 10 command and show that the kernel is busy until the process of this command ends.
​
```bash
sleep  10
```

- Run sleep 20 command and let this command work behind while you're running other commands.
​
```bash
sleep  20 &
ls -l
cat count.txt
cat days.txt
```

>**$?**
​
- This control operator is used to check the status of last executed command. If status shows '0' then command was successfully executed and if shows '1' then command was a failure.

- Run ls command and show that it is executed successfully.
​
```bash
ls
echo $?
```

- Run lss command and show that it failed.
​
```bash
lss
echo $?
```

Exit Code | Meaning |
|:-------:|---------|
|1| Catchall for general errors
|2| Misuse of shell builtins
|126| Command invoked cannot execute
|127| Command not found
|128| Invalid argument to exit
|128+n| Fatal error signal "n"
|255| Exit status out of range (exit takes only integer args in the range 0 - 255)

- Bash command line exit codes 

```bash
https://www.redhat.com/sysadmin/exit-codes-demystified
```

>**&&**

- The command shell interprets the && as the logical AND. When using this command, the second command will be executed only when the first one has been successfully executed.
​
- Display days.txt and if it runs properly display count.txt.
​
```bash
cat days.txt && cat count.txt
```

- Display days.text and if it runs properly display count.txt.
​
```bash
cat days.text && cat count.txt
```

>**||**

- The command shell interprets the (||) as the logical `OR`. This is opposite of logical `AND`. Means second command will execute only when first command will be a failure.
​
- Display days.txt or write 'clarusway' on the screen, then write 'one'.
​
```bash
cat days.txt || echo clarusway ; echo one
```

- Write 'first' or write 'second' on the screen, then write 'third'.
​
```bash
echo first || echo second ; echo third
zecho first || echo second ; echo third
```

>**&& and ||**

- We can use this logical AND and logical OR to write an if-then-else structure on the command line. This example uses echo to display whether the rm command was successful.
​
- Make a copy of file1.txt and named it file11.txt.
​
```bash
cp file1.txt file11.txt
```
- Delete file11.txt and write a message if it is deleted properly.
​
```bash
rm file11.txt && echo 'it worked' || echo 'it failed'
```
- Run the last command again.
​
```bash
rm file11.txt && echo 'it worked' || echo 'it failed'
```

>**#**

- Everything written after a pound sign (#) is ignored by the shell. This is useful to write a shell comment but has no influence on the command execution or shell expansion.​

- Run the echo command and add a comment line.
​
```bash
echo '# is the comment sign' # echo command displays the string comes after it.
echo # is the comment sign
echo \# is the comment sign
```

>** \ **

- Lines ending in a backslash are continued on the next line. The shell does not interpret the newline character and will wait on shell expansion and execution of the command line until a newline without backslash is encountered.

- Escaping characters are used to enable the use of control characters in the shell expansion but without interpreting it by the shell.
​
- Run a single command on multipe lines.
​
```bash
echo this command is written \
not only on a single line \
but also on multiple lines.
```
- Write the following sentence on the screen: The special characters are *, \, ", #, $, '.
​
```bash
echo The special characters are \*, \\, \", \#, \$, \'.
```

- EXERCISE:
​

  1.a. Search for “clarusway.doc” in the current directory

    b. If it exists display its content
  
    c. If it does not exist print message “Too early!”
  
  2.Create a file named “clarusway.doc” that contains “Congratulations”

  3.Repeat Step 1
​
```bash
********************************
```

### BONUS PART
## Aliases

```bash
alias ls="ls -al"				

alias pl="pwd; ls"

alias dir="ls -l | grep ^d"

alias lmar="ls –l | grep Mar"

alias wpa="chmod a+w"

alias tell="whoami; hostname; pwd"

alias d="df -h | awk '{print $6}' | cut -c1-4"
```

```txt
- User = /home/user/.bashrc or ~/.bashrc

- Global = /etc/bash.bashrc or /etc/profile
```