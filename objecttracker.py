#!/usr/bin/python 

from collections import Iterator,Iterable

import json
import requests
#import webbrowser
from urlparse import parse_qs
from requests_oauthlib import OAuth1


class ObjectTracker(Iterable):
    """This class is a virtual class to wrap a connection to a streaming data
    source that can be filtered with patterns, ie matching rules"""
    pass

class TwitterStreamTracker(ObjectTracker):
    """Uses twitter streaming api to track a set of rules

    >>> from searchpattern import *
    >>> twitterParams = ['xxx4h93sJt9gGVbwzQVLUtxYw', 'tKlKRm0zhBH2mTOi7UZdfaBxpvE2GL7N40tvZbstOk', '365601032-VzaZ7j5w8bI6e4wFbnbirSAq0kQa5ioYPQCyOVls', 'o91sNy1IJXLsSCyBS9gJqldoefuo1xilwXp5uYOQ']
    >>> searchPatterns = SearchPatternList(["iron man", "iron_man"])
    >>> tst = TwitterStreamTracker(twitterParams,searchPatterns)
    >>> for line in tst.r.iter_lines(): print line
    """
    
    def __init__(self,twitterParams,searchPatterns):
        self.search = searchPatterns
        search_string = searchPatterns.toTwitterTrackPattern()
        self.url = u"https://stream.twitter.com/1.1/statuses/filter.json?track=%s"%search_string
        print self.url
        
        consumer_key = unicode(twitterParams[0])
        consumer_secret = unicode(twitterParams[1])
        access_token = unicode(twitterParams[2])
        access_secret = unicode(twitterParams[3])
        print consumer_key, consumer_secret, access_token, access_secret
        self.oauth = OAuth1(consumer_key, client_secret=consumer_secret, resource_owner_key=access_token, resource_owner_secret=access_secret)
        self.r = requests.get(url=self.url, auth=self.oauth, stream=True)
        #for line in self.r.iter_lines(): 
        #    print line

    def __iter__(self):
        r = requests.get(url=self.url, auth=self.oauth, stream=True)
        # note, the if self.search(l) below is b/c the twitter stream api doesn't do exactly a
        # regex.  The stream api params result in a promiscuous search that needs to be filtered
        #return iter((json.loads(l) if self.search(l) for l in r.iter_lines()) )
        #return iter( (json.loads(l)  for l in r.iter_lines() if self.search(l)) )
        return (json.loads(l)  for l in r.iter_lines() if self.search(l)) 
    
    
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # from searchpattern import *
    # twitterParams = ['4h93sJt9gGVbwzQVLUtxYw', 'tKlKRm0zhBH2mTOi7UZdfaBxpvE2GL7N40tvZbstOk', '365601032-VzaZ7j5w8bI6e4wFbnbirSAq0kQa5ioYPQCyOVls', 'o91sNy1IJXLsSCyBS9gJqldoefuo1xilwXp5uYOQ']
    # searchPatterns = SearchPatternList(["iron man", "iron_man"])
    # tst = TwitterStreamTracker(twitterParams,searchPatterns)
    # for line in tst: print line    
    
