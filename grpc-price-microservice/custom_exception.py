class Error(Exception):
   """Base class for other exceptions"""
   pass

class NotFoundError(Error):
   """Raised when the value is not found"""
   pass
