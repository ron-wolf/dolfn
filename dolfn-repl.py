#############################################################################
#  This is a basic interpreter for my programming language known as dolfn.  # 
#  This interpreter can be used for bootstrapping a (much) more efficient   #
#  compiler or to test out small programs. Use it well and have fun!        #
#############################################################################


global dicti, stak
dicti = {}
stak = []

def dolfn(npt):
    if npt in dicti:
        eval(dicti[npt])
    elif npt.is:
        stak.append()


## The REPL:
while True:
    dolfn(input('dolfn #> '))

'''
try:
    i = int(s)
except ValueError:
    i = 0
'''



