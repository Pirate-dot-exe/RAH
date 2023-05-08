from kivy.utils import platform
from enum import Enum

def ask_permission():
    if platform == 'android':
        from android.permissions import request_permissions, Permission
        
        request_permissions([
            Permission.CAMERA,
            Permission.WRITE_EXTERNAL_STORAGE,
            Permission.READ_EXTERNAL_STORAGE,
            Permission.BLUETOOTH_CONNECT,
            Permission.BLUETOOTH_SCAN
        ])

    if platform == 'win':
        pass

class PermissionRequestState(Enum):
    UNKNOWN = "UNKNOWN"
    HAVE_PERMISSION = "HAVE_PERMISSION"
    DO_NOT_HAVE_PERMISSION = "DO_NOT_HAVE_PERMISSION"
    AWAITING_REQUEST_RESPONSE = "AWAITING_REQUEST_RESPONSE"