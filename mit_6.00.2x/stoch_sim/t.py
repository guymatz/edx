from ps3b import SimpleVirus
from ps3b import Patient

viruses = [ SimpleVirus(0.75, 0.82),  SimpleVirus(0.83, 0.75) , SimpleVirus(0.31, 0.77), SimpleVirus(0.64, 0.76) ]
P1 = Patient(viruses, 7)

print P1.getTotalPop()

for n in range(10):
  P1.update()
  print("Virus population = %i" % P1.getTotalPop())
  print len(P1.viruses) < P1.getMaxPop() 
