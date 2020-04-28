from guerrillamail import GuerrillaMailSession
session = GuerrillaMailSession()
print(session.get_session_state()['email_address'])