def decorator(any_function, *args, **kwargs):
    def modified_function(*args, **kwargs):
        print('-----------')

        kwargs['z'] += 10 # <-- Access the argument option 1
        # kwargs['i'] = 'this_will_not_work'

        kwargs.update({'z': 12}) # <-- CHanging value using tuple update
        any_function(*args, **kwargs)
        print(f'args => {args} kwargs => {kwargs}')
        print('___________')

    return modified_function

@decorator
def normal_function(x, z=23):
    z += 1 # <-- this doesn't change or update the value
    print('INSIDE NORMAL FUNCTION')
    return z

normal_function(5, z=32)