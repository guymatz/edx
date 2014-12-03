# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics 

import numpy
import random
import pylab
from ps3b_precompiled_27 import *

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 2
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """

        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self.clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """

        r = random.random()
        if random.random() < self.getClearProb():
            #print("TRUE: r = %f, clearProb = %f" % (r, self.getClearProb()))
            return True
        else:
            #print("FALSE: r = %f, clearProb = %f" % (r, self.getClearProb()))
            return False

    
    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """

        #random.seed(0)
        r = random.random()
        w = self.getMaxBirthProb() * (1 - popDensity)
        if r < w:
#            #print("New virus: %f < %f" % (r,w))
            return SimpleVirus(
                                  self.getMaxBirthProb(),
                                  self.getClearProb()
                                )
        else:
            raise NoChildException



class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """

        self.viruses = viruses
        self.maxPop = maxPop

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        return self.viruses


    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self.maxPop


    def getTotalPop(self):
        """
        Gets the size of the current total virus population. 
        returns: The total virus population (an integer)
        """
        return len(self.viruses)


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        
        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """

        original_pop_size = self.getTotalPop()
        uncleared_viruses = []
        for v_index in range(self.getTotalPop()):
            if not self.viruses[v_index].doesClear():
                uncleared_viruses.append(self.viruses[v_index])
        self.viruses = uncleared_viruses

        for v in self.getViruses():
            try:
                pop_density = self.getTotalPop() / float(self.getMaxPop())
                #print("pop_density = %02f" % pop_density)
                self.viruses.append(v.reproduce(pop_density))
            except NoChildException, e:
                pass

        return self.getTotalPop()



#
# PROBLEM 3
#
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """

    steps = 300
    trial_outcomes = []
    for t in range(numTrials):
        trial_outcomes.append( [] )
        viruses = [ SimpleVirus(maxBirthProb, clearProb) for x in
                      range(numViruses) ]
        #print("Starting with %i viruses attacking" % len(viruses))
        P = Patient(viruses, maxPop)
        for update in range(steps):
            P.update()
            #print("%i viruses left" % P.getTotalPop())
            trial_outcomes[t].append(P.getTotalPop())

    #print trial_outcomes

    # Is there a list comprehension way to do this?
    # trial_outcome_avgerages =
    # [ a[y][x] for x in range(len(a[0])) for y in range(len(a)) ]
    total_per_trial = []
    for col in range(len(trial_outcomes[0])):
        total_per_trial.append(0)
        for row in range(len(trial_outcomes)):
            total_per_trial[col] += trial_outcomes[row][col]
    avg_per_step = [ x/float(numTrials) for x in total_per_trial ]

    #print avg_per_step

    pylab.figure(1)
    pylab.title("SimpleVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend()
    pylab.plot(avg_per_step)
    pylab.show()


#simulationWithoutDrug(100, 1000, .1, .05, 30)
#simulationWithoutDrug(1, 10, 1.0, 0.0, 1)
#simulationWithoutDrug(100, 200, 0.2, 0.8, 1)

#
# PROBLEM 4
#
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """   

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb
    
    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        viruses = self.resistances
        return { k:viruses[k] for k in viruses.keys() if viruses[k] }

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        return self.mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.       

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        
        return drug in self.resistances and self.resistances[drug] == True
        
    def reproduce(self, popDensity, activeDrugs):
        for drug in activeDrugs:
            if not self.isResistantTo(drug):
                return

        new_resistances = {}
        # reproduction chance based on density, etc.
        r = random.random()
        #print("random num = %f" % r)
        if r < self.maxBirthProb * (1 - popDensity):
            #print("Reproducing . . ")
            for drug,resistant in self.resistances.iteritems():
                if resistant:
                    #print("Resistant drug %s . . " % drug)
                    if random.random() > (1-self.mutProb):
                        new_resistances[drug] = False
                        #print(". . . is no longer resistant")
                    else:
                        #print(". . . is STILL resistant")
                        new_resistances[drug] = True
                else:
                    #print("NON-Resistant drug %s . . " % drug)
                    if random.random() > self.mutProb:
                        #print(". . . is NOW resistant")
                        new_resistances[drug] = False
                    else:
                        #print(". . . is still NON-resistant")
                        new_resistances[drug] = True
        #print("new_resistances : %s" % new_resistances)
        return type(self)(self.maxBirthProb, self.clearProb, new_resistances, self.mutProb)
        
class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        Patient.__init__(self, viruses, maxPop) 
        self.administered_drugs = []
        
    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """

        if newDrug not in self.getPrescriptions():
            self.administered_drugs.append(newDrug)


    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """

        return self.administered_drugs
        
    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.       

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        # drugResist is a list of drugs,
        # e.g. [ 'srinol','guttagonol' ]
        #return [ k for k,v in drugResist.iteritems() if v ]
        total_resistant_population_count = 0
        for virus in self.getViruses():
            resistant_population_count = 0
            for drug in drugResist:
                if virus.isResistantTo(drug):
                    resistant_population_count += 1
            if resistant_population_count == len(drugResist):
                total_resistant_population_count += 1
        return total_resistant_population_count
        
    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """

        original_pop_size = self.getTotalPop()
        uncleared_viruses = []
        #print("Original Pop. Size = %i" % original_pop_size)
        for v_index in range(self.getTotalPop()):
            if not self.viruses[v_index].doesClear():
                #print("Appending Uncleared virus #%i, %s" % (v_index, self.viruses[v_index]))
                uncleared_viruses.append(self.viruses[v_index])
        self.viruses = uncleared_viruses
        #print("Uncleared Pop. Size = %i" % len(self.viruses))
        
        pop_density = self.getTotalPop() / float(self.getMaxPop())
        new_viruses = []
        for v in self.getViruses():
            try:
                children = v.reproduce(pop_density, self.getPrescriptions())
                #print("New Children = %s" % children)
                if children:
                    new_viruses.append(children)
            except NoChildException, e:
                pass

        self.viruses = new_viruses + uncleared_viruses
        #self.viruses = current_viruses
        #print("Updating Pop. Size = %i" % len(self.viruses))
        return self.getTotalPop()



#
# PROBLEM 5
#
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """

    # TODO
