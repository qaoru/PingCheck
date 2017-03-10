import os
import subprocess
import time

trash=open(os.devnull, 'w')
report=open("PingCheck_report.txt", 'w')
hostname = str(input("Host to check ? (IPv4) : "))

text_result = ""
while True :
    ping_var = str(subprocess.Popen("ping %s" %hostname, stdout=subprocess.PIPE).stdout.read())
    now = int(time.time())

    if "TTL" in ping_var:
        text_result = "PingCheck : SUCCESS"
    else:
        text_result = "PingCheck : Fail\nLogs sent to PingCheck_report.txt"
        report.write(time.strftime("%d-%m-%Y | %X", time.localtime()) + '\t PingCheck failed (Hostname : %s)\n'%hostname)

    print(text_result)

    if (time.time() >= now + (600)) and ("SUCCESS" in text_result):
        print(time.strftime("%d-%m-%Y | %X", time.localtime()) + '\t 10min log sent to PingCheck_report.txt')
        report.write(time.strftime("%d-%m-%Y | %X", time.localtime()) + '\t 10 minutes of SUCCESS (Hostname : %s)\n'%hostname)
        now = time.time()

    time.sleep(3)
