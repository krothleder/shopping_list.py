
def already_exists(new_item,list):
	if(new_item.lower() in list):
		print "already exists"
	else:
		list.append(new_item)


def alf_order(list):
	return list.sort()


def remove(item,list):
	if (item.lower() in list):
		list.remove(item.lower())
		return alf_order(list)
	else:
		print "that item item is not in your list"

def main():
	list = ["apples", "oranges", "bananna's", "carrots"]
	remove("grapes",list)
	print list

if __name__ == '__main__':
	main()