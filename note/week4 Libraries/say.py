import cowsay
import sys
from saying import hello
from saying import bye

if len(sys.argv)==2 :
    #cowsay.trex("hello, "+sys.argv[1])
    hello(sys.argv[1])
    bye(sys.argv[1])

