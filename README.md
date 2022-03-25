<h3 align="center">What's this?</h3>
<h4>This project helps in automatically accepting the LinkedIn connections requests. It uses a selenium to automate the manual behaviour.</h4>

<h3 align="center">Prerequisites</h3>
<li>Clone the repo in your local machine</li>
<li>Run this command inside the project directory: <code>pip install -r requirements.txt</code></li>
<li>Download chrome driver from here: <a href="https://chromedriver.chromium.org/downloads" target="_blank">link</a></li>
<li>Inside <code>main.py</code> enter your chromium driver path in this variable <code>driver_path</code></li>
<li>Make sure that your computer's doesn't sleep while you are running this script.</li>

<h3 align="center">Run</h3>
<li>Go inside the project directory and run: <code>python main.py</code></li>
<li>It would open up LinkedIn page, <b>perform the signIn manually</b> and then leave the script, it would start accepting your requests.</li>

<h3 align="center">Troubleshooting</h3>
<li>As this script targets the accept button by its class, there might be cases in which class of the linkedin accept button is changed, in that case go to <i>contants.py</i> file and change the second parameter (after @class) of <i>XPATH_PATTERN_OF_LINKEDIN_CONNECTION_ACCEPT_BUTTON</i> with correct class pattern</li>