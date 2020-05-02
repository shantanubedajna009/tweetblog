from rest_framework import pagination

class StandardResultsPagination(pagination.PageNumberPagination):
    page_size = 10
    page_query_param = "page_number_size"
    max_page_size = 1000