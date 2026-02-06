import pandas as pd

patients = pd.DataFrame(
    {'patient_id': [1, 2, 3, 4, 5],
     'patient_name': ["Daniel", "Alice", "Bob", "George", "Alain"],
     'conditions': ["YFEV COUGH", None, "DIAB100 MYOP", "ACNE DIAB100", "DIAB201"]}
)


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
        return patients[patients["conditions"].str.startswith("DIAB1") | patients["conditions"].str.contains(" DIAB1", regex=False)]

result = find_patients(patients)
print(result)
