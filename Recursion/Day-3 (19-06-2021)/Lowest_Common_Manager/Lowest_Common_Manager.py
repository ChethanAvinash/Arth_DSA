class Node:
    def __init__(self,node,directReports):
        self.node = node
        self.directReports = directReports

def getLowestCommonManager(manager,reportOne,reportTwo):
    
    # initially we don't have any of the reports
    no_of_reports_found = 0
    
    # Next we check the directReports of the current manager
    for report in manager.directReports:
        # then we find the reports of each of the reports of the current manager
        lowestCommonManager,reportsFound = getLowestCommonManager(report,reportOne,reportTwo)
        if lowestCommonManager:
            return lowestCommonManager,reportsFound
        no_of_reports_found+=reportsFound
    
    if manager.node==reportOne or manager.node==reportTwo:
        no_of_reports_found+=1
    
    lowestCommonManager = manager if no_of_reports_found==2 else None
    
    return lowestCommonManager,no_of_reports_found
        
# Inputs
root = Node("A",[])
nextLevel_of_A = [Node("B",[]),Node("C",[])]
root.directReports+=nextLevel_of_A
nextLevel_of_B = [Node("D",[]),Node("E",[])]
root.directReports[0].directReports+=nextLevel_of_B
nextLevel_of_C = [Node("F",[]),Node("G",[])]
root.directReports[1].directReports+=nextLevel_of_C
nextLevel_of_D = [Node("H",[]),Node("I",[])]
root.directReports[0].directReports[0].directReports+=nextLevel_of_D

reportOne = "E"
reportTwo = "D"
print(getLowestCommonManager(root,reportOne,reportTwo)[0].node)


        