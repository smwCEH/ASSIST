import os
import sys
import collections
from PIL import Image
import numpy as np


def report_array(tif):
    im = Image.open(tif)
    imarray = np.array(im)
    print('\timarray.shape:\t\t{0}'.format(imarray.shape))
    print('\timarray.size:\t\t{0}'.format(imarray.size))
    unique = np.unique(imarray, return_counts=True)
    print('\tnp.unique[0]:\t\t{0}'.format(unique[0]))
    print('\tnp.unique[1]:\t\t{0}'.format(unique[1]))
    print('\tnp.unique[1].sum:\t\t{0}'.format(np.sum(unique[1])))
    del im, imarray


def get_rates(csv_path):
    print('\n\ngetting rates...')
    # Create empty ordered dictionary
    rates_dict = collections.OrderedDict()
    # From csv get rates and add to a nested ordered dictionary
    lines = np.genfromtxt(csv_path, delimiter=',', dtype=None)
    ncols = len(lines[0])
    print('ncols:\t\t{0}'.format(ncols))
    for i in range(len(lines)):
        # print(lines[i])
        if i == 0:
            for j in range(1, ncols):
                # print(lines[i][j])
                variable = 'variable' + str(j)
                # print(variable)
                rates_dict[variable] = collections.OrderedDict()
                rates_dict[variable]['units'] = lines[i][j]
                if j == 1:
                    rates_dict[variable]['name'] = 'calories'
                elif j == 2:
                    rates_dict[variable]['name'] = 'income'
                else:
                    sys.exit()
        else:
            for j in range(1,ncols):
                variable = 'variable' + str(j)
                # print(variable)
                # print(lines[i][j])
                rates_dict[variable][int(lines[i][0])] = float(lines[i][j])
    #
    print('got rates.')
    return rates_dict


def main():
    print('\n\nrunning main()...')
    #
    # Define csv of model rates
    csv_folder = r'E:\assist\demo-data\Demo Data for Tool'
    csv_file = r'CropClass_Calories_and_Income.csv'
    csv_path = os.path.join(csv_folder, csv_file)
    print('\n\ncsv_path:\t\t{0}'.format(csv_path))
    #
    # Get ordered dictionary of model rates
    model_dict = get_rates(csv_path)
    print('\n\n')
    print(model_dict)
    print(model_dict['variable1'])
    print(model_dict['variable1']['name'])
    print(model_dict['variable1']['units'])
    print(model_dict['variable1'][1])
    print(model_dict['variable1'][8])
    #
    # Define land cover scenarios ordered dictionary
    lc_scenarios_folder = r'E:\assist\demo-data\Demo Data for Tool\LandCoverScenarios'
    lc_scenarios_dict = collections.OrderedDict()
    lc_scenarios_dict['baseline'] = collections.OrderedDict()
    lc_scenarios_dict['baseline']['image'] = os.path.join(lc_scenarios_folder, r'LC_Baseline.tif')
    lc_scenarios_dict['baseline']['label'] = 'current pattern based on LCM2007'
    lc_scenarios_dict['a_np_x'] = collections.OrderedDict()
    lc_scenarios_dict['a_np_x']['image'] = os.path.join(lc_scenarios_folder, r'LC_scenario_A_NP_X.tif')
    lc_scenarios_dict['a_np_x']['label'] = 'Expansion of arable land in 5% increments, SSSIs not protected'
    lc_scenarios_dict['a_p_x'] = collections.OrderedDict()
    lc_scenarios_dict['a_p_x']['image'] = os.path.join(lc_scenarios_folder, r'LC_scenario_A_P_X.tif')
    lc_scenarios_dict['a_p_x']['label'] = 'Expansion of arable land in 5% increments, SSSIs protected'
    lc_scenarios_dict['a_gsn_x'] = collections.OrderedDict()
    lc_scenarios_dict['a_gsn_x']['image'] = os.path.join(lc_scenarios_folder, r'LC_scenario_A_GSN_X.tif')
    lc_scenarios_dict['a_gsn_x']['label'] = 'Expansion of grassland in 5% increments, SSSIs protected'
    print('\n\n')
    print(lc_scenarios_dict)
    #
    # Define cropping scenarios ordered dictionary
    cropping_scenarios_folder = r'E:\assist\demo-data\Demo Data for Tool\CroppingScenarios'
    cropping_scenarios_dict = collections.OrderedDict()
    cropping_scenarios_dict['baseline'] = collections.OrderedDict()
    cropping_scenarios_dict['baseline']['image'] = os.path.join(lc_scenarios_folder, r'cropclass_Baseline.tif')
    cropping_scenarios_dict['baseline']['label'] = 'current pattern based on LCM+Crops2015'
    cropping_scenarios_dict['o'] = collections.OrderedDict()
    cropping_scenarios_dict['o']['image'] = os.path.join(cropping_scenarios_folder, r'cropclass_O.tif')
    cropping_scenarios_dict['o']['label'] = 'Expansion of cropping systems to fill the land for which they are best suited, with priority going the most productive systems'
    cropping_scenarios_dict['h'] = collections.OrderedDict()
    cropping_scenarios_dict['h']['image'] = os.path.join(cropping_scenarios_folder, r'cropclass_H.tif')
    cropping_scenarios_dict['h']['label'] = 'Expasion of industrial crops under simple rotations'
    cropping_scenarios_dict['e'] = collections.OrderedDict()
    cropping_scenarios_dict['e']['image'] = os.path.join(cropping_scenarios_folder, r'cropclass_E.tif')
    cropping_scenarios_dict['e']['label'] = 'Expasion of mixed grass-crop systems, spring cropping and complex rotations where land permits'
    print('\n\n')
    print(cropping_scenarios_dict)
    #
    # Define regions ordered dictionary
    regions_folder = r'E:\assist\demo-data\Demo Data for Tool\Regions'
    regions_dict = collections.OrderedDict()
    regions_dict['country'] = collections.OrderedDict()
    regions_dict['country']['image'] = os.path.join(regions_folder, r'county.tif')
    regions_dict['country']['label'] = 'countries'
    regions_dict['euroregion'] = collections.OrderedDict()
    regions_dict['euroregion']['image'] = os.path.join(regions_folder, r'euroregion.tif')
    regions_dict['euroregion']['label'] = 'euroregion'
    print('\n\n')
    print(regions_dict)


    #
    print('\n\ndone main().')



