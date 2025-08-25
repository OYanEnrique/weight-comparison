# Weight comparison

print('---Weight Comparison---')

persons = []
temp_data = []
greater_weight = 0
lower_weight = 0

while True:
	
	temp_data.append(input('Name: '))
	temp_data.append(float(input('Weight: ')))
	
	if len(persons) == 0:
		greater_weight = lower_weight = temp_data[1]
	else:
		if greater_weight < temp_data[1]:
			greater_weight = temp_data[1]
		if lower_weight > temp_data[1]:
			lower_weight = temp_data[1]
	
	persons.append(temp_data[:])
	temp_data.clear()
	
	user_continue = input('Continue? [S/N]').strip().lower()[0]
	if user_continue == "n":
			print('\nUntil next time!\n')
			break
			
print(f'In total, you registered {len(persons)} people')
print(f'The greatest weight was {greater_weight}Kg. This weight is from', end = ' ')

for p in persons:
	if p[1] == greater_weight:
		print(f'[{p[0].capitalize()}]')
		
print(f'The lower weight was {lower_weight}Kg. This weight is from', end = ' ')

for p in persons:
	if p[1] == lower_weight:
		print(f'[{p[0].capitalize()}]')