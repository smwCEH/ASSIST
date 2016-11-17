#!/usr/bin/env python3
__author__ = "smw"
__email__ = "smw@ceh.ac.uk"


import os
import sys
from PIL import Image
import numpy as np


def report_array(tif):
    im = Image.open(tif_path)
    imarray = np.array(im)
    print('\timarray.shape:\t\t{0}'.format(imarray.shape))
    print('\timarray.size:\t\t{0}'.format(imarray.size))
    unique = np.unique(imarray, return_counts=True)
    print('\tnp.unique[0]:\t\t{0}'.format(unique[0]))
    print('\tnp.unique[1]:\t\t{0}'.format(unique[1]))
    print('\tnp.unique[1].sum:\t\t{0}'.format(np.sum(unique[1])))
    del im, imarray


print('\n\nCroping Scenarios')
tif_folder = r'E:\assist\demo-data\Demo Data for Tool\CroppingScenarios'
tif_list = ['cropclass_Baseline.tif',
            'cropclass_scenario_O.tif', 'cropclass_scenario_H.tif', 'cropclass_scenario_E.tif']
for tif in tif_list:
    tif_path = os.path.join(tif_folder, tif)
    print('TIF:\t\t{0}'.format(tif_path))
    report_array(tif)


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
