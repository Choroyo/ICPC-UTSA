#Bryan Chora 11/26/2024 Kattis: Proofs
"""
This program will check if A line of the proof is valid if and only
if all assumptions were conclusions of previous lines. Sometimes the
students derive a conclusion more than once just to be extra sure it
is true, and that is perfectly all right!  
"""


#Number of line in the proof"
n = int(input())

incorrect = False

# intilize a set of conclusions
conclusions = set()

for i in range(1, n + 1):
    
    #proof line
    line = input()

    # if there is only conclusion
    if line[:2] == "->":
        
        conclusion = [part.strip() for part in line.split("->") if part.strip()]
        #Add the conclusion in a set of conclusions
        conclusions.update(conclusion)
    else:
        
        #If there is assumptions and conclusion
        partition = line.split("->")
        assumptions = partition[0].split()
        
        #for each assumtion in assumtions
        for assumption in assumptions:
            #if assumptions not in conclusion
            if assumption not in conclusions and not incorrect:
                # print the first number line incorrect
                numLine = i
                # flag to check if the proof is incorrect
                incorrect = True
        conclusion = [part.strip() for part in partition[1].split("->") if part.strip()]
        conclusions.update(conclusion)
if incorrect:
    print(numLine)
else:
    print("correct")
