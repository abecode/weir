#!/usr/bin/python

import re     
import urllib

class SearchPattern(object):
    """A search pattern for matching textual social media content
    
    Basically holds the search pattern and provides ways to convert to other
    formats, e.g. twitter streaming api vs gnip
    
    >>> sp = SearchPattern("iron man")
    >>> sp("iron man 3 is a great romantic comedy for the whole family")
    True
    
    It is case insensitive

    >>> sp("Iron man 3 is a great romantic comedy for the whole family")
    True
    
    order is important
    
    >>> sp = SearchPattern("man iron")
    >>> sp("Iron man 3 is a great romantic comedy for the whole family")
    False

    convert to twitter streaming track api
    >>> sp = SearchPattern('"iron man"')
    >>> sp("Iron man 3 is a great romantic comedy for the whole family")
    False
    >>> sp('"Iron man" 3 is a great romantic comedy for the whole family')
    True
    >>> sp.toTwitterTrackPattern()
    '%22iron%20man%22'
    >>> sp.toGnipPattern()
    Traceback (most recent call last):
      ...
    NotImplementedError: toGnipPattern is not implemented yet.
    

    
    """ 
    
    def __init__(self,pattern):
        self.regex = re.compile(pattern, re.I)
    
    def __call__(self,s):
        if self.regex.search(s):
            return True
        else:
            return False
    def toTwitterTrackPattern(self):
        return urllib.quote(self.regex.pattern)
        return self.regex.pattern
    def toGnipPattern(self):
        raise NotImplementedError("toGnipPattern is not implemented yet.")


class SearchPatternList(list):
    """A list of search patterns

    >>> spl = SearchPatternList(["iron man", "iron_man"])
    >>> spl("Iron man 3 is a great romantic comedy for the whole family")
    True
    >>> spl("@iron_man you provided me with a deeply touching moviegoing experience")
    True
    >>> spl.toTwitterTrackPattern()
    'iron%20man%2Ciron_man'

    """
    def __init__(self,l):
        for x in l:
            self.append(SearchPattern(x))
    def __call__(self,s):
        for x in self:
            if x.regex.search(s):
                return True
        return False
    def toTwitterTrackPattern(self):
        patterns = map(SearchPattern.toTwitterTrackPattern, self)
        return '%2C'.join(patterns)
    def toGnipPattern(self):
        raise NotImplementedError("toGnipPattern is not implemented yet.")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
