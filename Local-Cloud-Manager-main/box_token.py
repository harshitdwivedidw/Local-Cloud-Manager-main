from boxsdk import OAuth2

""" Replace with your Box API credentials """
client_id = 'ws64vbjjvnkw76roo45133nsvcizkxx0'
client_secret = 'mk2JjlWHVHB634nrIq4jBH2x15zLL0dk'

"""Extracted from the redirect URI """

auth_code = 'BJCH8p6WS01jNff5IskMRwsP7f1z9vdw'  
auth = OAuth2(client_id, client_secret)
access_token, refresh_token = auth.authenticate(auth_code)

print("Access Token:", access_token)
print("Refresh Token:", refresh_token)