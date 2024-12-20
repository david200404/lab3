class PermissionModule:
    """
    This module manages guest permissions.
    """
    def __init__(self, guest_id, has_permission=False):
        self.guest_id = guest_id
        self.has_permission = has_permission

    def set_permission(self, permission):
        """
        Sets the permission for the guest.
        """
        self.has_permission = permission
        status = "granted" if permission else "denied"
        print(f"[INFO] Permission for GuestID={self.guest_id} has been {status}.")

