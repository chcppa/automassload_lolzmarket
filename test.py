# Fill accs.txt not valid strings
accs_txt = open('accs.txt', 'r+')

for i in range(200):
	accs_txt.write(f'test:{i}'+'\n')
