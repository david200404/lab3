class ScheduleModule:
    """
    This module handles guest schedule information.
    """
    def __init__(self, guest_id, schedule_details=None):
        self.guest_id = guest_id
        self.schedule_details = schedule_details or "No schedule available."

    def view_schedule(self):
        """
        Displays the schedule for the guest.
        """
        if self.schedule_details:
            print(f"[INFO] Schedule for GuestID={self.guest_id}: {self.schedule_details}")
        else:
            print("[WARNING] No schedule available.")

    def update_schedule(self, new_schedule):
        """
        Updates the schedule for the guest.
        """
        self.schedule_details = new_schedule
        print(f"[INFO] Schedule updated for GuestID={self.guest_id}: {self.schedule_details}")

