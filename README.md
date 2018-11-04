# Log Analysis

By Vinicius Conceição

This is an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.
This tool runs in the terminal.

#### The questions of the reporting tool are:
**1. What are the most popular three articles of all time?**

**2. Who are the most popular article authors of all time?**

**3. On which days did more than 1% of requests lead to errors?**

# Required Libraries and Dependencies
- Python 2.X
- Vagrant
- Virtual Box


# Setting the enviroment

 - You can download and unzip this file: [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) 
This will give you a directory called FSND-Virtual-Machine. 
Or, you can use Github to fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm.

- Access the new directory created with your terminal

- Navigate to the directory vagrant using the command: `cd /vagrant` 

- Inside the vagrant subdirectory, run the command `vagrant up`. This will configure and set the virtual machine to be ready for use.

- At this point, you can run `vagrant ssh` to log in the VM.

- With the VM up and running, go back to your browser and download the [news data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) that you will be using in the project.

- Set the directory for the downloaded file or copy and unzip it to the VM directory **FSND-Virtual-Machine\vagrant**

- Back to the terminal, you can now import the news data that you downloaded running the command `psql -d news -f newsdata.sql`

- To test the database, type the command `\dt`- *to lists the tables that are available in the database*.
    - To exit the database, type the command `\q`

**Don't close the the terminal yet...**

# Running the project

- Download the project zip file to your computer
OR
Clone this repository to your computer

- Copy or Move the file/folder of the project to the VM directory **FSND-Virtual-Machine/vagrant.**

 - Back to the virtual machine terminal that you opened before.

- Navigate to the project directory and type in the following command:
 `python log_database.py`

# Miscellaneous

There is a file with the output of the report called **output.txt**









