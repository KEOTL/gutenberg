# Gutenberg : A simple end-to-end REST API testing framework

## Installation
```
pip3 install gutenberg-framework
```

## Example Usage
```python

from gutenberg.core import *;
from gutenberg.suite import *;
from gutenberg.matcher import *;

@Case
def MyEndpointTest():
  @Test
  def givenValidClient_whenGettingClientDetails_thenReturnCorrespondingClientInfo():
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

```
