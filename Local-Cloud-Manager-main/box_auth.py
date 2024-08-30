from boxsdk import OAuth2

""" Replace with your Box API credentials """

client_id = 'ws64vbjjvnkw76roo45133nsvcizkxx0'
client_secret = 'mk2JjlWHVHB634nrIq4jBH2x15zLL0dk'

auth = OAuth2(client_id, client_secret)
auth_url, csrf_token = auth.get_authorization_url('http://localhost:5000/callback')
print("Visit this URL to authorize your app:", auth_url)
