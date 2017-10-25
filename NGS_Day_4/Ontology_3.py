#! /usr/bin/env python3

import six
import pronto
import sys

GO_GENES = sys.argv[1]
MY_GO_ID = sys.argv[2]

ont = pronto.Ontology('/Users/admin/pfb2017/NGS_Day_4/go.owl')

term_obj = ont[MY_GO_ID]
term_name = term_obj.name
print("These genes have all been annotated with", MY_GO_ID + ', "' + term_name + '" or any of tis child terms')

all_children = {}
all_children[MY_GO_ID] = term_name

for child in ont[MY_GO_ID].rchildren():
	all_children[child.id] = child.name
print(all_children)
