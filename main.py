from guest_module import GuestModule
from badge_module import BadgeModule
from schedule_module import ScheduleModule
from permission_module import PermissionModule
from reception_module import ReceptionModule
from admin_module import AdminModule

def main():
    """
    Main program entry point.
    """
    # Initialize admin and guest objects
    admin = AdminModule("Admin123", "password")
    guest = GuestModule("John Doe", "G123", "VIP")

    badge = BadgeModule("B456", "G123", "EventA")
    schedule = ScheduleModule("G123", "Opening Ceremony at 10:00 AM")
    reception = ReceptionModule("G123", "Lunch at 12:00 PM, Room 101")
    permission = PermissionModule("G123")

    # Admin login
    print("\n--- Admin Login ---")
    admin.login("Admin123", "password")

    if admin.is_logged_in:
        # Admin operations
        print("\n--- Admin Issuing Badge ---")
        badge.issue_badge()

        print("\n--- Admin Setting Permission ---")
        permission.set_permission(True)

        print("\n--- Updating Guest Schedule ---")
        schedule.update_schedule("Keynote Speech at 2:00 PM")

        print("\n--- Updating Reception Plan ---")
        reception.update_reception_plan("Dinner at 7:00 PM, Ballroom")

        # Guest operations
        print("\n--- Guest Viewing Schedule ---")
        schedule.view_schedule()

        print("\n--- Guest Viewing Reception Plan ---")
        reception.view_reception_plan()

        print("\n--- Displaying Guest Info ---")
        guest.display_guest_info()

        # Admin logout
        print("\n--- Admin Logout ---")
        admin.logout()

if __name__ == "__main__":
    main()

