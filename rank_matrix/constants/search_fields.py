COLLEGE_LIST_SEARCH = ['code', 'name', 'state', 'city', 'college_type__type',
        'nirf_1', 'nirf_2', 'nirf_3', 'website']

COLLEGE_LIST_MINIMAL_SEARCH = ['code', 'name', 'display_code']

SEAT_MATRIX_SEARCH = ['quota', 'category', 'seat_pool', 'seats', 'institute_code__name',
        'institute_code__display_code','institute_code__city', 'institute_code__state',
        'institute_code__college_type__type', 'branch_code__branch_name','branch_code__branch_code', 
        'branch_code__duration', 'branch_code__degree']

OPENING_CLOSING_SEARCH = ['quota', 'category', 'seat_pool', 'opening_rank', 'closing_rank', 'institute_code__name',
        'institute_code__display_code','institute_code__city', 'institute_code__state', 'institute_code__category',
        'branch_code__branch_name','branch_code__branch_code', 'branch_code__duration']

ALL_COLLEGE_ONE_BRANCH_INSTITUTE_SEARCH = ['branch_name', 'code', 'branch_code', 'duration', 'degree']