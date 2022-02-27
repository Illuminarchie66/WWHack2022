@ECHO OFF
Echo Installing dependencies
Echo Installing beautifulSoup
py -m pip install beautifulsoup4
Echo Installing Flask
py -m pip install Flask
Echo Installing requests
py -m pip install requests
Echo Installing Selenium
py -m pip install -U selenium
Echo Installing Chrome drivers
powershell -Command "Invoke-WebRequest https://chromedriver.storage.googleapis.com/98.0.4758.102/chromedriver_win32.zip -OutFile chromedriver.zip"
powershell -Command "Expand-Archive -Path chromedriver.zip -DestinationPath C:\Windows -Force -Verbose"
move chromedriver.exe c:\Windows