# Berea Farmer's Market

This system was developed in order to increase the efficiency in which the Berea Farmer's Market staff recorded their sales. Prior to the creation of this system all sales were recorded through paper forms and manually inserted into an excel spreadsheet. By developing this web system we have drastically decreased the amount of time that is required to collect and record the sales for each market.

## Built With

* [Flask](http://flask.pocoo.org/docs/0.11/)  - Python Based Web Framework Used
* [Jinja2](http://jinja.pocoo.org/docs/dev/) - HTML Templating Language for Python
* [Peewee](http://docs.peewee-orm.com/en/latest/index.html) - A small, expressive ORM used for database communications
* [SQLite](https://sqlite.org/) - SQL database engine

# Setting Up a Development Environment
### Getting Started On Cloud9 ###
[Cloud9](https://c9.io/?redirect=0) is the preferred tool for our software team while developing and debugging code. However, if you are new to cloud9, they did just recent start requiring a credit card to create an account. Therefore you may not want to use cloud9 as your development environment.  

### Create a Workspace with Bitbucket using SSH Protocol

When you first log into your cloud9 account, select the tab that says **workspaces**. After you open this tab you should see an option to create a new workspace, it should look like the image below.

![creatework.PNG](https://bitbucket.org/repo/bEXb4L/images/4213557604-creatework.PNG) 

After you click the button go ahead and input a name and description for this workspace.

![description.PNG](https://bitbucket.org/repo/bEXb4L/images/2446581179-description.PNG)
![public.PNG](https://bitbucket.org/repo/bEXb4L/images/69137571-public.PNG)

>***Note:*** 
The default for the workspace is to be public, it's important to **NOT** change this default option. The way that our system works is that it creates a virtual environment for the application to run on. The virtual environment requires the use of ports in order to access the application. If you may the workspace private, it can block these ports so that they can not be accessed. There may be a way around this; however, we just find it easier if you let the workspace be public. 

Next, you will want to make sure you choose to clone your repo from bitbucket. You do this by adding your git URL using the SSH.

For Example:
```git@bitbucket.org:<username>/<name_of_Repo>.git```

If you are uncertain what your git ssh URL is you can find it at the top of the bitbucket page if you click the clone option. 

![git clone.PNG](https://bitbucket.org/repo/bEXb4L/images/340042303-git%20clone.PNG)

>***Note***: If you copy and paste this line make sure to remove the ```git clone``` at the front in order to ensure you only get the URL.

After you have entered in the URL, the last portion of the page asked you to choose a template. Please select the python option in order to have the workspace to run correctly. 

![PYTHON.PNG](https://bitbucket.org/repo/bEXb4L/images/3923875225-PYTHON.PNG)

All that is left is to hit the create workspace button and your workspace will be configured correctly. 

### Getting Your Development Environment Running

After you have created your workspace, there are three additional steps that you will have to complete before your virtual environment will be completely operational. 

**Step One: Activate Your Virtual Environment**

In order to do this, all you have to do is type: ```source setup.sh``` into the Linux terminal. You might have to wait a minute or two as the tools you need for our application are downloaded into your virtual environment. However, after the setup is completed you should see the words ```(venv)``` at the front of your terminal.

![venv.PNG](https://bitbucket.org/repo/bEXb4L/images/2846617267-venv.PNG) 

>***Note:*** 
In order for the application to work, you must activate the virtual environment. If you are not inside of the virtual environment you will see this error:
![venvError.PNG](https://bitbucket.org/repo/bEXb4L/images/1415469357-venvError.PNG)Whenever you get this error just activate the virtual environment again by entering the command ```source setup.sh```

>Also, If you ever want to deactivate the virtual environment for any reason just type ```deactivate``` into the terminal. 
![deactivate.PNG](https://bitbucket.org/repo/bEXb4L/images/2248015321-deactivate.PNG) 


**Step Two: Setup Your Database**

A couple of elements are necessary in order to get your database established. The first step is creating the SQLite file, we can create the file in the desired location through the use of one of our scripts.

**Create Database**

By typing the command ```python reset-db.py``` a database file containing the correct schemas will be created in the data directory with the name ```bfm.sqlite```.

**Populate Database**

The ```reset-db.py``` will only create empty tables for you, in order to populate the database you will need to execute the command: ```python add_dummy.py```. This file will add dummy data to the system so that you can gauge how the system is supposed to run.

**How to View the Database** 

Now that you have the database created and populated with data, you are probably asking yourself how do I see that? Our system development team likes to use a tool called [DB Browser](http://sqlitebrowser.org/). This tool is a visual way of viewing and editing SQLite database files. 

![dbBrowser.PNG](https://bitbucket.org/repo/bEXb4L/images/3023751797-dbBrowser.PNG)
 

**Step Three: Running the Application**

The only remaining step to getting your development environment deployed is running the actual application. This can be achieved through the command ```python run.py```, when you run this command you should see a URL created for you. 

![run.PNG](https://bitbucket.org/repo/bEXb4L/images/1543001500-run.PNG)

The URL will take you to the application and allow you to see any changes you make to the system. That's all that has to be done in order to get the development environment created and ready for editing. 

![application.PNG](https://bitbucket.org/repo/bEXb4L/images/2789264337-application.PNG)

# Deployment: Setting Up an Ubuntu Server for Production

**Disclaimer:** At this point I think it's important to note that this section is not a step by step solution for how a system administrator should set up a Linux server. Tasks such as setting up SSL and HTTPS, setting up user groups and permissions, and other things of this nature should be completed by your system administrator. However, this portion of our READme.md does provide what additional steps your system administrator will have to complete in order to get the system operational.

**Required Tools:**

1) [Apache2](https://help.ubuntu.com/lts/serverguide/httpd.html) - `sudo apt-get install apache2`

2) [Python-Pip](https://pip.pypa.io/en/stable/) - `sudo apt-get install python-pip`

3) [Virtualenv](https://virtualenv.pypa.io/en/stable/) - `sudo apt-get install virtualenv`

4) [WSGI](http://flask.pocoo.org/docs/0.11/deploying/mod_wsgi/) - `sudo apt-get install libapache2-mod-wsgi`

5) [Flask](http://flask.pocoo.org/docs/0.11/) - `sudo pip install Flask`

**Recommended Tool:**

1) [Unattended-Upgrades](https://help.ubuntu.com/community/AutomaticSecurityUpdates) - `sudo apt-get install unattended-upgrades`

** Setting Up WSGI **

WSGI stands for web server gateway interface and what is does is stand as a specification for how the server should communicate with our python framework flask. We have already downloaded Flask and WSGI with the commands above. However, there are a few additional commands and files required to get the server and application communicating successfully.

Steps to Enabling WSGI

* You will need to enable WSGI using the command `sudo a2enmod wsgi`. 

* After you enable the enable the communication link you have to edit some apache2 config files. Maneuver yourself to the config file using `cd /etc/apache2/sites-available`.

* If you have not set up any config files within the sites-available page yet, you could start by copying the default config through the command: `sudo cp 000-default.conf bfm.conf`. 

* Now you need to write the line: `WSGIScriptAlias / /var/www/html/bfm/bfm.wsgi` into the bfm.conf. Your system admin should know how to handle this for you. 

* The last step that will be required to set up the communication link between the server and the application is to restart apache2. You can do this through the command: `sudo service apache2 restart`. 

> **Note:** Any conditional settings beyond setting up the WSGI communication link should be handled by your system administrator at this point. 

** Configuring Logrotate **

[Logrotate](http://www.linuxcommand.org/man_pages/logrotate8.html) is a built-in automatic log rotation tool that manages disk space regarding log files for Linux servers. If you wish to learn more regarding the utility of this tool, I suggest you read this [article](https://support.rackspace.com/how-to/understanding-logrotate-utility/).

We have to change the default permissions set by logrotate so that our system will always have access to read and write to the log files for apache2. The current default location for these log files is located in a file at `/etc/logrotate.d/apache2`. The default config will look like this:

![defaultLog.PNG](https://bitbucket.org/repo/bEXb4L/images/3036210369-defaultLog.PNG)

* We must change the line `create 640 root adm` to `create 660 root bfm`. 

>***Note:*** that bfm is an example of a group that www-data belongs to. Your system administrator should decide if a group is the best course of action for your server. However, it is important that www-data be granted access to these log files. 

** Installation of the Application **

After these tasks regarding setting up the server have been completed we can now shift our focus to installing the application onto the server. We need to [clone](https://confluence.atlassian.com/bitbucket/clone-a-repository-223217891.html) the application from bitbucket using the `git clone` command into the `html` directory.

>**Check Permissions:**
It's essential that `www-data` has the permission to read and write to all the files within the Berea Farmers Market directory. 

Just as we set up the virtual environment and database in the development stage we need to do the same within the production process. If you need more detail about the process please refer to the same steps taken in the development stage. 

*Set up Virtual Environment*

* `source setup.sh`
* `deactivate` 
* We don't need to keep the virtual environment activated because of the link of communication we created with the WSGI. 

*Set up database*

* `python reset-db.py`

After all of these steps have been completed the system should be operational. If any problems consist please notify us that we can help with them.  

## Authors

* **Cody Myers** - *Initial work* - [Repo](https://bitbucket.org/cody_myers/)

* **Aleksandra Cvetanovska** - *Initial work* - [Repo](https://bitbucket.org/cvetanovskaalex/)

* **Shadia Prater** - *Initial work* - [Repo](https://bitbucket.org/praters/)

* **Daryl Sullivan** - *Initial work* - [Repo](https://bitbucket.org/Sullivand/)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.


## Contributing

Please read [CONTRIBUTING.md](https://bitbucket.org/cody_myers/bereafarmersmarket/src/9bee6dec7817028d7704231b867323da92f415d7/CONTRIBUTING.md?at=master&fileviewer=file-view-default) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

** List of Developers: **

*Everyone whose code has been used in the development of his application.*

* [Cody Myers](https://bitbucket.org/cody_myers/)
* [Aleksandra Cvetanovska](https://bitbucket.org/cvetanovskaalex/)
* [Shadia Prater](https://bitbucket.org/praters/)
* [Darl Sullivan](https://bitbucket.org/Sullivand/)

** Special Thanks **

* The development of this READ.md was based on this [template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) created by [Billie Thompson](Billie Thompson)
* Drew Elliot has been our community partner and has worked closely with us during the development of this system.