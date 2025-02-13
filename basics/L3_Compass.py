import L2_compass_heading
import L1_log
import time

def CompassRetrieve():
    y = L2_compass_heading.get_heading()
    L1_log.tmpFile(y,"compassdata.txt")


def Cardinal():

    y = L2_compass_heading.get_heading()
    if((y<22.5) and (y > -22.5)):
        return "South"

    elif((y>22.5) and (y < 67.5)):
        return "South West"

    elif((y>67.5) and (y < 112.5)):
        return "West"

    elif((y>112.5) and (y < 157.5)):
        return "North West"

    elif((y<-22.5) and (y > -67.5)):
        return "South East"

    elif((y<-67.5) and (y > -112.5)):
        return "East"

    elif((y<-112.5) and (y > -157.5)):
        return "North East"

    else:
        return "North"
    





if __name__ == "__main__":
    while(1):
        CompassRetrieve()
        L1_log.stringTmpFile(Cardinal(),"CompassHeadingdata.txt")
        time.sleep(1)