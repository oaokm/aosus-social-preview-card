from requests_html import HTMLSession
from utils import (
    getUserProfileImageUrlPath,
    extractUsername
)

class aosusExtracter:
    """
    aosusExtracter: the object that responsible to deal with aosus discourse website to extract basic info about articles

    args:
        - url(str): aosus article's link

    variables:
        - ok(bool): if it is "True", this means that nothing is hindering the object's operation.
        - session(HTMLSession): reqeusts session
        - webpage(HTMLSession): establishing a connection via `session` with method `GET` to aosus discourse website
    """

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
        """
        _extractArtcleData: the object that responsible to deal with aosus discourse website to extract basic info about articles

        args:
            - contentLenght(int): an integer value represents the length of the content displayed in the generated card. default is 400 characters 
            - tagsLimit(int): the number of tags displayed on the generated card is determined so that it does not exceed the specified dimensions. default is 3 tags
            - titleLimit(int): an integer value represents the length of the title displayed in the generated card. default is 115 characters
            - paragraphsLimit(int): represents only the number of text paragraphs that will be displayed. default is 3 paragraphs

        """
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
