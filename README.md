<h1>WebServerWithAutomatedTesting</h1>
<h2>Introduction</h2>
This solution uses Flask to accomplish a simple web server that takes a user's name/input in a form, and diplays the user's input as in the format "Hello [user's input]"
The automated testing is written in python  and is accomplished by using the Selenium library for automated testing. The test itself simulates a full journey from the user's input to the display at the endpoint. 
<br>
<h2>Instructions</h2>
<h3>Setting Up</h3>
Before running the solution, Flask, Selenium and a chromedriver is required to be installed on the system. 
<h4>Flask</h4>
- To install Flask run <b>pip install flask</b>
<h4>Selenium</h4>
- To install Selenium run <b>pip install selenium</b>
<h4>ChromeDriver</h4>
- Go to https://sites.google.com/chromium.org/driver/
- Download the correct version of the chromediver. (This would be the version of your chrome installed on your system.)
- Extract the .exe into C:\Program Files (x86)

<h3>Running the Web Server</h3>
To run the web server, type:<br>
1. <b>cd \WebServerWithAutomatedTesting-main\venv</b><br>
2. <b>Scripts\activate</b><br>
3. <b>cd webserver</b><br>
4. <b>set FLASK_APP=server</b><br>
5. <b>flask run</b><br>

<h3>Running the Automated Test</h3>
To run the automated test the webserver must been running first, therefore, open a new terminal and type:<br>
1. <b>cd \WebServerWithAutomatedTesting-main\venv\Test<b><br>
2. <b>main</b><br>
(Note: Step 2 can also work with <b>main.py</b>)
