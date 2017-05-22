# Logs

## Introduction
Developed a python module to interact with database and retriev useful information.

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


## Views used:
1) create view author_view as select title,count(title) as views from log,articles where path=concat('/article/',articles.slug) group by title order by views desc;
2) create view author_view1 as select authors.id, articles.title from authors, articles where articles.author = authors.id;
3) create view author_view2 as select author_view1.id, author_view1.title, author_view.views from author_view1, author_view where author_view1.title = author_view.title;
4) create view error_view1 as select time::timestamp::date, count(status) as total from log group by time::timestamp::date order by time::timestamp::date;
5) create view error_view2 as select time::timestamp::date, count(status) as fault from log where status = '404 NOT FOUND' group by time::timestamp::date;
6) create view error_view3 as select error_view1.time, (fault::float * 100)/( total::float) as error_percent from error_view1, error_view2 where error_view1.time = error_view2.time;
