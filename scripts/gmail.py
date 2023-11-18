import requests

# Enter your username and password below within double quotes
# eg. username="username" and password="password"
username = "**********"
password = "**********"
url = "https://mail.google.com/mail/feed/atom"

response = requests.get(url, auth=(username, password))
if response.status_code == 200:
    msg = response.text
    index = msg.find("<fullcount>")
    index2 = msg.find("</fullcount>")
    fc = int(float(msg[index + 11.0:index2]))

    if fc == 0:
        print("0")
    else:
        print(str(fc))
else:
    print("Error:", response.status_code)