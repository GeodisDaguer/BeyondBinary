import json
import hashlib
from datetime import datetime

class GenAIDataGovernance:
    def __init__(self):
        self.data_registry = {}  # Stores metadata about the data
        self.audit_trail = []  # Logs all data access and operations

    def log_audit(self, action, details):
        """Log an action to the audit trail with a timestamp."""
        self.audit_trail.append({'timestamp': datetime.now().isoformat(), 'action': action, 'details': details})

    def register_data(self, data_id, user_consent, data_description):
        """Register new data with its metadata and consent status."""
        if user_consent:
            self.data_registry[data_id] = {
                'consent': user_consent,
                'description': data_description,
                'registered_on': datetime.now().isoformat()
            }
            self.log_audit('register_data', f'Data ID {data_id} registered.')
        else:
            print(f"Data ID {data_id} registration failed due to lack of user consent.")

    def anonymize_data(self, data):
        """Anonymize data using a simple hash function (for demonstration purposes)."""
        anonymized_data = hashlib.sha256(data.encode()).hexdigest()
        self.log_audit('anonymize_data', 'Data anonymized.')
        return anonymized_data

    def check_consent_and_access(self, data_id):
        """Check if there's consent for the data and log access."""
        if data_id in self.data_registry and self.data_registry[data_id]['consent']:
            self.log_audit('access_data', f'Accessed Data ID {data_id}.')
            return True
        else:
            self.log_audit('access_denied', f'Access denied for Data ID {data_id}.')
            return False

    def generate_audit_report(self):
        """Generate a report of the audit trail."""
        report = json.dumps(self.audit_trail, indent=4)
        print("Audit Trail Report:")
        print(report)

# Example usage
if __name__ == "__main__":
    governance = GenAIDataGovernance()
    governance.register_data('data123', True, 'Sample data for GenAI model training')
    if governance.check_consent_and_access('data123'):
        anonymized_data = governance.anonymize_data('Sensitive user data example')
        print(f"Anonymized data: {anonymized_data}")
    governance.generate_audit_report()
