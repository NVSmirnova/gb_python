#https://stackoverflow.com/questions/21598872/how-to-create-multiple-class-objects-with-a-loop-in-python
#1
objs = [MyClass() for i in range(10)]
for obj in objs:
    other_object.add(obj)

objs[0].do_sth()


#2
class MyClass:
    def __init__(self, name):
        self.name = name
        self.pretty_print_name()

    def pretty_print_name(self):
    print("This object's name is {}.".format(self.name))

my_objects = {}
for i in range(1,11):
    name = 'obj_{}'.format(i)
    my_objects[name] = my_objects.get(name, MyClass(name = name))