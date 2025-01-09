import inspect

def introspection_info(obj):
	data_obj={}
	data_obj['type']=type(obj)
	data_obj['attributes']=dir(obj)
	data_obj['module']=inspect.getmodule(obj)
	data_obj['ismodule']=inspect.ismodule(obj)
	data_obj['isclass']=inspect.isclass(obj)
	data_obj['isfunction']=inspect.isfunction(obj)
	data_obj['ismethod']=inspect.ismethod(obj)
	data_obj['isgenerator']=inspect.isgenerator(obj)
	for data in data_obj:
		return data_obj

gen=(x*2 for x in range(20))

number_info = introspection_info(gen)
print(number_info)
