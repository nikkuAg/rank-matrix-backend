import pandas as pd

branch_data = pd.read_csv(
    'database/List_of_Branches.csv', sep=',', header=0, na_filter=False)
inst_data = pd.read_csv(
    'database/List_of_Institute.csv', sep=',', header=0, na_filter=False)
data_2015 = pd.read_csv(
    'database/Round_2015.csv', sep=',', header=0, na_filter=False)
data_2016_1 = pd.read_csv(
    'database/Round_1_2016.csv', sep=',', header=0, na_filter=False)
data_2016_6 = pd.read_csv(
    'database/Round_6_2016.csv', sep=',', header=0, na_filter=False)
data_2017_1 = pd.read_csv(
    'database/Round_1_2017.csv', sep=',', header=0, na_filter=False)
data_2017_7 = pd.read_csv(
    'database/Round_7_2017.csv', sep=',', header=0, na_filter=False)
data_2018_1 = pd.read_csv(
    'database/Round_1_2018.csv', sep=',', header=0, na_filter=False)
data_2018_7 = pd.read_csv(
    'database/Round_7_2018.csv', sep=',', header=0, na_filter=False)
data_2019_1 = pd.read_csv(
    'database/Round_1_2019.csv', sep=',', header=0, na_filter=False)
data_2019_7 = pd.read_csv(
    'database/Round_7_2019.csv', sep=',', header=0, na_filter=False)
data_2020_1 = pd.read_csv(
    'database/Round_1_2020.csv', sep=',', header=0, na_filter=False)
data_2020_2 = pd.read_csv(
    'database/Round_2_2020.csv', sep=',', header=0, na_filter=False)
data_2020_3 = pd.read_csv(
    'database/Round_3_2020.csv', sep=',', header=0, na_filter=False)
data_2020_4 = pd.read_csv(
    'database/Round_4_2020.csv', sep=',', header=0, na_filter=False)
data_2020_5 = pd.read_csv(
    'database/Round_5_2020.csv', sep=',', header=0, na_filter=False)
data_2020_6 = pd.read_csv(
    'database/Round_6_2020.csv', sep=',', header=0, na_filter=False)


data_list = {
    'branch': branch_data,
    'institute': inst_data,
    '_2015': data_2015,
    '1_2016': data_2016_1,
    '6_2016': data_2016_6,
    '1_2017': data_2017_1,
    '7_2017': data_2017_7,
    '1_2018': data_2018_1,
    '7_2018': data_2018_7,
    '1_2019': data_2019_1,
    '7_2019': data_2019_7,
    '1_2020': data_2020_1,
    '2_2020': data_2020_2,
    '3_2020': data_2020_3,
    '4_2020': data_2020_4,
    '5_2020': data_2020_5,
    '6_2020': data_2020_6,
}

round_2015 = []
round_1_2016 = []
round_6_2016 = []
round_1_2017 = []
round_7_2017 = []
round_1_2018 = []
round_7_2018 = []
round_1_2019 = []
round_7_2019 = []
round_1_2020 = []
round_2_2020 = []
round_3_2020 = []
round_4_2020 = []
round_5_2020 = []
round_6_2020 = []

lists = {
    '_2015': round_2015,
    '1_2016': round_1_2016,
    '6_2016': round_6_2016,
    '1_2017': round_1_2017,
    '7_2017': round_7_2017,
    '1_2018': round_1_2018,
    '7_2018': round_7_2018,
    '1_2019': round_1_2019,
    '7_2019': round_7_2019,
    '1_2020': round_1_2020,
    '2_2020': round_2_2020,
    '3_2020': round_3_2020,
    '4_2020': round_4_2020,
    '5_2020': round_5_2020,
    '6_2020': round_6_2020,
}


viewset_url = ['branches', 'institutes', '1_2016', '1_2017', '1_2018', '1_2019', '1_2020', '2_2020',
               '3_2020', '4_2020', '5_2020', '6_2016', '6_2020', '7_2017', '7_2018', '7_2019', '_2015']
