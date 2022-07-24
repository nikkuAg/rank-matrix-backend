from datetime import date
from unittest.mock import DEFAULT

from backend.models import getLatestYear

#Serializers Type
NORMAL_SERIALIZER = 'normal serializer'
INSTITUTE_DATA_SERIALIZER = 'normal serializer with institute detail'
BRANCH_DATA_SERIALIZER = 'normal serializer with branch detail'
BRANCH_INSTITUTE_DATA_SERIALIZER = 'normal serializer with branch and institute detail'
FULL_BRANCH_DETAIL_SERIALIZER = 'branch institute data serializer with extra branch information'

#Error Messages
NO_SUCH_INSTITUTE_TYPE_ERROR = "The institute type you choose does not exist."
DATA_DOES_NOT_EXISTS_ERROR = "No corresponding data found."
MODLE_DOES_NOT_EXISTS_ERROR = "Model for the given year does not exists."
DO_NOT_HAVE_PERMISSION_ERROR = "You do not have permission to perform this action."


#Default Value
DEFAULT_INSTITUTE_TYPE = "IIT"
DEFAULT_YEAR = getLatestYear()
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

#Messages
CREATE_SUCCESS = "Data has been populated for the models for the given key"


#Institute Type
INSTITUTE_TYPE_IIT = "IIT"
INSTITUTE_TYPE_NIT = "NIT"
INSTITUTE_TYPE_IIIT = "IIIT"
INSTITUTE_TYPE_GFTI = "GFTI"