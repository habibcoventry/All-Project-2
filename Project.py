from ProgramSetup import *


class TrafficLight():
    def __init__(self,Location):
        self.Location = Location




        
#========================= Initialisation ============================

(RobotList,canvasMain,
canvasRobotInfo,RobotCordLabels,
RobotScoreLables,RobotObjectiveLines) = Initialise(2)

#============================== Main =================================

Running = True

while Running == True:
    for x in range (0,2): #So all actions within here are implimented for both Robots.
        
        if RobotList[x].HasObjective == False:
            RobotList[x].FindNewObjective()
            RobotList[x].HasObjective = True
    
        RobotList[x].FollowPath()
        
    UpdateHUD(RobotList,canvasMain,canvasRobotInfo,RobotCordLabels,RobotScoreLables,RobotObjectiveLines)
    canvasMain.update()
    time.sleep(0.01)
window.mainloop()
