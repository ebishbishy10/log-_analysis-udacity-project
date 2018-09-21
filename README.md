# Log-Analysis-Udacity-Project
An internal reporting tool that uses information of large database of a web server and draw business conclusions from that information.
(Project from [Full Stack Web Development Nanodegree](https://in.udacity.com/course/full-stack-web-developer-nanodegree--nd004/))

## Introduction
This is a python module that uses information of large database of a web server and draw business conclusions from that information. The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. The database includes three tables:
* The **authors** table includes information about the authors of articles.
* The **articles** table includes the articles themselves.
* The **log** table includes one entry for each time a user has accessed the site.

#### The project drives following conclusions:
* Most popular three articles of all time.
* Most popular article authors of all time.
* Days on which more than 1% of requests lead to errors.

### Functions in tool.py:
* **connect():** Connects to the PostgreSQL database and returns a database connection.
* **topviews():** Prints most popular three articles of all time.
* **topauthors():** Prints most popular article authors of all time.
* **error_percentage():** Print days on which more than 1% of requests lead to errors.

## Instructions
* To run this module succesfully make sure that you install:
    *[python](https://www.python.org/downloads/)
    *[psycopg2 module](http://initd.org/psycopg/download/)
    *[Postgresql](https://www.postgresql.org/download/)
    *[newsdata](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
* Install [https://www.vagrantup.com/downloads.html] and [https://www.virtualbox.org/wiki/Downloads] 
* Clone the repository to your local machine:</h4>
  git clone [https://github.com/ebishbishy10/log-_analysis-udacity-project.git]
* Start the virtual machine
  From your terminal, inside the project directory, run the command `vagrant up`. This will cause Vagrant to download the Linux           operating   system and install it.
  When vagrant up is finished running, you will get your shell prompt back. At this point, you can run `vagrant ssh` to log in to your     newly installed Linux VM!
* Download the [https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip]
  You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant           directory, which is shared with your virtual machine.
* Setup Database
  To load the database use the following command:
  `psql -d news -f newsdata.sql;`
* Run Module
  `python tool.py`
  
### Output:
![alt text](https://github.com/ebishbishy10/log-_analysis-udacity-project/blob/master/Screenshot.png)

