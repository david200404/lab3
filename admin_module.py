class AdminModule:
    """
    This module handles administrator login and operations.
    """
    def __init__(self, admin_name, admin_password):
        self.admin_name = admin_name
        self.admin_password = admin_password
        self.is_logged_in = False

    def login(self, name, password):
        """
        Logs in the administrator.
        """
        if name == self.admin_name and password == self.admin_password:
            self.is_logged_in = True
            print(f"[INFO] Admin {self.admin_name} logged in successfully.")
        else:
            print("[ERROR] Invalid admin credentials.")

    def logout(self):
        """
        Logs out the administrator.
        """
        self.is_logged_in = False
        print(f"[INFO] Admin {self.admin_name} logged out.")

