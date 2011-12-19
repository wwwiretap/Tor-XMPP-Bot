#!/usr/bin/python
#

import os.path
import gdata.data
import gdata.acl.data
import gdata.docs.client
import gdata.docs.data
import sys


class TorXMPPBot(object):
  APP_NAME = 'Tor XMPP Bot'
  DEBUG = False


def CreateClient():
  client = gdata.docs.client.DocsClient(source=TorXMPPBot.APP_NAME)
  client.http_client.debug = TorXMPPBot.DEBUG
  try:
     client.ClientLogin('torbot@redteam.io', 'vum-v0d7xaju', client.source)
  except gdata.client.BadAuthentication:
    exit('Invalid user credentials given.')
  except gdata.client.Error:
    exit('Login Error')
  return client


def PrintFeed(feed):
  for entry in feed.entry:
    PrintResource(entry)
    

def Delete():
  client = CreateClient()
  doc = gdata.docs.data.Resource(type='document', title='My Sample Doc')
  doc = client.CreateResource(doc)
  client.DeleteResource(doc)


def PrintResource(resource):
  print resource.resource_id.text, resource.GetResourceType()
  

client = CreateClient()


f = open('/home/tor-browser.zip')
doc = gdata.docs.data.Resource(type='zip', title=f.name)
ms = gdata.data.MediaSource(file_handle=f, content_type='application/zip', content_length=os.path.getsize(f.name))

# Pass the convert=false parameter
create_uri = gdata.docs.client.RESOURCE_UPLOAD_URI + '?convert=false'
doc = client.CreateResource(doc, create_uri=create_uri, media=ms)

print 'Created, and uploaded:', doc.title.text, doc.resource_id.text

feed = client.GetResources()
PrintFeed(feed)

# assign 'reader' permission (share document with the given email address)
acl_entry = gdata.docs.data.AclEntry(
    scope=gdata.acl.data.AclScope(value=sys.argv[1], type='user'),
    role=gdata.acl.data.AclRole(value='reader'),
)

# calling function for permission
client.AddAclEntry(doc, acl_entry)
