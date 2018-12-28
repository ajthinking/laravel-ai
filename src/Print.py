import os
import sys

# Glorious print with color and grouping
class Print(object):
    INFO = '\033[94m' # BLUE
    SUCCESS = '\033[92m' # GREEN
    WARNING = '\033[93m' # YELLOW
    FAIL = '\033[91m' # RED
    # end colorization with this
    ENDC = '\033[0m'

    def __init__(self):
        self.indentation_levels = 0
        self.active_color = self.ENDC
        pass

    def __call__(self, *args):
        return self.print(*args)

    def print(self, *args):
        if not len(args):
            raise Exception('Please pass at least one argument')

        # Calls the builtin print
        print(
                self.active_color,
                self.indentation() + str(args[0]),
                *args[1:],
                self.ENDC
        )
        self.active_color = self.ENDC
        return self

    def indentation(self):
        return " " * 4 * self.indentation_levels

    def warning(self, *args):
        self.active_color = self.WARNING
        self.print(*args)
        return self            

    def info(self, *args):
        self.active_color = self.INFO
        self.print(*args)
        return self 

    def fail(self, *args):
        self.active_color = self.FAIL
        self.print(*args)
        return self 

    def success(self, *args):
        self.active_color = self.SUCCESS
        self.print(*args)
        return self            

    def group(self):
        self.indentation_levels += 1
        return self        

    def ungroup(self):
        if self.indentation_levels > 0:
            self.indentation_levels += -1
        return self

    def reset(self):
        self.indentation_levels = 0
        return self

if __name__ == '__main__':

    # Demo of the class 
    printer = Print()
    printer.group().success("sure")
    printer.reset().warning('extensive testing', 3, "COOL")
