from backend.models.round import Round1, Round2, Round3, Round4, Round5, Round6, Round7
from backend.serializers.opening_closing_rank import Round1Serializer, Round2Serializer, Round3Serializer, Round4Serializer, Round5Serializer, Round6Serializer, Round7Serializer


def get_round_model(round):
  models = [Round1, Round2, Round3, Round4, Round5, Round6, Round7]
  return models[round-1]

def get_round_serializer(round):
  serializers = [Round1Serializer, Round2Serializer, Round3Serializer, Round4Serializer, 
                 Round5Serializer, Round6Serializer, Round7Serializer]
  return serializers[round-1]
  