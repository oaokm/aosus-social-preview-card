import re

getUserProfileImageUrlPath = lambda username: f'/user_avatar/discourse.aosus.org/{username}/48/9345_2.png'
extractUsername = lambda userUrl: re.search(r'/u/([^/?#]+)', userUrl).group(1)
