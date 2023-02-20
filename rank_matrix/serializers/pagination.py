from rest_framework import serializers, pagination, response

class CustomPaginationSerializer(pagination.PageNumberPagination):
    """
    Serializer for fields to be available for paginations
    """
    
    def get_paginated_response(self, data):
        return response.Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })
