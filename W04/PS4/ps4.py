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
    delays = [0, 75, 150, 300]
    for i in range(len(delays)):
        print 'Running simulationDelayedTreatment for delay: ' + str(delays[i])
        pylab.subplot(2, 2, i+1)
        virus_population = run_treatment_helper(numTrials=numTrials, treatment=simulationDelayedTreatment_helper, delay=delays[i])
    
        pylab.hist(virus_population, bins = 10)

        pylab.xlim(0, 600)        
        xmin,xmax = pylab.xlim()
        ymin,ymax = pylab.ylim()   
        
        pylab.xlabel('Final Virus Population')
        pylab.ylabel('Number of Trials')
        pylab.text(xmin + (xmax-xmin)*0.02, (ymax-ymin)/2, 'Delay = ' + str(delays[i])) 
   
    pylab.show()
    
def simulationDelayedTreatment_helper(delay):
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False}
    mutProb = 0.005
    numStepsPostDrug = 150
    
    viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for v in range(numViruses)]
    patient = TreatedPatient(viruses, maxPop)
        
    for i in range(delay):
        patient.update()
            
    patient.addPrescription('guttagonol')   
    
    for i in range(numStepsPostDrug - 1):
        patient.update()

    return patient.update()

def run_treatment_helper(numTrials, treatment, delay):
    virusPopulations = [0] * numTrials

    for i in range(numTrials):
        virusPopulations[i] = treatment(delay)
    
    return virusPopulations


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
    delays = [0, 75, 150, 300]
    for i in range(len(delays)):
        print 'Running simulationTwoDrugsDelayedTreatment for delay: ' + str(delays[i])
        pylab.subplot(2, 2, i+1)
        virusPopulations = run_treatment_helper(numTrials=numTrials, treatment=simulationTwoDrugsDelayedTreatment_helper, delay=delays[i])
    
        pylab.hist(virusPopulations, bins = 10)

        pylab.xlim(0, 600)        
        xmin,xmax = pylab.xlim()
        ymin,ymax = pylab.ylim()   
        
        pylab.xlabel('Final Virus Population')
        pylab.ylabel('Numb Patients')
        pylab.text(xmin + (xmax-xmin)*0.02, (ymax-ymin)/2, 'Delay2 = ' + str(delays[i])) 
   
    pylab.show()

def simulationTwoDrugsDelayedTreatment_helper(delay):
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005
    numStepsPreFirstDrug = 150
    numStepsPostDrug = 150
    
    viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for v in range(numViruses)]
    patient = TreatedPatient(viruses, maxPop)
        
    for i in range(numStepsPreFirstDrug):
        patient.update()
                
    patient.addPrescription('guttagonol')   
    
    for i in range(delay):
        patient.update()
    
    patient.addPrescription('grimpex') 
            
    for i in range(numStepsPostDrug - 1):
        patient.update()

    return patient.update()

simulationTwoDrugsDelayedTreatment(200)
    