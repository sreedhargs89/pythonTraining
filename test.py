## Zip the list
emplst = ["arun", "ravi", "hari"]
deplst = ["sales","mkt","fin"]
country = ["India", "Pakistan", "Bangladesh"]
for name,dept,place in zip(emplst,deplst,country):
	print ("%s works for %s dept in %s "%(name, dept, place))


a,b,c = [1,2,3], (4,5),60
