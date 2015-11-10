import rdflib

g = rdflib.Graph();
g.parse("AngryBird.ttl",format="turtle")

i = 0
for s,p,o in g:
    i += 1
    print s,p,o

print 'there are ' + str(i) + ' triples.'