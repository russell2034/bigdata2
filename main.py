from  sodapy import Socrata
import argparse
import os
import json
# take environmental  argument from the CLI
APP_KEY = os.environ['APP_KEY']
#  connect to  our  source
if __name__ == '__main__':
	# define parser to pass arguments for our function
	parser = argparse.ArgumentParser(description='Retrieving OCPV Data')
	parser.add_argument('--page_size',type = int, help = "Size of a page" )
	parser.add_argument('--num_pages', type = int, default= -1, help = 'Number of Pages')
	parser.add_argument('--output', type = str, default= 'print', help = 'Use only if you want to write in file. 4 print - leave out')
	args = parser.parse_args()
	client = Socrata('data.cityofnewyork.us', APP_KEY)

#get data
	if args.num_pages== -1:
		nump=client.get('nc67-uf89',SELECT='COUNT(*)')/args.page_size
		for i in range(nump):
			data = client.get('nc67-uf89',limit = args.page_size, offset=i*args.page_size)
	else:
		with open(args.output, 'a') as newfile:			
			for i in range(args.num_pages):
				data = client.get('nc67-uf89',limit = args.page_size, offset=i*args.page_size)
				if args.output =='print':
					for m in data:
						print(m,'\n')
			
				else:
					try:
						for m in data:
							newfile.write(json.dumps(m)+'\n')
				
					except:
						if args.output =='':
							print('Please specify your output')

		

		
#output logic 


