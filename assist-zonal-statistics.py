#!/usr/bin/env python3
__author__ = "smw"
__email__ = "smw@ceh.ac.uk"


import os
import sys


import arcpy
from arcpy.sa import *
from PIL import Image
import numpy as np


def describe_raster(raster):
    desc = arcpy.Describe(raster)
    properties = ['name', 'extent', 'height', 'width', 'meanCellHeight', 'meanCellWidth', 'isInteger', 'pixelType', 'noDataValue']
    for property in properties:
        if hasattr(desc, property):
            print('\t\t{0:<20}:\t{1}'.format('desc.' + property, getattr(desc, property)))
    # statistics = ['MINIMUM', 'MAXIMUM', 'MEAN', 'STD']
    statistics = ['MINIMUM', 'MAXIMUM']
    for statistic in statistics:
        stat = arcpy.GetRasterProperties_management(in_raster=raster,
                                                    property_type=statistic)
        print('\t\t{0:<20}:\t{1}'.format(statistic, stat.getOutput(0)))


def image_to_raster(image, fgdb):
    print('\n\nConverting image to fgdb raster...')
    print('\t{0:<20}:\t{1}'.format('image', image))
    im = Image.open(image)
    imarray = np.array(im)
    print('\t{0:<20}:\t{1}'.format('imarray.size', imarray.size))
    print('\t{0:<20}:\t{1}'.format('imarray.shape', imarray.shape))
    unique = np.unique(imarray, return_counts=True)
    print('\t{0:<20}:\t{1}'.format('np.unique[0]', unique[0]))
    print('\t{0:<20}:\t{1}'.format('np.unique[1]', unique[1]))
    print('\t{0:<20}:\t{1}'.format('np.sum(np.unique[1])', np.sum(unique[1])))

    raster = os.path.basename(image)
    raster = os.path.splitext(raster)[0]
    raster = os.path.join(fgdb, raster)
    print('\t{0:<20}:\t{1}'.format('raster', raster))
    if arcpy.Exists(raster):
        arcpy.Delete_management(raster)
    # arcpy.CopyRaster_management(in_raster=image,
    #                             out_rasterdataset=raster,
    #                             pixel_type='8_BIT_UNSIGNED')
    sa_raster = arcpy.NumPyArrayToRaster(in_array=imarray,
                                  lower_left_corner=arcpy.Point(0.0, 0.0),
                                  x_cell_size=1000.0,
                                  y_cell_size=1000.0,
                                  value_to_nodata=None)
    sa_raster.save(raster)
    arcpy.CalculateStatistics_management(in_raster_dataset=raster)
    arcpy.BuildRasterAttributeTable_management(in_raster=raster,
                                               overwrite=True)
    describe_raster(raster)
    print('Converted image to fgdb raster.')


def main():
    print('\n\nrunning main()...')
    #
    # Define and create file geodatabase if it doesn't exist
    fgdb = r'E:\assist\demo-data\arcgis\assist.gdb'
    print('\n\n{0:<20}:\t{1}'.format('fgdb', fgdb))
    if not arcpy.Exists(fgdb):
        arcpy.CreateFileGDB_management(out_folder_path=os.path.dirname(fgdb),
                                       out_name=os.path.basename(fgdb),
                                       out_version='CURRENT')
    #
    # Define arcpy environment workspace
    arcpy.env.workspace = fgdb
    #
    # Define processing dictionary
    process_dict = {}
    process_dict['crop_scenario'] = r'E:\assist\demo-data\Demo Data for Tool\CroppingScenarios\cropclass_Baseline.tif'
    process_dict['regions'] = r'E:\assist\demo-data\Demo Data for Tool\Regions\country.tif'
    process_dict['rates'] = r'E:\assist\demo-data\Demo Data for Tool\calories.txt'
    #
    # Display rates
    print('\n\n{0:<20}:\t{1}'.format('rates', process_dict['rates']))
    f = open(process_dict['rates'], 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()
    #
    # Convert images to fgdb rasters
    image_to_raster(process_dict['crop_scenario'], fgdb)
    image_to_raster(process_dict['regions'], fgdb)
    #
    # Set raster processing environment
    print('\n\nSetting raster processing environment...')
    arcpy.env.extent = arcpy.Extent(XMin=0.0, YMin=0.0, XMax=700000.0, YMax=1300000.0)
    arcpy.env.cellSize = 1000.0
    arcpy.env.mask = os.path.splitext(os.path.basename(process_dict['regions']))[0]
    settings = ['extent', 'cellSize', 'mask']
    for setting in settings:
        print('\t{0:<20}:\t{1}'.format('arcpy.env.' + setting, getattr(arcpy.env, setting)))
    print('Set raster processing environment.')
    #
    # Reclassify crop scenario using rates
    print('\n\nReclassifying crop scenario using rates...')
    in_raster = os.path.basename(process_dict['crop_scenario'])
    in_raster = os.path.splitext(in_raster)[0]
    in_raster = os.path.join(fgdb, in_raster)
    in_remap_file = process_dict['rates']
    sa_raster = ReclassByASCIIFile(in_raster=in_raster,
                                    in_remap_file=in_remap_file,
                                    missing_values='NODATA')
    if arcpy.Exists('rates'):
        arcpy.Delete_management('rates')
    sa_raster.save('rates')
    describe_raster('rates')
    print('Reclassified crop scenario using rates.')
    #
    # Zonal statistics for regions - writes to a table
    print('\n\nCreating zonal statistics table...')
    in_zone_data = os.path.basename(process_dict['regions'])
    in_zone_data = os.path.splitext(in_zone_data)[0]
    in_zone_data = os.path.join(fgdb, in_zone_data)
    print(in_zone_data)
    out_table = 'zs_table'
    if arcpy.Exists(out_table):
        arcpy.Delete_management(out_table)
    out_zonal_stats_table = ZonalStatisticsAsTable(in_zone_data=in_zone_data,
                                                   zone_field='Value',
                                                   in_value_raster='rates',
                                                   out_table=out_table,
                                                   ignore_nodata='DATA',
                                                   statistics_type='SUM')
    print('Created zonal statistics table.')






    #
    print('\n\ndone main().\n\n')



if __name__ == '__main__':
    main()
