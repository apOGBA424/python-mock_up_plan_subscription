
cost = [ 500,'1,500','5,000','15,000']
description = 'N'
header ='\nsubscription plan'.upper()

print(header)

for unit_cost in cost:
	print(description + str(unit_cost))

print('-'*36,'\n')



bundle = {
'daily' : '500',
'weekly' : '1,500',
'monthly' : '5,000 (MOST POPULAR)',
'yearly' : '50,000'
}
for x in bundle:
	 print(str(x).title()+ ' plan  N'+str(bundle[x]))
