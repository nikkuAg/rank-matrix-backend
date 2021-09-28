import pandas as pd

branch_data = pd.read_csv(
    'database/CSV/List_of_Branches.csv', sep=',', header=0, na_filter=False)
inst_data = pd.read_csv(
    'database/CSV/List_of_Institute.csv', sep=',', header=0, na_filter=False)
data_2015 = pd.read_csv(
    'database/CSV/Rounds/Round_2015.csv', sep=',', header=0, na_filter=False)
data_2016_1 = pd.read_csv(
    'database/CSV/Rounds/Round1_2016.csv', sep=',', header=0, na_filter=False)
data_2016_6 = pd.read_csv(
    'database/CSV/Rounds/Round6_2016.csv', sep=',', header=0, na_filter=False)
data_2017_1 = pd.read_csv(
    'database/CSV/Rounds/Round1_2017.csv', sep=',', header=0, na_filter=False)
data_2017_7 = pd.read_csv(
    'database/CSV/Rounds/Round7_2017.csv', sep=',', header=0, na_filter=False)
data_2018_1 = pd.read_csv(
    'database/CSV/Rounds/Round1_2018.csv', sep=',', header=0, na_filter=False)
data_2018_7 = pd.read_csv(
    'database/CSV/Rounds/Round7_2018.csv', sep=',', header=0, na_filter=False)
data_2019_1 = pd.read_csv(
    'database/CSV/Rounds/Round1_2019.csv', sep=',', header=0, na_filter=False)
data_2019_7 = pd.read_csv(
    'database/CSV/Rounds/Round7_2019.csv', sep=',', header=0, na_filter=False)
data_2020_1 = pd.read_csv(
    'database/CSV/Rounds/Round1_2020.csv', sep=',', header=0, na_filter=False)
data_2020_2 = pd.read_csv(
    'database/CSV/Rounds/Round2_2020.csv', sep=',', header=0, na_filter=False)
data_2020_3 = pd.read_csv(
    'database/CSV/Rounds/Round3_2020.csv', sep=',', header=0, na_filter=False)
data_2020_4 = pd.read_csv(
    'database/CSV/Rounds/Round4_2020.csv', sep=',', header=0, na_filter=False)
data_2020_5 = pd.read_csv(
    'database/CSV/Rounds/Round5_2020.csv', sep=',', header=0, na_filter=False)
data_2020_6 = pd.read_csv(
    'database/CSV/Rounds/Round6_2020.csv', sep=',', header=0, na_filter=False)
data_2020_CSAB1 = pd.read_csv(
    'database/CSV/Rounds/CSAB_2020_Round1.csv', sep=',', header=0, na_filter=False)
data_2020_CSAB2 = pd.read_csv(
    'database/CSV/Rounds/CSAB_2020_Round2.csv', sep=',', header=0, na_filter=False)
data_2020_provisonal = pd.read_csv(
    'database/CSV/Rounds/Round_2020_P.csv', sep=',', header=0, na_filter=False)
data_2018_provisonal = pd.read_csv(
    'database/CSV/Rounds/Round_2018_P.csv', sep=',', header=0, na_filter=False)
data_2019_provisonal = pd.read_csv(
    'database/CSV/Rounds/Round_2019_P.csv', sep=',', header=0, na_filter=False)
data_2020_seats = pd.read_csv(
    'database/CSV/Seat_Matrix_2020.csv', sep=',', header=0, na_filter=False)
data_2019_seats = pd.read_csv(
    'database/CSV/Seat_Matrix_2019.csv', sep=',', header=0, na_filter=False)
data_CSAB_seats = pd.read_csv(
    'database/CSV/Seat_Matrix_CSAB.csv', sep=',', header=0, na_filter=False)


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
    '2020_1': data_2020_CSAB1,
    '2020_2': data_2020_CSAB2,
    'sional_2018': data_2018_provisonal,
    'sional_2019': data_2019_provisonal,
    'sional_2020': data_2020_provisonal,
    'atrix_2020': data_2020_seats,
    'atrix_2019': data_2019_seats,
    'atrix_2020_csab': data_CSAB_seats,
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
round1_2020_CSAB = []
round2_2020_CSAB = []
round_2018_provisonal = []
round_2019_provisonal = []
round_2020_provisonal = []
seats_2020 = []
seats_2019 = []
seats_CSAB = []


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
    '2020_1': round1_2020_CSAB,
    '2020_2': round2_2020_CSAB,
    'sional_2018': round_2018_provisonal,
    'sional_2019': round_2019_provisonal,
    'sional_2020': round_2020_provisonal,
    'atrix_2020': seats_2020,
    'atrix_2019': seats_2019,
    'atrix_2020_csab': seats_CSAB,
}


viewset_url = ['branches', 'institutes', '1_2016', '1_2017', '1_2018', '1_2019', '1_2020', '2_2020',
               '3_2020', '4_2020', '5_2020', '6_2016', '6_2020', '7_2017', '7_2018', '7_2019', '_2015', 'provisional_2018', 'provisional_2019', 'provisional_2020', 'csab1_2020', 'csab2_2020', 'seat_2019', 'seat_2020', 'seat_csab_2020']
