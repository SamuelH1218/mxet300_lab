import L1_log
import time
import L2_kinematics
import L2_inverse_kinematics

while(1):
    C = L2_kinematics.getMotion()
    D = L2_inverse_kinematics.getPdTargets(C)
    L1_log.tmpFile(D[0],"PDL.txt")
    L1_log.tmpFile(D[1],"PDR.txt")
    L1_log.tmpFile(C[0],"xdot.txt")
    L1_log.tmpFile(C[1],"thetadot.txt")
    time.sleep(.5)