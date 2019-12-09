#

#
# from example import  *
# pp=add.delay(38888,4)
#
# print(pp)

from mycelery.tasks import *
add.delay(38888,4)
mul.delay(38888,4)
xsum.delay([38888,4,555555])
