from ps3b import ResistantVirus
virus = ResistantVirus(1.0, 0.0, {'drug1':True}, 0.0)
for i in range(100):
  virus.reproduce(0,[])
  raw_input()

print virus.getResistances()
