

resources = {"VPUS":4,"membery":2222,"gb":3124,"a":312321}

resource_query = ",".join(sorted("%s:%s" % (rc, amount)
                                      for (rc, amount) in resources.items()))
print type(resource_query)

poli = sorted("%s:%s" % (rc, amount)
                                      for (rc, amount) in resources.items())
print poli