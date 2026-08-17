import re, os

getUserProfileImageUrlPath = lambda username: f'/user_avatar/discourse.aosus.org/{username}/48/9345_2.png'
extractUsername = lambda userUrl: re.search(r'/u/([^/?#]+)', userUrl).group(1)
extractArticleID = lambda aosusUrl : re.search(f'https://discourse.aosus.org/t/topic/([^/?#]+)', aosusUrl).group(1)

def _removeFile( filepath:str):
    try:
        os.remove(path=filepath)
    except FileNotFoundError:
        print(f'[utils._removeFile]: `{filepath}` not exsits')
