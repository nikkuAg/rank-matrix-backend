from rank_matrix.models.college_type import College_Type

def get_college_type():
    """
    Returns:
        list: All available college types
    """
    type = []
    try:
        types = College_Type.objects.all()
        for x in types:
            type.append(x.type)
    except:
        return

    return type