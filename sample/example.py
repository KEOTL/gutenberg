from gutenberg.core import *;
from gutenberg.suite import *;
from gutenberg.matcher import *;

@Case
def MyEndpointTest():
    @Test
    def getClientInfoTest():
        when(Method.GET, "http://localhost:8080/client",
             {
                 "clientId" : 5
             }
        ).expect(Status.OK,
               {
                   "clientId" : 5,
                   "name" : "Paul Atreides",
                   "age" : someInt
               },
                 andNothingMore);
