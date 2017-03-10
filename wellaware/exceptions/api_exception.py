
class ApiException(Exception):
    """
    Generic Catch-all for API Exceptions.
    """

    status_code = None

    def __init__(self, status_code=None, *args, **kwargs):
        self.status_code = status_code
        super(ApiException).__init__(self, *args, **kwargs)
