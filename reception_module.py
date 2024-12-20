class ReceptionModule:
    """
    This module manages reception plans for guests.
    """
    def __init__(self, guest_id, reception_details=None):
        self.guest_id = guest_id
        self.reception_details = reception_details or "No reception plan available."

    def view_reception_plan(self):
        """
        Displays the reception plan for the guest.
        """
        print(f"[INFO] Reception Plan for GuestID={self.guest_id}: {self.reception_details}")

    def update_reception_plan(self, new_plan):
        """
        Updates the reception plan for the guest.
        """
        self.reception_details = new_plan
        print(f"[INFO] Reception plan updated for GuestID={self.guest_id}: {self.reception_details}")

