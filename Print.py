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
        self.indentation = 0
        pass

    def __call__(self, message):
        return self.print(message)

    def indent(self, message):
        return " " * 4 * self.indentation + message

    def print(self, message):
        print(self.indent(message))
        return self

    def warning(self, message):
        print(self.WARNING + self.indent(message)  + self.ENDC)
        return self            

    def info(self, message):
        print(self.INFO + self.indent(message) + self.ENDC)
        return self

    def fail(self, message):
        print(self.FAIL + self.indent(message) + self.ENDC)
        return self

    def success(self, message):
        print(self.SUCCESS + self.indent(message) + self.ENDC)
        return self            

    def group(self):
        self.indentation += 1
        return self        

    def ungroup(self):
        if self.indentation > 0:
            self.indentation += -1
        return self

    def reset(self):
        self.indentation = 0
        return self


if __name__ == '__main__':

    # Demo of the class 
    printer = Print()
    #printer.info("laravel/laravel").group().success("User.php").success("Password_resets.php").warning(".gitignore").fail("Could not open file X")
    #printer.reset().info('laravel/valet')
    printer("yeah")
