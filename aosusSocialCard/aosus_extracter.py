from requests_html import HTMLSession
from utils import (
    getUserProfileImageUrlPath,
    extractUsername
)

class aosusExtracter:
    def __init__(self, url):
        self.ok  = True
        self.url = url
        
        self.session = HTMLSession()

        self.webpage = self.session.get(self.url)

        if self.webpage.ok:
            pass

        
        else:
            self.ok = False


    def _extractArtcleData(
            self, 
            contentLenght=400, 
            tagsLimit=3,
            titleLimit=115,
            paragraphsLimit=3
            ):
        if self.ok:
            _title    = self.webpage.html.find('h1', first=True).text
            if len(_title) > titleLimit:
                _title = ' '.join([_title[:titleLimit], '...'])
            _username = extractUsername([ i.attrs.get('href') for i in self.webpage.html.find('a') if not i.attrs.get('href', '').find('https://discourse.aosus.org/u/')][0])
            _content  = ' '.join([ p.text for p in self.webpage.html.find('p') if not p.find('div.lightbox-wrapper') ][:paragraphsLimit])[:contentLenght]
            
            tags = [ tag.text  for tags in self.webpage.html.find('div.topic-category') for tag in tags.find('a')]

            return {
                    'username': _username, 
                    'profileImageUrlPath': getUserProfileImageUrlPath(_username),
                    'title': _title,
                    'text': _content,
                    'tag': " | ".join(tags[:tagsLimit])
        }

if __name__ == '__main__':
    url = 'https://discourse.aosus.org/t/topic/5415'
    print(aosusExtracter(url)._extractArtcleData())
