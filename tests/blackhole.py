__author__ = 'reggie'

###START-CONF
##{
##"object_name": "blackhole",
##"object_poi": "my-blackhole-1234",
##"auto-load" : true,
##"parameters": [ {
##                  "name": "name",
##                  "description": "name to greet",
##                  "required": true,
##                  "type": "X",
##                  "state" : "{(.)+S$}"
##              } ],
##"return": [
##              {
##                  "name": "greeting",
##                  "description": "a greeting",
##                  "required": true,
##                  "type": "X",
##                  "state" : "5THDIMENSION"
##               }
##
##          ] }
##END-CONF




from pumpkin import *

class blackhole(PmkSeed.Seed):

    def __init__(self, context, poi=None):
        PmkSeed.Seed.__init__(self, context,poi)
        pass


    def run(self, pkt, data):

        name = str(data[0])
        stag = self.get_last_stag(pkt)
        print name+" "+stag+" lost in blackhole"
        pass
