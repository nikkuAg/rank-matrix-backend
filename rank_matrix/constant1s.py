from datetime import date
from unittest.mock import DEFAULT

# from rank_matrix.models import getLatestYear

# Serializers Type
NORMAL_SERIALIZER = 'normal serializer'
INSTITUTE_DATA_SERIALIZER = 'normal serializer with college detail'
BRANCH_DATA_SERIALIZER = 'normal serializer with branch detail'
BRANCH_INSTITUTE_DATA_SERIALIZER = 'normal serializer with branch and college detail'
FULL_BRANCH_DETAIL_SERIALIZER = 'branch college data serializer with extra branch information'

# Error Messages
NO_SUCH_INSTITUTE_TYPE_ERROR = "The college type you choose does not exist."
DATA_DOES_NOT_EXISTS_ERROR = "No corresponding data found."
MODLE_DOES_NOT_EXISTS_ERROR = "Model for the given year does not exists."
DO_NOT_HAVE_PERMISSION_ERROR = "You do not have permission to perform this action."
ERROR_OCCURED = "Some error occured"

# Default Value
DEFAULT_INSTITUTE_TYPE = "IIT"
# DEFAULT_YEAR = getLatestYear()
DEFAULT_ROUND_NUMBER = 6
DEFAULT_ROUND_TYPE = 'rounds'
DEFAULT_CATEGORY = 'General'
DEFAULT_QUOTA = 'AI'
DEFAULT_SEAT_POOL = 'Gender-Neutral'
CLOSING_OPTION = 'closing'
DEFAULT_BRANCH_AND_INSTITUTE_EXISTS = 'Y'
DEFAULT_SEAT_INCREASE = False
DEFAULT_NULL = None
DEFAULT_CUTOFF = 10
DEFAULT_NUMBER_TYPE = 1
DEFAULT_TRUE = True

# Messages
CREATE_SUCCESS = "Data has been populated"
CREATE_FILE_FAILED = "File not found at that location"
CREATE_PARTIAL = "Data was populated partially"

# College Type
INSTITUTE_TYPE_IIT = "IIT"
INSTITUTE_TYPE_NIT = "NIT"
INSTITUTE_TYPE_IIIT = "IIIT"
INSTITUTE_TYPE_GFTI = "GFTI"
