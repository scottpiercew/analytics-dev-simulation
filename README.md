# Analytics project developer simulation

Experience the end-to-end collaborative process of developing code that’s production-ready

##Tools to install / setup
Follow these steps in order.

####GitHub
Create a GitHub account: https://github.com \
Once you have created a GitHub account navigate to the following repository: https://github.com/npratt3284/analytics-dev-simulation \
Click the "Fork" button in the middle top right of the page. \
This will now be available as a repository to you and can be viewed by navigating to your repositories. \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Click your account logo in the top right of the page \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Select "Your Repositories" to view this

####GitKraken
Install GitKraken: https://www.gitkraken.com \
Once GitKraken has been installed we need to clone the repository that was forked above. \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Click on the folder icon in the top left of the screen \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Select the Clone option \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Select the GitHub.com option and click Connect GitHub and Continue Authorization\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Exit preferences once connected and navigate back to the GitHub.com option in the previous steps \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; You will now see the analytics-dev-simulation as an option, select this branch \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; You have now cloned the repo ! \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Double click the WebScraperSim branch under the Remote section


####Python
Install Python 2.7: https://www.python.org/downloads/release/python-2715/ \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Windows: Windows x86-64 MSI installer \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Mac:     macOS 64-bit installer

####PyCharm IDE
Install the latest version of PyCharm Community Edition: www.jetbrains.com/pycharm/download/ \
Steps during installation: \
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Select "Do not use a previous configuration" \
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Select "I've never used PyCharm" \
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Click Next:UI Themes \
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Select Darcula \
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Click Next:Launcher Script \
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Do not select anything and click Next:Featured plugins \
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Click Start using PyCharm \
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Open a project and select the directory on your local machine where you cloned the repository

Once PyCharm has been installed and your project is opened there are a few configurations that need to be made: \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Click on PyCharm and navigate to Preferences -> Project:analytics-dev-simulation -> Project Interpreter \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Click the gear icon in the top right and select Add \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Select System Interpreter and the directory should point to the location where Python was installed \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; This should appear as the "Project Interpreter" now after you click OK 

We now need to add additional packages: \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Click the "+" button on the bottom right \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Search for "beautifulsoup4" and install package \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Repeat this step for the "requests" package as well

You should now be able to run the project. Right click on NFLWebScraper.py in the project navigation window and select Run 'NFLWebScraper.py'