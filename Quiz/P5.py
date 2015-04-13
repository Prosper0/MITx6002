import random
import pylab

#PROBLEM 5-1
def sampleQuizzes():
    '''
    returns: the probability of a student with final score between 70 and 75
    given the distrubution of the tests:
    Midterm1 between 50 and 80
    Midterm2 between 60 and 90
    FinalExam between 55 and 95
    with
    Midterm1 weighs 0.25    
    Midterm2 weighs 0.25
    FinalExam weighs 0.50
    '''
    num_trials = 10000
    num_score_70_75 = 0.0

    for i in range(num_trials):
        midterm1 = random.randint(50, 80)
        midterm2 = random.randint(60, 90)
        final_exam = random.randint(55, 95)
        total = (0.25 * midterm1) + (0.25 * midterm2) + (0.50 * final_exam)
        if (total >= 70) and (total <= 75):
            num_score_70_75 += 1

    return num_score_70_75 / num_trials

#PROBLEM 5-2
def generateScores(numTrials):
    """
    Runs numTrials trials of score-generation for each of
    three exams (Midterm 1, Midterm 2, and Final Exam).
    Generates uniformly distributed scores for each of 
    the three exams, then calculates the final score and
    appends it to a list of scores.
    
    Returns: A list of numTrials scores.
    """
    num_trial_scores = []

    for i in range(numTrials):
        midterm1 = random.randint(50, 80)
        midterm2 = random.randint(60, 90)
        final_exam = random.randint(55, 95)
        total = (0.25 * midterm1) + (0.25 * midterm2) + (0.50 * final_exam)
        num_trial_scores.append(total)

    return num_trial_scores

def plotQuizzes():
    scores = generateScores(10000)
    pylab.hist(scores,bins = 7)
    pylab.title('Distribution of Scores')
    pylab.xlabel('Final Score')
    pylab.ylabel('Number of Trials')
    pylab.show()

plotQuizzes()