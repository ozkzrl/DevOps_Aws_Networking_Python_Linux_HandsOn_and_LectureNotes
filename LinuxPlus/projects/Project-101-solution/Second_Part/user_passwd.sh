#!/bin/bash
#
# This script creates a new user on the local system.
# You will be prompted to enter the username (login), the person name, and a password.
# The username, password, and host for the account will be displayed.

# Make sure the script is being executed with superuser privileges.
if [[ ${UID} -ne 0 ]]
then
    echo "Please run this script with sudo or root"
    exit 1
fi

# Get the username (login).
read -p "Enter the username to create : " USER_NAME

# Get the real name (contents for the description field).
read -p "Enter the person/application role (Title - Devops Engineer, Backend Developer) : " COMMENT


# Get the password.
# read -sp "Enter the password to use for the account :" PASSWORD
PASSWORD=$(openssl rand -base64 20)

# Create the account.
useradd -m -c "${COMMENT}" -p $(echo $PASSWORD | openssl passwd -6 -stdin) ${USER_NAME} 


# Check to see if the useradd command succeeded.
# We don't want to tell the user that an account was created when it hasn't been.

if [[ "${?}" -eq 0 ]]
then
    echo -e "\nThis username and password have been successfully added."
    echo "Here : $(tail -1 /etc/passwd)"
else
    echo "This username is already exists. Please select different username."
    exit 1
fi


# Force password change on first login.
passwd -e ${USER_NAME}


# Display the username, password, and the host where the user was created.
echo
echo "Username"
echo "${USER_NAME}"

echo
echo "Password"
echo "${PASSWORD}"