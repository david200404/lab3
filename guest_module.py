class GuestModule:
    """
    This module manages guest information.
    """
    def __init__(self, guest_name, guest_id, guest_type):
        self.guest_name = guest_name
        self.guest_id = guest_id
        self.guest_type = guest_type

    def update_guest_info(self, name=None, guest_type=None):
        """
        Updates guest information such as name or type.
        """
        if name:
            self.guest_name = name
        if guest_type:
            self.guest_type = guest_type
        print(f"[INFO] Guest info updated: Name={self.guest_name}, Type={self.guest_type}")

    def display_guest_info(self):
        """
        Displays guest information.
        """
        print(f"Guest Information: Name={self.guest_name}, ID={self.guest_id}, Type={self.guest_type}")

