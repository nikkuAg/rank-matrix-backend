from rank_matrix.models.round import Round1, Round2, Round3, Round4, Round5, Round6, Round7
from rank_matrix.serializers.opening_closing_rank import Round1Serializer, Round2Serializer, Round3Serializer, Round4Serializer, Round5Serializer, Round6Serializer, Round7Serializer

MODELS = [Round1, Round2, Round3, Round4, Round5, Round6, Round7]
MODEL_SERIALIZERS = [Round1Serializer, Round2Serializer, Round3Serializer, Round4Serializer,
                     Round5Serializer, Round6Serializer, Round7Serializer]


def get_round_model(round: int):
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


def get_total_exisiting_round_count():
    """
    Returns:
        int: Total number of round models that exists
    """
    return len(MODELS)


def year_exists_in_round(round: int, year: int):
    return bool(get_round_model(round).objects.filter(year=year).count())


def get_last_round(year: int):
    """
    This function provides the last round that exists for the year

    Args:
        year (int): Year for which last round needs to be found

    Returns:
        int: Last Round for the year
    """
    round_count = get_total_exisiting_round_count()
    for i in range(round_count, 0, -1):
        if year_exists_in_round(i, year):
            return i

    return -1


def get_round_list(year: int):
    """
    This function provides the list of rounds available in given year

    Args:
        year (int): Year for rounds need to be found

    Returns:
        list: Rounds available in a year
    """
    rounds = list()
    for index in range(len(MODELS)):
        if year_exists_in_round(index+1, year):
            rounds.append(f'Round {index+1}')
    return rounds
