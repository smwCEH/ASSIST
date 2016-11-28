#!/usr/bin/env python3
__author__ = "smw"
__email__ = "smw@ceh.ac.uk"


import os
import sys
from PIL import Image
import numpy as np
import gdal


def report_array(tif):
    im = Image.open(tif_path)

    print('\n')
    properties = ['format', 'mode', 'size', 'width', 'height', 'palette', 'info']
    for property in properties:
        if hasattr(im, property):
            print('\t{0:20}:\t\t{1}'.format('im.' + property, getattr(im, property)))
    tiles = im.tile
    print('\t{0:<20}:\t\t{1}'.format('im.tile', tiles))
    for tile in range(len(tiles)):
        print('\t\t{0:<20}:\t\t{1}'.format('im.tile[{0}]'.format(tile), im.tile[tile]))
    print('\n')

    imarray = np.array(im)
    print('\timarray.shape:\t\t{0}'.format(imarray.shape))
    print('\timarray.size:\t\t{0}'.format(imarray.size))
    print('\timarray.dtype:\t\t{0}'.format(imarray.dtype))
    unique, counts = np.unique(imarray, return_counts=True)
    print('\tunique[0]:\t\t\t{0}'.format(unique))
    print('\tcounts[1]:\t\t\t{0}'.format(counts))
    print('\tdict:\t\t\t\t{0}'.format(dict(zip(unique, counts))))
    print('\tcounts.sum:\t\t\t{0}'.format(np.sum(counts)))
    print imarray
    print imarray[999]

    # im.show()

    # print(imarray[999,])
    # unique, counts = np.unique(imarray[999,], return_counts=True)
    # print(dict(zip(unique, counts)))

    del im, imarray

    gtif = gdal.Open(tif_path)
    print('\tGetMetdata():\t\t{0}'.format(gtif.GetMetadata()))
    print('\tRasterCount:\t\t{0}'.format(gtif.RasterCount))
    imarray = np.array(gtif.GetRasterBand(1).ReadAsArray())
    print('\timarray.shape:\t\t{0}'.format(imarray.shape))
    print('\timarray.size:\t\t{0}'.format(imarray.size))
    print('\timarray.dtype:\t\t{0}'.format(imarray.dtype))
    unique, counts = np.unique(imarray, return_counts=True)
    print('\tunique[0]:\t\t\t{0}'.format(unique))
    print('\tcounts[1]:\t\t\t{0}'.format(counts))
    print('\tdict:\t\t\t\t{0}'.format(dict(zip(unique, counts))))
    print('\tcounts.sum:\t\t\t{0}'.format(np.sum(counts)))
    print imarray
    print imarray[999]

    # gtif.show()

    # print(imarray[999,])
    # unique, counts = np.unique(imarray[999,], return_counts=True)
    # print(dict(zip(unique, counts)))

    gtif = None

print('\n\nCroping Scenarios')
tif_folder = r'E:\assist\demo-data\Demo Data for Tool\CroppingScenarios'
# tif_list = ['cropclass_Baseline.tif',
#             'cropclass_scenario_O.tif', 'cropclass_scenario_H.tif', 'cropclass_scenario_E.tif']
tif_list = ['cropclass_Baseline.tif']
# tif_list = ['cropclass_scenario_E.tif']
for tif in tif_list:
    tif_path = os.path.join(tif_folder, tif)
    print('TIF:\t\t{0}'.format(tif_path))
    report_array(tif)



sys.exit()


print('\n\nLand Cover Scenarios')
tif_folder = r'E:\assist\demo-data\Demo Data for Tool\LandCoverScenarios'
tif_list = ['LC_Baseline.tif',
            'LC_scenario_GSN_5.tif', 'LC_scenario_GSN_10.tif', 'LC_scenario_GSN_15.tif', 'LC_scenario_GSN_20.tif', 'LC_scenario_GSN_25.tif', 'LC_scenario_GSN_30.tif',
            'LC_scenario_A_P_5.tif', 'LC_scenario_A_P_10.tif', 'LC_scenario_A_P_15.tif', 'LC_scenario_A_P_20.tif', 'LC_scenario_A_P_25.tif', 'LC_scenario_A_P_30.tif',
            'LC_scenario_A_NP_5.tif', 'LC_scenario_A_NP_10.tif', 'LC_scenario_A_NP_15.tif', 'LC_scenario_A_NP_20.tif', 'LC_scenario_A_NP_25.tif', 'LC_scenario_A_NP_30.tif']
for tif in tif_list:
    tif_path = os.path.join(tif_folder, tif)
    print('TIF:\t\t{0}'.format(tif_path))
    report_array(tif)


print('\n\nMasks')
tif_folder = r'E:\assist\demo-data\Demo Data for Tool\Regions'
tif_list = ['country.tif', 'euroregion.tif']
for tif in tif_list:
    tif_path = os.path.join(tif_folder, tif)
    print('TIF:\t\t{0}'.format(tif_path))
    report_array(tif)
