# Take-home-assignment 
A simple Flask-Kubernetes-Docker web application that allows the user to upload a .CSV file. On successful file upload, the application should perform the following validations:
Checks whether the uploaded is a .CSV and not any other format.
Check whether the .CSV file has exactly 10 rows and 3 columns.
Checks whether the data is present in each cell (.CSV file is "complete"). A "complete" sample test.csv is available in this repository for testing purposes.
<br>

# Contents
* [Features](#features)
* [Technologies & Stack](#techstack)
* [Set-up & Installation](#installation)


## <a name="features"></a> Features

Homepage - page where you can upload file
<br>


Validate_file - throws response message after validating the file
<br>


## <a name="techstack"></a> Technologies and Stack
**Backend:**
Python, Flask <br>
**Frontend:**
HTML, Jinja <br>

## <a name="installation"></a> Set-up & Installation
Install a code editor such as [VS code](https://code.visualstudio.com/download) or [Sublime Text](https://www.sublimetext.com/).<br>
Install [Python3](https://www.python.org/downloads/mac-osx/)<br>
Install [pip](https://pip.pypa.io/en/stable/installing/), the package installer for Python <br>

Clone or fork repository:
```
$ git clone https://github.com/rlavanya9/take-home-assign.git
```
Create and activate a virtual environment inside the directory:
```
$ virtualenv myproject
$ source env/bin/activate
```
Install dependencies:
```
$ pip3 install -r requirements.txt
```
in server.py, get the file uploaded and do all the file validations
```
Run the app from the command line:
```
$ python3 server.py
```

