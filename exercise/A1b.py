import rdflib
import codecs

g = rdflib.Graph()
g.parse("calvin.ttl.txt",format="turtle")
#g.parse("AngryBird.ttl", format="turtle")
unknown1 = rdflib.Namespace("http://www.tut.fi/example.org/")

def addIfUnseenRes(r,s):
  """Add s to r if so far unseen and of proper type (URIRef or BNode)"""
  if not (type(s) is rdflib.URIRef or type(s) is rdflib.BNode):
      return
  if not (s in r):
      r.append(s)

i = 0
r = []
for s, p, o in g:
    i += 1
    addIfUnseenRes(r, s)
    addIfUnseenRes(r, p)
    addIfUnseenRes(r, o)

g2 = rdflib.Graph()
for resource in r:
    # when there is any resouce did not have a rdf:type, assign a Blank Node.
    bn = rdflib.BNode()
    if len(list(g.objects(subject=resource, predicate=rdflib.namespace.RDF.type))) == 0:
        g.add((resource, rdflib.namespace.RDF.type, bn))

print 'there are ' + str(i) + ' triples, and ' + str(len(r)) + ' resources'
print(g.serialize(format="n3"))
#this dataset didn't have any resource which type is unknown.


# file = codecs.open("out.ttl", "w", "utf-8")
# file.write(g.serialize(format="turtle").decode('utf8'))
# file.close()