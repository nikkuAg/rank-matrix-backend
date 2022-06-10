from .views import BranchesViewSet, College_BranchViewSet, College_CategoryViewSet, InstitutesViewSet, UpdatesViewSet
from .customViews.SeatMatrix.views import CSAB_Seat_2020ViewSet, Seat_2019ViewSet, Seat_2020ViewSet, Seat_2021IViewSet, Seat_2021ViewSet
from .customViews.v2017.views import Round1_2017ViewSet, Round2_2017ViewSet, Round3_2017ViewSet, Round4_2017ViewSet, Round5_2017ViewSet, Round6_2017ViewSet, Round7_2017ViewSet
from .customViews.v2018.views import Provisional_2018ViewSet, Round1_2018ViewSet, Round2_2018ViewSet, Round3_2018ViewSet, Round4_2018ViewSet, Round5_2018ViewSet, Round6_2018ViewSet, Round7_2018ViewSet
from .customViews.v2019.views import Provisional_2019ViewSet, Round1_2019ViewSet, Round2_2019ViewSet, Round3_2019ViewSet, Round4_2019ViewSet, Round5_2019ViewSet, Round6_2019ViewSet, Round7_2019ViewSet
from .customViews.v2020.views import CSAB_2020_1ViewSet, CSAB_2020_2ViewSet, Provisional_2020ViewSet, Round1_2020ViewSet, Round2_2020ViewSet, Round3_2020ViewSet, Round4_2020ViewSet, Round5_2020ViewSet, Round6_2020ViewSet
from .customViews.v2021.views import Round1_2021ViewSet, Round2_2021ViewSet, Round3_2021ViewSet, Round4_2021ViewSet, Round5_2021ViewSet, Round6_2021ViewSet
from .customViews.v2016.views import Round1_2016ViewSet, Round2_2016ViewSet, Round3_2016ViewSet, Round4_2016ViewSet, Round5_2016ViewSet, Round6_2016ViewSet
from .customViews.v2015.views import Round_2015ViewSet




viewset_list = [BranchesViewSet, InstitutesViewSet,UpdatesViewSet, College_BranchViewSet,College_CategoryViewSet,
                Round_2015ViewSet,
                Round1_2016ViewSet,  Round2_2016ViewSet, Round3_2016ViewSet, Round4_2016ViewSet, Round5_2016ViewSet, Round6_2016ViewSet,
                Round1_2017ViewSet, Round2_2017ViewSet, Round3_2017ViewSet, Round4_2017ViewSet, Round5_2017ViewSet, Round6_2017ViewSet, Round7_2017ViewSet,
                Round1_2018ViewSet, Round2_2018ViewSet, Round3_2018ViewSet, Round4_2018ViewSet, Round5_2018ViewSet, Round6_2018ViewSet,Round7_2018ViewSet, Provisional_2018ViewSet,
                Round1_2019ViewSet, Round2_2019ViewSet, Round3_2019ViewSet, Round4_2019ViewSet, Round5_2019ViewSet, Round6_2019ViewSet, Round7_2019ViewSet, Provisional_2019ViewSet, Seat_2019ViewSet,
                Round1_2020ViewSet, Round2_2020ViewSet,Round3_2020ViewSet, Round4_2020ViewSet, Round5_2020ViewSet, Round6_2020ViewSet,Provisional_2020ViewSet, CSAB_2020_1ViewSet, CSAB_2020_2ViewSet,Seat_2020ViewSet, CSAB_Seat_2020ViewSet,
                Round1_2021ViewSet, Round2_2021ViewSet, Round3_2021ViewSet, Round4_2021ViewSet, Round5_2021ViewSet, Round6_2021ViewSet, Seat_2021ViewSet, Seat_2021IViewSet]


viewset_url = ['branches', 'institutes', 'update', 'college_branch', 'college_category',
               '7_2015',
               '1_2016', '2_2016', '3_2016', '4_2016', '5_2016', '6_2016',
               '1_2017', '2_2017', '3_2017', '4_2017', '5_2020', '6_2020', '7_2017'
               '1_2018', '2_2018', '3_2017', '4_2017', '5_2020', '6_2020', '7_2018', 'provisional_2018',
               '1_2019', '2_2019', '3_2017', '4_2017', '5_2020', '6_2020', '7_2019', 'provisional_2019', 'seat_2019'
               '1_2020', '2_2020', '3_2020', '4_2020', '5_2020', '6_2020', 'provisional_2020', '1_csab_2020', '2_csab_2020', 'seat_2020', 'seat_csab_2020',
               '1_2021', '2_2021', '3_2021', '4_2021', '5_2021', '6_2021', 'seat_2021', 'seat_2021I',]
