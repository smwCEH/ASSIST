#!/usr/bin/env python3
__author__ = 'smw'
__email__ = 'smw@ceh.ac.uk'
__status__ = 'Development'


# Example JSON file mangling from Python for Data Analysis book
# See: http://shop.oreilly.com/product/0636920023784.do
# Code scrapped from Chapter 7 pages 212-217 using example USDA Food Database (downloaded from book web site)
#

import os
import sys


import json
import pandas as pd
import matplotlib.pyplot as plt


pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 120)


plt.interactive(False)


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
    print(nutrients.info())
    print(nutrients.duplicated().sum())
    nutrients = nutrients.drop_duplicates()
    #
    col_mapping = {'description' : 'food',
                   'group'       : 'fgroup'}
    info=info.rename(columns=col_mapping, copy=False)
    print(info.info())
    col_mapping = {'description' : 'nutrient',
                   'group'       : 'nutgroup'}
    nutrients = nutrients.rename(columns=col_mapping, copy=False)
    print(nutrients.info())
    ndata = pd.merge(nutrients, info, on='id', how='outer')
    print(ndata.info())
    print(ndata.ix[30000])
    #
    result = ndata.groupby(['nutrient', 'fgroup'])['value'].quantile(0.5)
    # print(result['Zinc, Zn'])
    # print(result['Zinc, Zn']).order() # order() method deprecated, replaced with sort_values()
    print(result['Zinc, Zn']).sort_values()
    # result['Zinc, Zn'].order().plot(kind='barh')
    result['Zinc, Zn'].sort_values().plot(kind='barh')
    plt.subplots_adjust(left=0.45, bottom=0.10, right=0.95, top=0.95)
    plt.show()



if __name__ == '__main__':
    main()
