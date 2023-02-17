from backend.models.college_type import College_Type

def get_college_type():
    type = []
    try:
        types = College_Type.objects.all()
        for x in types:
            type.append(x.type)
    except:
        return

    return type