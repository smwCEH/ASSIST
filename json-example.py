#!/usr/bin/env python3
__author__ = 'smw'
__email__ = 'smw@ceh.ac.uk'
__status__ = 'Development'

import os
import sys


import json
import pandas as pd


pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 120)


def main():
    #
    data_folder = r'E:\assist\demo-data\json\pydata-book-master\ch07'
    json_file = r'foods-2011-10-03.json'
    json_filepath = os.path.join(data_folder, json_file)
    print('\n\n{0:<20}:\t{1}'.format('json_filepath', json_filepath))
    #
    db = json.load(open(json_filepath))
    print('\n\n{0:<20}:\t{1}'.format('len(db)', len(db)))
    #
    nutrients = pd.DataFrame(db[0]['nutrients'])
    print('\n\n{0:<20}'.format('nutrients'))
    print(nutrients[:7])
    #
    info_keys = ['description', 'group', 'id', 'manufacturer']
    info = pd.DataFrame(db, columns=info_keys)
    print('\n\n{0:<20}'.format('info'))
    print(info[:5])
    print(info.info())
    print(pd.value_counts(info.group)[:10])
    #
    nutrients = []
    for rec in db:
        fnuts = pd.DataFrame(rec['nutrients'])
        fnuts['id'] = rec['id']
        nutrients.append(fnuts)
    nutrients = pd.concat(nutrients, ignore_index=True)
    print(nutrients)



if __name__ == '__main__':
    main()
