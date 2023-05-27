from rank_matrix_stage.models.college_type import CollegeType

def get_college_type():
    """
    Returns:
        list: All available college types
    """
    type = []
    try:
        types = CollegeType.objects.all()
        for x in types:
            type.append(x.type)
    except:
        return

    return type