#import library to do http requests:
import urllib2
 
#import easy to use xml parser called minidom:
from xml.dom.minidom import parseString
#all these imports are standard on most modern python implementations
 
#download the file:
file = urllib2.urlopen('http://api.s4u.se/all/Er3lpPms8511fTTm/xml/all/fname/Game.of.Thrones.S03E03.720p.HDTV.x264-EVOLVE')
#convert to string:
data = file.read()
#close file because we dont need it anymore:
file.close()
#parse the xml you downloaded
dom = parseString(data)
#retrieve the first xml tag (<tag>data</tag>) that the parser finds with name tagName:
try:
    xmlTag = dom.getElementsByTagName('download_zip')[0].toxml()
except:
    xmlTag = None

#strip off the tag (<tag>data</tag>  --->   data):
if xmlTag:
    xmlData = xmlTag.replace('<download_zip>','').replace('</download_zip>','')
    print xmlData
else:
    print "error"

#print out the xml tag and data in this format: <tag>data</tag>
#print xmlTag
#just print the data
