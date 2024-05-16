# Prerequistes

You must have Node installed on your computer, in order to run script, 
Please follow instructions in the provided URL, 

`https://nodejs.org/en/download`

Please make sure `node` is in your environment path before running, as it is required in the upload stage. 

Make sure you have the Python 3.9 and higher virsion from url:

`https://python.org`

Also you will need Google Chrome browser installed.

--------------------------------------
### Installation

Donwload repository as a .zip archive directly from this github repository page.

OR

Clone the repository from github.

For cloning this rep you must have Git installed and set up. 
If you are using Windows check https://git-scm.com/download/ and download latest virsion.

```bash
git clone https://github.com/makiisthenes/TiktokAutoUploader.git
```
------------

For Windows: find **Installation.bat** file in repository and launch it.

For Unix/Mac OS: find **Installation.sh** file in repository. Copy the filepath. In Terminal write commands below to execute script:
```bash
cd your_filepath
bash Installation.sh
```

OR use cli (Terminal) commands below.

Install requirements for package.

```bash
pip upgrade
pip install -r requirements.txt
```
Install node packages.
```bash
cd tiktok_uploader/tiktok-signature/
npm i
```
------------

### Adding new user

For Windows: find **user_login.bat** file in repository and start it manually. 

For Unix/Mac OS: find **user_login.sh** file in repository. Copy the filepath. In Terminal write commands below to execute script:
```bash
cd your_filepath
bash user_login.sh
```

You will be asked to enter username (recommended to use tik-tok username) and  the youtube link to connected channel with **.../videos** adding.

example: `https://www.youtube.com/@spud17soccer/videos`

If everything completes successfully, browser Google Chrome will be opened. Than you have to log in to your tik-tok account to create the cookies file, which can be found in **CookiesDir** in your project repository. Browser will be automatically closed after logging in.

------------

### Automation guide:

<details>
  <summary>Windows</summary>
  
  Before automation you need to manualy launch first video uploade to your tik-tok channel. This have to be done as a workaround to problem with downloading age-restricted videos from youtube. 
Find **...\TiktokAutoUploader\upload_start.bat** file in project repository and launch it. Next follow the messages in cli, log in your youtube account to create cookie cache, so you won't need to do this next time.

To access Windows Task Scheduler, use the Win+R key combination and enter taskschd.msc. Alternatively, search for it through the standard Windows search.

Then follow these steps:

1. Navigate to Task Scheduler Library: In the Task Scheduler window, on the left-hand side, navigate to "Task Scheduler Library". This is where you'll see existing tasks and where you'll create a new one.

2. Create a New Task: Right-click on "Task Scheduler Library" and select "Create Basic Task" or "Create Task" from the context menu. Both options will allow you to create a new task, but the latter offers more advanced options.

3. Name and Description: Give your task a name and an optional description to help you identify it later. You can use something like "TiktokScheduler".
In Security options section choose "Run whether user logged on or not", "Run with highest privileges", "Hidden", "Configure for: Windows *** (choose your win version)".

4. Choose Trigger: Select when you want the task to start. You can choose from options like "Daily", "Weekly", "Monthly", or "At log on". Follow the prompts to set the specific details for your chosen trigger.

5. Action: Select "Start a program".
Settings.
Find "upload_start.bat" file in your repository. Copy the path with the file name attached and insert into Program/Script section. Like this: **...\TiktokAutoUploader\upload_start.bat**
Copy the path without file name and insert into "Start in" section. This is a mandatory field for our settings. Like this: **...\TiktokAutoUploader**

6. Set Conditions: Unset all checkboxes.
   
7. Settings.
Set checkboxes:
Allow task to be run on demand;
Run task as soon as possible after a scheduled start is missed;
If task fails, fails every: 5 mins, 2 attempts;
Stop the task if it runs longer than: 4 hours;
If the task does not end when requested, force it to stop;

8. Finish: Review your settings and click "OK" to create the task. You may be asked to enter your user password for Windows.

</details>

<details>
  <summary>Unix / Mac OS</summary>
  Before automation you need to manualy launch first video uploade to your tik-tok channel. This have to be done as a workaround to problem with downloading age-restricted videos from youtube. 
  
Find **...\TiktokAutoUploader\upload_start.sh** file in your project repository and execute it. For executing write commands below in Termianl:
```bash
cd your_filepath
bash upload_start.sh
``` 
Next follow the messages in Terminal, log in your youtube account to create cookie cache, so you won't need to do this next time.


Crontab will be used for automation. 

1. To open crontab file use command in Terminal:

```bash
nano crontab -e
```

2. Find `upload_start.sh` in project repository and copy its path. In the crontab file enter the following command.

```bash
0 1 * * * .../TiktokAutoUploader/upload_start.sh
```
Paste the path to the upload_start.sh instead of ".../".

This will run the scrape at minute = 0 , hour = 1, day = * : every day, month=: * every month, weekday= * every weekday.
Using the website `https://crontab.guru/`, it’s easy to create any schedule you can wish for.

3. Save the crontab file.
Keyword combination CTRL+O will save the file and you can exit using CTRL+X.
Great work, now your script should be running on schedule.
  
</details>



------------

### Logs

Logs are being stocked in file **./Logging/app.log** inside the project repository. As for now it is being written into one file, which clears before script starts. 

### Using program in CLI:

Show Current Users and Videos ⚙️:

All local videos must be saved under folder `VideosDirPath` if this doesn't exist please create one.

```bash
# Show all current videos found on system.
python cli.py show -v 
```

All cookies must be saved under folder `CookiesDir`, if this doesn't exist please create one.

```bash
# Show all current cookies found on system.
python cli.py show -c 
```

-----
