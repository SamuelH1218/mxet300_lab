import L1_log
import time
import L1_lidar
import L2_vector
import numpy

while(1):
    C = L2_vector.getNearest()
    L1_log.tmpFile(C[0],"dist.txt")
    L1_log.tmpFile(C[1],"degrees.txt")

    x = numpy.cos(numpy.radians(C[1]))* C[0]
    y = numpy.sin(numpy.radians(C[1]))* C[0]
    print(C[0])
    print(C[1])
    L1_log.tmpFile(x,"xcord.txt")
    L1_log.tmpFile(y,"ycord.txt")
    time.sleep(.1)