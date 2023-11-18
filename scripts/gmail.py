import requests

# Define mail feed URL
mail_feed_url = "https://username:password@mail.google.com/mail/feed/atom"

# Create session object to send HTTP requests
session = requests.Session()

# Set Connection header to "keep-alive" (maintain connection)
session.headers["Connection"] = "keep-alive"

# Send GET request to mail feed URL using the session
response = session.get(mail_feed_url)

# Raise an exception if the response has an error status code
response.raise_for_status()