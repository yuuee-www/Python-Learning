patientAgeList = [2, 5, 92, 27, 73, 14, 58, 44, 67, 10]

for age in patientAgeList :
    age = age + 1
print("Patient ages are: ", patientAgeList)

for i in range(len(patientAgeList)):
    patientAgeList[i] = patientAgeList[i] + 1
print("Patient ages are: ", patientAgeList)
