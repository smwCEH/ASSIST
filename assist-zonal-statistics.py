#!/usr/bin/env python3
__author__ = "smw"
__email__ = "smw@ceh.ac.uk"


import os
import sys


import arcpy


def main():
    print('\n\nrunning main()...')
    #
    # Define and create file geodatabase if it doesn't exist
    fgdb = r'E:\assist\demo-data\arcgis\assist.gdb'
    if not arcpy.Exists(fgdb):
        arcpy.CreateFileGDB_management(out_folder_path=os.path.dirname(fgdb),
                                       out_name=os.path.basename(fgdb),
                                       out_version='CURRENT')
    # Define crop scenario image
    crop_scenario = r'E:\assist\demo-data\Demo Data for Tool\CroppingScenarios\cropclass_Baseline99.tif'
    if not arcpy.Exists(crop_scenario):
        sys.exit('crop_scenario {0} does not exist!'.format(crop_scenario))
    #
    # Define region image
    region = r'E:\assist\demo-data\Demo Data for Tool\Regions\country99.tif'
    if not arcpy.Exists(region):
        sys.exit('region {0} does not exist!'.format(region))
    #
    # Define arcpy environment settings
    arcpy.env.workspace = fgdb





    #
    print('\n\ndone main().')



if __name__ == '__main__':
    main()
