import traceback as tbmodule

current_describe = None

class describe(object):
    def __init__(self, description):    
        self.description = description
        self.errors = []
        self.results = []

    def add_success(self):
        self.results.append('.')

    def add_error(self, type, value, traceback, should):
        self.errors.append((type, value, traceback, should))
        self.results.append('F' if type is AssertionError else 'E')

    def __enter__(self):
        global current_describe
        current_describe = self
    
    def __exit__(self, type, value, traceback):
        print "".join(self.results)
        for type, value, traceback, should in self.errors:
            print "===================================="
            print "it %s; instead:" %should
            print "===================================="
            tbmodule.print_exception(type, value, traceback)
            print "===================================="

class it(object):
    def __init__(self, should):
        self.should = should

    def __enter__(self):
        pass
    
    def __exit__(self, type, value, traceback):
        if type is None:
            current_describe.add_success()
        else:
            current_describe.add_error(type, value, traceback, self.should)
        return True

