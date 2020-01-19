import sys
import os.path

cache_fill_name = 'cache.csv'

text_in = sys.argv[1]
text_out = sys.argv[2]
lang_in = sys.argv[3]
lang_out = sys.argv[-1]
cache_fill_list = [text_in,text_out,lang_in,lang_out]

def update_fill(fill_name,translet_list):
	fill = open(fill_name, 'a')
	print(translet_list)
	string = ';'.join(translet_list)
	fill.write(string + '\n')
	fill.close()



if os.path.exists(cache_fill_name):
	print('Есть')
	update_fill(cache_fill_name,cache_fill_list)
else: f = open(cache_fill_name, 'w')