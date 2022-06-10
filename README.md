# Updating the Backend

- Create model for each round in `models.py` file.
- Add respective models data in `lists` created in end of `models.py` file.
- Create serializers for each of the new models in `serializers.py` file.
- Create a new folder for viewset for that particular year in `customViews/{vYear}` or in `customViews/SeatMatrix`.
- Add created viewsets in the `variableData.py` file and also add respective urls.