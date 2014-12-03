from ps3b import ResistantVirus
from ps3b import TreatedPatient

print "test: TreatedPatient 1"
virus = ResistantVirus(1.0, 0.0, {}, 0.0)
patient = TreatedPatient([virus], 100)
for i in range(10):
    patient.update()
print patient.getTotalPop() > 100

print "test: TreatedPatient 2"
virus = ResistantVirus(1.0, 1.0, {}, 0.0)
patient = TreatedPatient([virus], 100)
print("PRE: Total Pop = %i" % patient.getTotalPop())
for i in range(10):
    patient.update()
print("POST: Total Pop = %i" % patient.getTotalPop())
print patient.getTotalPop() > 100

print "test: TreatedPatient 5"
virus1 = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
virus2 = ResistantVirus(1.0, 0.0, {"drug1": False, "drug2": True}, 0.0)
virus3 = ResistantVirus(1.0, 0.0, {"drug1": True, "drug2": True}, 0.0)
patient = TreatedPatient([virus1, virus2, virus3], 100)
print patient.getResistPop(['drug1']) == 2
print patient.getResistPop(['drug2']) == 2
print patient.getResistPop(['drug1','drug2']) == 1
print patient.getResistPop(['drug3']) == 0
print patient.getResistPop(['drug1', 'drug3']) == 0
print patient.getResistPop(['drug1','drug2', 'drug3']) == 0

print "test: TreatedPatient 6"
virus1 = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
virus2 = ResistantVirus(1.0, 0.0, {"drug1": False}, 0.0)
patient = TreatedPatient([virus1, virus2], 1000000)
patient.addPrescription("drug1")
for i in range(5):
    patient.update()
r_count = 0
s_count = 0
for v in patient.getViruses():
    if v.isResistantTo('drug1'):
        r_count +=1
    else:
        s_count +=1
print r_count > 10 and s_count == 1
