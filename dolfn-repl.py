#############################################################################
#  This is a basic interpreter for my programming language known as dolfn.  # 
#  This interpreter can be used for bootstrapping a (much) more efficient   #
#  compiler or to test out small programs. Use it well and have fun!        #
#############################################################################

# The basic idea of this is:
# getline -> basic_parse -> str_parse -> macro_expand -> str_parse -> feed <-> run


global dicti, stak, macros
dicti  = {}     # a dictionary of commands and their instructions, both primative and user-defined
macros = {}     # a dictionary of macros and their expanded forms, both primative and user-defined
stak   = []     # a stack to help with evaluation of a program

def getline(prompt='dolfn #> '):
    return input(prompt)

def basic_parse(npt):
    collector, retlist, npt = '', [], npt.lstrip() + ' '
    while len(npt) > 0:
        if not npt[0].isspace():
            collector = collector + npt[0]
            npt = npt[1:]
        else:
            retlist.append(collector)
            collector, npt = '', npt.lstrip()
    return retlist

print( basic_parse(getline()) )

