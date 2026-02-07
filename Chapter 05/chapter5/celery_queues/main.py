from tasks import send_email, process_data, backup_database

if __name__ == "__main__":
    print("Starting tasks...")
    send_email.delay("user@example.com", "Welcome!", "Thanks for registration")
    send_email.delay("admin@example.com", "Alarm", "Critical problem found")
    process_data.delay("dataset_1")
    process_data.delay("dataset_2")
    backup_database.delay()
    print("Tasks sent")
