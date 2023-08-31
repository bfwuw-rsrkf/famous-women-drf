from rest_framework.pagination import PageNumberPagination


class PaginationWoman(PageNumberPagination):
    page_size = 4
    max_page_size = 10000
