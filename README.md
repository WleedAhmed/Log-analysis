# Logs Analysis
_A project for Udacity Full Stack Nanodegree._

## About the project:
I was asked to build an internal reporting tool that will use information from the database of a newspaper site to discover what kind of articles the site's readers like. 

## To Run the code:
You will need **Python2**, **Vagrant** and **VirtualBox** installed on your computer. once you have them, you are ready for setup.

## Setup
**1 - The VM:** 
if you don't have the folder FSND-Virtual-Machine, download and unzip the file here: 
[FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip)
This will give you a directory called FSND-Virtual-Machine. It may be located inside your Downloads folder.

**2 - Project files:**
[download the data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory in the directory you dowloaded in **step 1.**

**3 - Launch Vagrant VM:** 
Using your terminal, cd to the vagrant directory and run the command `vagrant up`. When `vagrant up` is finished running, log in into your VM with `vagrant ssh`.

**4 - To load the data:** 
To do so `cd` into the vagrant directory and use the command `psql -d news -f newsdata.sql`.

**5- To execute the program:** 
Run `python log_analysis.py`.
