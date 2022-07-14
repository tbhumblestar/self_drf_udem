from rest_framework.pagination import (
                                    PageNumberPagination,
                                    LimitOffsetPagination,
                                    CursorPagination
)

class WatchListPagination(PageNumberPagination):
    page_size = 10

    
class LOPagination(LimitOffsetPagination):
    default_limit = 10
    offset_query_param = 'start'
    max_limit = 20

    
class CPagination(CursorPagination):
    page_size = 10
    ordering = 'created_at'
    cursor_query_param = 'record'