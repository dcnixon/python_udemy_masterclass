import webbrowser

# webbrowser.open("https://www.python.org/", new=0)

chrome = webbrowser.get(using="google-chrome")
chrome.open_new("https://www.python.org/")