if __name__ == '__main__':
    main()








# print('\n\nCroping Scenarios')
# tif_folder = r'E:\assist\demo-data\Demo Data for Tool\CroppingScenarios'
# tif_list = ['cropclass_Baseline.tif',
#             'cropclass_scenario_O.tif', 'cropclass_scenario_H.tif', 'cropclass_scenario_E.tif']
# for tif in tif_list:
#     tif_path = os.path.join(tif_folder, tif)
#     print('TIF:\t\t{0}'.format(tif_path))
#     report_array(tif)
#
#
# print('\n\nLand Cover Scenarios')
# tif_folder = r'E:\assist\demo-data\Demo Data for Tool\LandCoverScenarios'
# tif_list = ['LC_Baseline.tif',
#             'LC_scenario_GSN_5.tif', 'LC_scenario_GSN_10.tif', 'LC_scenario_GSN_15.tif', 'LC_scenario_GSN_20.tif', 'LC_scenario_GSN_25.tif', 'LC_scenario_GSN_30.tif',
#             'LC_scenario_A_P_5.tif', 'LC_scenario_A_P_10.tif', 'LC_scenario_A_P_15.tif', 'LC_scenario_A_P_20.tif', 'LC_scenario_A_P_25.tif', 'LC_scenario_A_P_30.tif',
#             'LC_scenario_A_NP_5.tif', 'LC_scenario_A_NP_10.tif', 'LC_scenario_A_NP_15.tif', 'LC_scenario_A_NP_20.tif', 'LC_scenario_A_NP_25.tif', 'LC_scenario_A_NP_30.tif']
# for tif in tif_list:
#     tif_path = os.path.join(tif_folder, tif)
#     print('TIF:\t\t{0}'.format(tif_path))
#     report_array(tif)
#
#
# print('\n\nMasks')
# tif_folder = r'E:\assist\demo-data\Demo Data for Tool\Masks\Masks'
# tif_list = ['country.tif', 'euroregion.tif']
# for tif in tif_list:
#     tif_path = os.path.join(tif_folder, tif)
#     print('TIF:\t\t{0}'.format(tif_path))
#     report_array(tif)