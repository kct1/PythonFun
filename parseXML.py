#!/usr/bin/python
# This program parses XML files using the DOM model 

import xml.dom.minidom

def eliminateText (node):
	return [x for x in node.childNodes if x. nodeType !=
			xml.dom.Node.TEXT_NODE]

def readInfo (tag, node):
	if node.nodeType != xml.dom.Node.ELEMENT_NODE:
		return None

	if node.tagName == 'string':
		return node.firstChild.data

	elif node.tagName == 'integer':
		return int(node.firstChild.data)

	elif node.tagName == 'data':
		return node.firstChild.data

	elif node.tagName == 'dict':
		return readKeys(removeText(node))
		return None

def readKeys (lst):
y=0
dict = { }
	while y < len(lst):
	if lst[y].nodeType == xml.dom.Node.ELEMENT_NODE and lst[y].tagName == 'key':
		tag = lst[y].firstChild.data
		y += 1
		dict[tag] = readInfo(tag, lst[y])
		y += 1
	    return dict

itunesDB = xml.dom.minidom.parse("iTunes Music Library.xml") 
topnodes = removeText(itunesDB.documentElement)
topdict = readKeys(removeText(topnodes[0]))
trackdict = topdict.get('Tracks', {})
for track in trackdict:
	song = trackdict.get(track) print
	song.get('Name',''),':',song.get('Artist',''),':',song.get('Year','')