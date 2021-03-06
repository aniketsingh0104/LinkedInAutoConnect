<h2 align="center">What's this?</h2>
<h4>This project helps in automatically accepting the LinkedIn connections requests. It has two versions: </h4>
<li>Javascript based version</li>
<li>Selenium based version</li>

<h2 align="center">Javascript based version doc</h2>
<h3 align="center">Prerequisites</h3>
<li>User should be signedIn on LinkedIn</li>

<h3 align="center">Run</h3>
<li>Open your LinkedIn account and go to this url <a href="https://www.linkedin.com/mynetwork/invitation-manager/" target="_blank">manage connections</a></li>
<li>Open the console and run the script given in <code>autoConnectJavaScript.js</code></li>


<h2 align="center">Selenium based version doc</h2>
<h3 align="center">Prerequisites</h3>
<li>Clone the repo in your local machine: <code>git clone git@github.com:aniketsingh0104/LinkedInAutoConnect.git</code></li>
<li>Go to the directory: <code>cd LinkedInAutoConnect</code>. Setup virtual environment: <code>python3 -m venv ./venv</code></li>
<li>Activate virtual environment: <code>source venv/bin/activate</code></li>
<li>Run this command inside the project directory to install dependencies: <code>pip install -r requirements.txt</code></li>
<li>For chrome driver see section : <b>Setting up the Selenium Driver</b></li>
<li>Inside <code>main.py</code> enter your chromium driver path in this variable <code>driver_path</code></li>
<li>Make sure that your computer's doesn't sleep while you are running this script.</li>

<h3 align="center">Setting up the Selenium Driver</h3>
<p>The application uses Chrome as the web driver. If you want to use any other browser, make sure you modify the scrip and download appropriate drivers. Below instructions are for chrome although a lot of them would be transferable:</p>
<li>Download the chrome driver for your Google Chrome Version from chromium drivers: <a href="https://chromedriver.chromium.org/downloads" target="_blank">link</a></li>
<li>Store it in a location and copy the path.</li>
<li>On a Mac, for your chrome driver to be allow-listed, fire up the below command on your terminal along with the path to your chrome driver. This is needed to allow the macOS to allow-list the driver and not check for a verified publisher. (<a href="https://stackoverflow.com/a/60374958/3766231">source</a>):</li>

```
xattr -d com.apple.quarantine <PATH_OF_DRIVER>
```

<h3 align="center">Run</h3>
<li>Go inside the project directory and run: <code>python main.py</code></li>
<li>It would open up LinkedIn page, <b>perform the signIn manually</b> and then leave the script, it would start accepting your requests.</li>

<h3 align="center">Troubleshooting</h3>
<li>As this script targets the accept button by its class, there might be cases in which class of the linkedin accept button is changed, in that case go to <i>contants.py</i> file and change the second parameter (after @class) of <i>XPATH_PATTERN_OF_LINKEDIN_CONNECTION_ACCEPT_BUTTON</i> with correct class pattern</li>
