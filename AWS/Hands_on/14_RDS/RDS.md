# Hands-on DB-01 : Configuring and Connecting RDS with Console and Workbench

Purpose of the this hands-on training is to configure RDS Instance via AWS Management Console and connect from MySQL Workbench.

## Learning Outcomes

At the end of the this hands-on training, students will be able to;

- learn how to set configuration of RDS Instance on console.

- learn how to connect to RDS via workbench.

- learn how to manipulate RDS Instance.

## Outline

- Part 1 - Creating RDS Instance on AWS Management Console

- Part 2 - Configuring MySQL Workbench to connect to the RDS Instance

- Part 3 - Manipulating RDS Instance

## Part 1 - Creating RDS Instance on AWS Management Console

- First, create Security Group for RDS service. Select EC2 dashboard. Select Security Groups from the left-hand menu.

```text
Security Group Name: aws_db_sg
Description: aws_db_sg
VPC: Default
Inbound Rules:
    - Type: MYSQL/AURORA ---> Source: MyIP
Outbound Rules: Keep it as it is
```

- Go to the Amazon RDS Service and select Database section from the left-hand menu, click databases and then click Creating Database.

- Choose a database creation method.

```text
Standard Create
```

- Engine option

```text
MySQL
```

- Version

```text
8.0.25
```

- Template

```text
Free tier
```

- Settings

```text
DB instance identifier: RDS-mysql
Master username: admin
Master password: Pl123456789
```

- DB instance class

```text
Burstable classes (includes t classes) : db.t3.micro
```

- Storage

```text
Storage type              : ssd
Storage size              : default 20GiB
Storage autoscaling       : default
Maximum storage threshold : 22 
```

- Connectivity

```text
VPC                           : default

Click Additional Connectivity Configuration;

Subnet group                  : default
*Publicly accessible          : ***Yes
Existing VPC security groups  : Select security group named aws_db_sg
Availability Zone             : No preference
Database port                 : 3306
```

- Database authentication

```text
DB Authentication: Password authentication
```

- Additional configuration

```text
Initial DB name                   : aws_demo
DB parameter group & option group : default
Automatic backups                 : enable
Backup retention period           : 7 days (Explain how)

Select window for backup to show snapshots
Monitoring  : Unchecked
Log exports : Unchecked

Maintenance
  - Enable auto minor version upgrade: Enabled (Explain what minor and major upgrade are)
  - Maintenance window (be careful not to overlap maintenance and backup windows)

Deletion protection: *Enabled
```

- Estimated monthly costs
Show that when you select `production` instead of `Free Tier Template` it charges you.

- Click `Create Database` button

- Go to database menu and select `RDS-mysql` database and show and explain sub-sections (Connectivity & Security, Monitoring etc.)

- Show the Automatic backup also.

- Show Modify button

- Show action button (restore,take snapshots, etc.)

## Part 2 - Configuring MySQL Workbench to connect to the RDS Instance

- First, go to the Amazon RDS Service, select `Database` section from the left-hand menu, click databases and select `RDS-mysql`. Then, copy the `endpoint` at the bottom of the page.

- Open the MySQL Workbench and click `+` to configure a new MySQL connection.

On the page opened, we'll set up a new connection:

```text
1. Connection Name   : first connection.

2. Host Name         : Paste the endpoint of the database that you have copied 
                       and leave the port as is, 3306

3. Username          : Here we enter the user name that we determined while creating the DB instance.
                       So we enter "admin" as a username.

4. Password          : Click the `Store in Keychain/Vault` and enter the password 
                       that you determined as "Pl123456789" while creating the DB Instance.

5. Test Connection   : Before you connect DB Instance, test the connection whether it works properly.
                       So, click `Test Connection` tab.

6. If the connection is set properly, you'll see the successfully message

7. Then click `OK` to complete the configuration
```

## Part 3 - Manipulating RDS Instance

- Show `aws` database that is created together with RDS DB instance creation.

- Create a new database from "Schema" tab

- To modify the database, first, we need to create a new table. So, click the `aws` schema (or your schema's name). Right-click the `Table` option, then select the `Create Table`, and enter `Personal_Info_1` as table name.

```text
1. First Row: Type "ID_number" into the first line. 
              ID number is an integer, so the system automatically assign Integer value to the Datatype column.
              Explain the Primary Key, choose the ID_number as a Primary Key, and check the PK box.

3. Second Row: type "Name" into the second row.VARCHAR(45)

4. Third Row: type "Surname" into the third row.VARCHAR(45)

5. Fourth Row: type "Gender" into the fourth row.VARCHAR(45)

6. Fifth Row : type "Salary" into the fifth row.VARCHAR(45)

After that click `Apply` at the bottom of the row.

Then a window that shows the review of the table pops up on the screen. Click Apply, if it's OK.
```

- Add another table via SQL command:

```sql
CREATE TABLE `aws_demo`.`Personal_Info_2` (
  `ID_number` INT NOT NULL,
  `Name` VARCHAR(45) NULL,
  `Surname` VARCHAR(45) NULL,
  `Gender` VARCHAR(45) NULL,
  `Age` INT NULL,
  `Department` VARCHAR(45) NULL,
  PRIMARY KEY (`ID_number`));
```

- Then refresh the "Table" tab to see newly created tables

- Add data to the "Personal_Info" table as shown below:

```sql
INSERT INTO aws_demo.Personal_Info_1
(ID_number, Name, Surname, Gender, Salary)
VALUES
('1234','Osvaldo','AWS','Male','45000'), 
('56789','Guile','AWS','Male','55000'), 
('007','Charlie','AWS','Male','50000'), 
('432','Marcus','AWS','Male','55000'), 
('324','Vincenzo','AWS','Male','65000'),
('4587','Aslan','AWS','Male','40000'), 
('43546','Serdar','AWS','Male','70000');
```

- Write a query to show all data in the `Personal_Info_1` table

```sql
SELECT * FROM aws_demo.Personal_Info_1;
```

- Write a query to show the personal whose salary are higher than 40K in the `Personal_Info_1` table

```sql
 SELECT * FROM aws_demo.Personal_Info_1 WHERE salary > 40000;
```




- Try to delete RDS and show that RDS instance can not be deleted because of the `Deletion Protection`.

- Modify DB instance for "Disabling Deletion Protection"

- Try to delete RDS and show that RDS instance again.

   -Show that "Create final snapshot?" option should be "Unchecked"

              "I acknowledge...." flag is "Checked"

- Type "delete me" nad Click "Delete".

- Show that Automated Backups are deleted also.
