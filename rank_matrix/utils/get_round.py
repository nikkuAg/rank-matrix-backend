from rank_matrix.models.round import Round1, Round2, Round3, Round4, Round5, Round6, Round7
from rank_matrix.serializers.opening_closing_rank import Round1Serializer, Round2Serializer, Round3Serializer, Round4Serializer, Round5Serializer, Round6Serializer, Round7Serializer

MODELS = [Round1, Round2, Round3, Round4, Round5, Round6, Round7]
MODEL_SERIALIZERS = [Round1Serializer, Round2Serializer, Round3Serializer, Round4Serializer, 
	Round5Serializer, Round6Serializer, Round7Serializer]

def get_round_model(round):
    """
    Args:
        round (int): Round number

    Returns:
        model: Round Model for the round number provided
    """
    return MODELS[round-1]

def get_round_serializer(round):
    """
    Args:
        round (int): Round number

    Returns:
        serializer: Round Serializer for the round number provided
    """
    return MODEL_SERIALIZERS[round-1]
  
def get_all_round_model():
    """
    Returns:
        list: List of all round models
    """
    return MODELS
