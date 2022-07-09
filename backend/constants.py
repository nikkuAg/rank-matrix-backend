from datetime import date
from unittest.mock import DEFAULT

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
DEFAULT_YEAR = date.today().year - 1
DEFAULT_ROUND_NUMBER = 6
DEFAULT_ROUND_TYPE = 'rounds'
DEFAULT_CATEGORY = 'General'
DEFAULT_QUOTA = 'AI'
DEFAULT_GENDER = 'Gender-Neutral'
DEFAULT_RANK_OPTION = 'closing'
DEFAULT_BRANCH_AND_INSTITUTE_EXISTS = 'y'
DEFAULT_SEAT_INCREASE = False

#Messages
CREATE_SUCCESS = "Data has been populated for the models for the given key"