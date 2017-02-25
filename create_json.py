import xml.etree.cElementTree as ET
import json
from audit import audit_post,audit_name
path = "mumbai_india.osm"


rc=0
wc=0
tagk={}
elemtag={}
nodefile=open("mumbai_india.osm.json","a")
with open(path,'rb') as f:
	for __,elem in ET.iterparse(f,events=("start",)):
		en=elem.tag
		node={}
		if en=='node' or en ==  'way':
			node['id']=elem.attrib['id']
			node['type']=en
			node['created']={
			"changeset": elem.attrib['changeset'], 
            "user": elem.attrib['user'], 
            "version": elem.attrib['version'], 
            "uid": elem.attrib['uid'], 
            "timestamp": elem.attrib['timestamp']
			}
			address={}
			for tg in elem:
				if tg.tag=='tag':
					k=tg.get('k')
					p=tg.get('v')
					if len(k)>5 and k[:5]=='addr:':
						if k[5:]=="postcode":
							p=audit_post(p)
							if p != None:
								address[k[5:]]=p
						else:
							address[k[5:]]=audit_name(p)
					elif k[:5]=='name:':
						pass
					elif k=='name':
						node[k]=audit_name(p)
					else:
						if k=="postal_code":
							p=audit_post(p)
							if p != None:
								node[k]=p
						else:
							node[k]=audit_name(p)
			if len(address.keys())!=0:
				node['address']=address
			if en == 'node':
				node['pos']=[float(elem.attrib['lat']),float(elem.attrib['lon'])]
			if en=='way':
				ref=[]
				for nd in elem:
					if nd.tag=='nd':
						ref.append(nd.attrib['ref'])
				node['nd']=ref
			nodefile.write(json.dumps(node)+"\n")
		elem.clear()
nodefile.close()
		