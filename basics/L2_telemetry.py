import L1_ina
import L1_log
import time

if __name__ == "__main__":
    while(1):
        y = L1_ina.readVolts()
        L1_log.tmpFile(y,"thedata.txt")
        time.sleep(1)
