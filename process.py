import os
import time
import psutil
import urllib.request
import smtplib
import schedule
from sys import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


def is_connected():
    try:
        urllib.request.urlopen('http://216.58.192.142',timeout=1)
        return True
    except urllib.request.URLError as err:
        return False
    
def MailSender(filename,time):
    try:
        fromaddr="vaishnavitalekar0811@gmail.com"
        toaddr="vaishnavitalekar293@gmail.com"

        msg=MIMEMultipart()

        msg['From']=fromaddr

        msg['to']=toaddr

        body="""
        Hello %s
        Welcome Here.
        Please find attached document which contains log of Running process.
        Log File is created at %s

        This is Auto Generated Mail

        Thanks & Regards,
        Vaishnavi Pravin Talekar.
        """ %(toaddr,time)

        Subject="""
            The log Generated at : %s"""%(time)

        msg['Subject']=Subject

        msg.attach(MIMEText(body,'plain'))

        attachment=open(filename,"rb")

        p=MIMEBase('application','octet-stream')

        p.set_payload((attachment).read())

        encoders.encode_base64(p)

        p.add_header('Content-Disposition',"attachemnet;filename=%s"%filename)

        msg.attach(p)

        s=smtplib.SMTP('smtp.gmail.com',587)

        s.starttls()

        s.login(fromaddr, "vaishnavitalekar0811@gmail.com")

        text=msg.as_string()

        s.sendmail(fromaddr,toaddr,text)

        s.quit()

        print("Log file succuessfully send through mail")

    except Exception as E:
        print("Unable to send mail.",E)

def ProcessLog(log_dir='marvellous'):
    listprocess=[]

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator="-"*80
    log_path=os.path.join(log_dir,"marvellousLog%s.log"%(time.ctime()))

    f=open(log_path,'w')
    f.write(separator+"\n")
    f.write("Process Logger : "+time.ctime()+"\n")
    f.write(separator+"\n")
    f.write("\n")

    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','username'])
            vms=proc.memory_info.vms/(1024*1024)
            pinfo['vms']=vms

            listprocess.append(pinfo)
        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n"%element)

    print("Log File is Successfully Generated at Location %s"%(log_path))

    connected=is_connected()

    if connected:
        startTime=time.time()
        MailSender(log_path,time.ctime())
        endTime=time.time()

        print('Took %s seconds to send mail'%(endTime-startTime))

    else:
        print("There is NO internet Connection")    

def main():
    print("--Vaishnavi_Pravin_Talekar--")
    print("Application Name : "+argv[0])

    if(len(argv)!=2):
        print("Error : Invalid Number of Arguments")
        exit()

    try:
        schedule.every(int(argv[1])).minutes.do(ProcessLog)
        while True:
            schedule.run_pending()
            time.sleep(1)
    except ValueError:
        print("Error : Invalid datatype of input")
    except Exception as E:
        print("Error : Invalid Input",E)

if __name__=="__main__":
    main()
