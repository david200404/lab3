class BadgeModule:
    """
    This module handles badge issuance for guests.
    """
    def __init__(self, badge_id, guest_id, source):
        self.badge_id = badge_id
        self.guest_id = guest_id
        self.source = source

    def issue_badge(self):
        """
        Issues a badge for the specified guest.
        """
        print(f"[INFO] Badge issued: BadgeID={self.badge_id}, GuestID={self.guest_id}, Source={self.source}")

