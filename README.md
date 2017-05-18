# Logs

## Introduction
Developed a python module to interact with databse and retrieve useful information.

## Files Included
* analysis.sql: This file contains all the views created requird for information retrieval.
* analysis.py : This file contains all the three functions to get required output.

## Steps To Run The Application:
1. Use terminal for Mac or Linux and Git Bash for Windows to run the application.
2. From the given link, install VirtualBox : https://www.virtualbox.org/wiki/Downloads
3.  From the given link, install Vagrant : https://www.vagrantup.com/downloads.html
4. Now, start the virtual machine by using `vagrant up` command and copy both files into /vagrant/logs directory.
5. After you have downloaded all the necessary files, login to the Linux Vm using `vagrant ssh` command.
6. Now, change the directory to the cloned folder by using following command : `cd /vagrant/logs`
7. Run 'psql' command and import the given sql file using this command: `\i analysis.sql` to your database.
8. Run the file using this command: `python analysis.py`
