from dateutil.parser import parse;
import util;

class matcher:
    def __init__(self, name, matcherFunction):
        self.name = name;
        self.matcherFunction = matcherFunction;
    def matches(self, other):
        return self.matcherFunction(other);

someObject = matcher("some object", lambda x: x is not None);
someInt = matcher("some integer", lambda x: isinstance(x, int));
someDate = matcher("some date", lambda x: util.isDate(x));
someNumber = matcher("some number", lambda x: isinstance(x, (int, float, complex)));
optional = matcher("optional value", lambda x: True);

def some(keySet):
    return matcher("object matching {}".format(keySet),
        lambda matchedObject: keySet == matchedObject.keys);

def isMatcher(x):
    return isinstance(x, matcher);
