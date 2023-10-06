import PatientClass as P
import ProcedureClass as R

def main():
    patient = P.Patient(1, "Matt Jones", "123 Main st, Waco TX 76706", 
                        "254-555-7415", True)
    
    prod1 = R.Procedure("Physical Exam", "2/15/2022", "Dr. Irvine", 250, 1)
    prod2 = R.Procedure("MRI", "2/15/2022", "Dr. Hamilton", 1500, 1)
    prod3 = R.Procedure("CT Scan", "2/17/2022", "Dr. Drey", 1200, 2)
    prolist = [prod1, prod2, prod3]

    print("\n*** Patient Bill ***")
    print(f"Name: {patient.get_name()}")
    print(f"Address: {patient.get_address()}")
    print(f"Phone: {patient.get_phone()}")
    
    total = 0

    for p in prolist:
        if p.get_patientID() == 1:
            print(f"\nProcedure: {p.get_name_pro()}")
            print(f"Date: {p.get_date()}")
            print(f"Practitioner: {p.get_name_prac()}")
            print(f"Charge: ${p.get_charge()}")
            total += p.get_charge()
    
    if patient.get_veteran_status() == True:
        total = total * 0.6
    
    print("\nTotal Charges: $", format(total, ",.2f"))

main()


