# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    additional_steps = 150
    initial_steps = [ 300, 150, 75, 0 ]
    viruses = [ ResistantVirus(0.1,0.05,{'guttagonol':False},0.005)
                        for x in range(1000) ]

    for n in range(len(initial_steps)):
        cured = 0
        v_left = []
        for t in range(numTrials):
            patient = TreatedPatient(viruses, 1000)
            #print("INitial steps: %i" % initial_steps[n])
            #print patient.getTotalPop()
            for s1 in range(initial_steps[n]):
                patient.update()
            patient.addPrescription('guttagonol')
            #print patient.getTotalPop()
            for s2 in range(additional_steps):
                patient.update()
    
            if patient.getTotalPop() <= 50:
                print("%i cured" % cured)
                cured += 1
            v_left.append(patient.getTotalPop())
        print("Cure rate for %i + %i = %f" % (initial_steps[n], additional_steps,cured/float(numTrials)))
        pylab.subplot(2,1,n)
        pylab.hist(v_left)
        pylab.title("Initial Steps = %i" % initial_steps[n])
    #pylab.show()
        

        

#simulationDelayedTreatment(100)


#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    resistances = { 'guttagonol':False, 'grimpex': False }
    viruses = [ ResistantVirus(0.1,0.05, resistances, 0.005)
                        for x in range(100) ]

    set_steps = 150
    variable_steps = [ 300, 150, 75, 0 ]

    f, axarr = pylab.subplots(4)
    for n in range(len(variable_steps)):
        v_left = []
        cured = 0
        for t in range(numTrials):
            patient = TreatedPatient(viruses, 1000)
            #print("INitial steps: %i" % initial_steps[n])
            #print patient.getTotalPop()
            for s in range(set_steps):
                patient.update()
            patient.addPrescription('guttagonol')
            for s in range(variable_steps[n]):
                patient.update()
            #print patient.getTotalPop()
            patient.addPrescription('grimpex')
            for s2 in range(set_steps):
                patient.update()
    
            if patient.getTotalPop() <= 50:
                print("%i cured" % cured)
                cured += 1
            v_left.append(patient.getTotalPop())
        print("Cure rate for %i + %i = %f" % (variable_steps[n], set_steps,cured/float(numTrials)))
        print("Variance for %i = %f" % (variable_steps[n], numpy.var(v_left)))
        axarr[n].hist(v_left, 50)
        #axarr[n].title("Variable Steps = %i", variable_steps[n])
    pylab.show()
 
simulationTwoDrugsDelayedTreatment(100)
