import json

class USNParser:
    def __init__(self, usn_file):
        self.usn_file = usn_file
        self.usn_data = None

    def load_usn(self):
        """Load USN data from a file."""
        try:
            with open(self.usn_file, "r") as f:
                self.usn_data = json.load(f)
            return True
        except FileNotFoundError:
            print(f"USN file not found: {self.usn_file}")
            return False
        except json.JSONDecodeError as e:
            print(f"Error parsing USN file: {e}")
            return False

    def get_vulnerable_packages(self, os_version):
        """Get a list of vulnerable packages for a specific OS version."""
        if not self.usn_data:
            raise Exception("USN data is not loaded.")
        
        vulnerable_packages = []
        for entry in self.usn_data.get("notices", []):
            affected_versions = entry.get("affected_versions", {})
            if os_version in affected_versions:
                vulnerable_packages.extend(entry.get("packages", []))
        
        return set(vulnerable_packages)  # Remove duplicates
