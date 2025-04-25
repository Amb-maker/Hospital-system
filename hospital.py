class Patient:
    def __init__(self, patient_id, name, age, gender, contact_number):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.contact_number = contact_number
        self.appointments = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def view_appointments(self):
        if len(self.appointments) > 0:
            print(f"Appointments for {self.name}:")
            for appointment in self.appointments:
                print(f"Date: {appointment.date}, Doctor: {appointment.doctor_name}, Time: {appointment.time}")
        else:
            print(f"{self.name} has no appointments.")

class Appointment:
    def __init__(self, date, time, doctor_name):
        self.date = date
        self.time = time
        self.doctor_name = doctor_name

class Staff:
    def __init__(self, staff_id, name, role, contact_number):
        self.staff_id = staff_id
        self.name = name
        self.role = role
        self.contact_number = contact_number

class Hospital:
    def __init__(self):
        self.patients = []
        self.staff_members = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_staff(self, staff):
        self.staff_members.append(staff)

    def view_all_patients(self):
        if len(self.patients) > 0:
            print("Patients List:")
            for patient in self.patients:
                print(f"ID: {patient.patient_id}, Name: {patient.name}, Age: {patient.age}, Gender: {patient.gender}")
        else:
            print("No patients registered.")

    def view_all_staff(self):
        if len(self.staff_members) > 0:
            print("Staff List:")
            for staff in self.staff_members:
                print(f"ID: {staff.staff_id}, Name: {staff.name}, Role: {staff.role}, Contact: {staff.contact_number}")
        else:
            print("No staff members added.")

    def search_patient(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                print(f"Patient Found: {patient.name}, Age: {patient.age}, Gender: {patient.gender}")
                return patient
        print("Patient not found.")
        return None

    def schedule_appointment(self, patient_id, appointment):
        patient = self.search_patient(patient_id)
        if patient:
            patient.add_appointment(appointment)
            print(f"Appointment scheduled for {patient.name} on {appointment.date} at {appointment.time} with Dr. {appointment.doctor_name}")

# Main Program
def main():
    hospital = Hospital()

    # Adding some staff members
    doctor = Staff(1, "Dr. Smith", "Doctor", "555-1234")
    nurse = Staff(2, "Nurse Linda", "Nurse", "555-5678")
    hospital.add_staff(doctor)
    hospital.add_staff(nurse)

    # Adding a patient
    patient1 = Patient(1, "John Doe", 30, "Male", "555-1111")
    hospital.add_patient(patient1)

    # View all staff and patients
    hospital.view_all_staff()
    hospital.view_all_patients()

    # Scheduling an appointment for the patient
    appointment1 = Appointment("2025-04-30", "10:00 AM", "Dr. Smith")
    hospital.schedule_appointment(1, appointment1)

    # View patient appointments
    patient1.view_appointments()

if __name__ == "__main__":
    main()
