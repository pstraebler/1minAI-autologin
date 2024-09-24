# 1minAI - Auto Login

Automatically connect to app.1min.ai using Python, Selenium and a Web Driver to get free credits every day :)

By default, it uses the Chrome Webriver

```
python autologin.py [--firefox|--chrome] [--headless] [--debug]
```

*Should works with Python >= 3.10*

## Installation

### Pip dependencies

You *should* create a virtual environment

```
$ python3 -m venv 1minai
$ source 1minai/bin/activate
$ pip install -r requirements.txt
```

### Chrome webdriver

This script uses the Chrome Webdriver (and therefore, Google Chrome). 

You can download it from [Chrome for Testing availability](https://googlechromelabs.github.io/chrome-for-testing/) and put the binary *chromedriver* in your `$PATH`

The Chromedrive must match the version of Google Chrome installed on your computer.  

### Env file

Put your 1minAI credentials in the .env file
