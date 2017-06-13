states = {
  'Ohio': 'oh',
  'Illinois': 'il',
  'Michigan': 'mi',
  'Indiana': 'in',
}

states['Pennsylvania'] = 'pa'


for a, b in states.items():
    print "%s is abbreviated as %s" % (a, b.upper())
