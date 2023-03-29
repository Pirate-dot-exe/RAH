from kivy.utils import platform
from enum import Enum

def ask_permission():
    if platform == 'android':
        from android.permissions import request_permission, check_permission, Permission

    if platform == 'win':
        print("no permissions required")

class PermissionRequestState(Enum):
    UNKNOWN = "UNKNOWN"
    HAVE_PERMISSION = "HAVE_PERMISSION"
    DO_NOT_HAVE_PERMISSION = "DO_NOT_HAVE_PERMISSION"
    AWAITING_REQUEST_RESPONSE = "AWAITING_REQUEST_RESPONSE"