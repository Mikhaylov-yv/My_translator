import sys
import os.path
import re

cache_fill_name = '/home/mikhaylov_yv/Programming/My_translator/cache.csv'
csv_delimiter = ','
# print(sys.argv)
for arg in range(len(sys.argv)):
	reg = re.compile('[,]')
	sys.argv[arg] = reg.sub('', str(sys.argv[arg]))

delimiter1 = sys.argv.index(';')
# print(delimiter1)
text_in = ' '.join(sys.argv[1:delimiter1])
delimiter2 = sys.argv.index(';',delimiter1+1)
delimiter3 = -3
if len(sys.argv[delimiter3-1]) >= 32:
	delimiter3 = delimiter3 -1

def clear_text(text):
	text = re.sub('\s\w{20}\w*\s',' ', text)
	return text

text_out = ' '.join(sys.argv[delimiter2+1:delimiter3])
print(text_in + ';')
lang_in = sys.argv[delimiter1+1]
lang_out = sys.argv[-1]
text_out = clear_text(text_out)
print(text_out)
cache_fill_list = [text_in,text_out,lang_in,lang_out]

def update_fill(fill_name,translet_list):
	fill = open(fill_name, 'a')
	# print(translet_list)
	string = csv_delimiter.join(translet_list)
	fill.write(string + '\n')
	fill.close()



if os.path.exists(cache_fill_name):
	update_fill(cache_fill_name,cache_fill_list)
else: f = open(cache_fill_name, 'w')
