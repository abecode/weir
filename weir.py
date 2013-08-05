#!/usr/bin/python

from searchpattern import SearchPattern, SearchPatternList
from objecttracker import TwitterStreamTracker

import argparse
import warnings
# usage: 

parser = argparse.ArgumentParser(description='Read from twitter streaming api and write to stdout or mongodb.')
parser.add_argument('--twaccess', type=str, nargs='+',
                    help='twitter user info',
                    default=['4h93sJt9gGVbwzQVLUtxYw', 'tKlKRm0zhBH2mTOi7UZdfaBxpvE2GL7N40tvZbstOk', '365601032-VzaZ7j5w8bI6e4wFbnbirSAq0kQa5ioYPQCyOVls', 'o91sNy1IJXLsSCyBS9gJqldoefuo1xilwXp5uYOQ']
                    )
parser.add_argument('--search', type=str, nargs='+',
                    #required=True,
                    help='search keywords')
parser.add_argument('--dbinfo', type=str, nargs='+',
                   help='database info')

args = parser.parse_args()
# canned versions
# american idol:
#args = parser.parse_args(['--twaccess', '4h93sJt9gGVbwzQVLUtxYw', 'tKlKRm0zhBH2mTOi7UZdfaBxpvE2GL7N40tvZbstOk', '365601032-VzaZ7j5w8bI6e4wFbnbirSAq0kQa5ioYPQCyOVls', 'o91sNy1IJXLsSCyBS9gJqldoefuo1xilwXp5uYOQ', '--search', 'americanidol', '"american idol"', '#idol'])
# iron man
args = parser.parse_args(['--twaccess', '4h93sJt9gGVbwzQVLUtxYw', 'tKlKRm0zhBH2mTOi7UZdfaBxpvE2GL7N40tvZbstOk', '365601032-VzaZ7j5w8bI6e4wFbnbirSAq0kQa5ioYPQCyOVls', 'o91sNy1IJXLsSCyBS9gJqldoefuo1xilwXp5uYOQ', '--search', 'iron man', 'iron_man'])
warnings.warn(str(args))

twitterParams = args.twaccess
searchParams = SearchPatternList(args.search)

tst = TwitterStreamTracker(twitterParams,searchParams)

for x in tst:
    print x['text']

