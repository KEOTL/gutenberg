# Gutenberg : A simple end-to-end REST API testing framework
## Example Usage
```python

from gutenberg import *;
from test import *;

@Case
def MyEndpointTest():
  @Test
  def givenValidClient_whenGettingClientDetails_thenReturnCorrespondingClientInfo():
    when(Method.GET, "http://localhost:8080/client",
    {"clientId" : 5}
    ).expect(Status.OK,
    {
      "clientId" : 5,
      "name" : "Paul Atreides",
      "age" : 19
    });

```
