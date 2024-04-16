from patient_record import PatientRecord
from authentication import authenticate_user, load_credentials
from user import User

def main():
    print("Welcome to the Hospital Data Management System")
    credentials_file = input("Enter the path to the credentials file: ")
    patients_file = input("Enter the path to the patient data file: ")
    credentials = load_credentials(credentials_file)

    username = input("Enter username: ")
    password = input("Enter password: ")
    user = authenticate_user(credentials_file, username, password)

    if user is None:
        print("Invalid credentials. Access denied.")
        return

    patient_records = PatientRecord(patients_file)

    while True:
        if user.role in ['admin', 'management']:
            if user.role == 'admin':
                print("\nAdmin access: Can only count visits.")
                print("1. Count visits")
                print("2. Logout")
                choice = input("Enter your choice (1 or 2): ")
                if choice == "1":
                    date = input("Enter the date for visit count (YYYY-MM-DD): ")
                    patient_records.count_visits(date)
                elif choice == "2":
                    print("Logging out...")
                    break
                else:
                    print("Invalid choice. Please choose a valid action.")
            elif user.role == 'management':
                print("\nManagement access: Generating key statistics...")
                patient_records.generate_statistics()
                print("1. Generate more statistics")
                print("2. Logout")
                choice = input("Enter your choice (1 or 2): ")
                if choice == "2":
                    print("Logging out...")
                    break
                elif choice != "1":
                    print("Invalid choice. Please choose a valid action.")

        elif user.role in ['nurse', 'clinician']:
            print("\nChoose an action:")
            print("1. Add_patient")
            print("2. Remove_patient")
            print("3. Retrieve_patient")
            print("4. Count_visits")
            print("5. Logout")
            choice = input("Enter your choice: ")

            if choice == "1":
                patient_information = {}
                print("Enter patient details:")
                patient_information['Patient_ID'] = input("Enter Patient_ID: ")
                patient_information['Visit_time'] = input("Enter Visit_time (YYYY-MM-DD): ")
                patient_information['Visit_department'] = input("Enter Visit_department: ")
                patient_information['Race'] = input("Enter Race: ")
                patient_information['Gender'] = input("Enter Gender: ")
                patient_information['Ethnicity'] = input("Enter Ethnicity: ")
                patient_information['Age'] = input("Enter Age: ")
                patient_information['Zip_code'] = input("Enter Zip_code: ")
                patient_information['Insurance'] = input("Enter Insurance: ")
                patient_information['Chief_complaint'] = input("Enter Chief_complaint: ")
                patient_information['Note_ID'] = input("Enter Note_ID: ")
                patient_information['Note_type'] = input("Enter Note_type: ")

                patient_records.add_patient_record(patient_information)
            elif choice == "2":
                patient_id = input("Enter Patient_ID: ")
                patient_records.delete_patient_record(patient_id)
            elif choice == "3":
                patient_id = input("Enter Patient_ID: ")
                visits = patient_records.retrieve_visit(patient_id)
                for index, visit in visits.iterrows():
                    print(visit.to_string())
            elif choice == "4":
                date = input("Enter the date (YYYY-MM-DD): ")
                patient_records.count_visits(date)
            elif choice == "5":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please choose a valid action.")
        else:
            print("Unauthorized role.")
            break

if __name__ == "__main__":
    main()
