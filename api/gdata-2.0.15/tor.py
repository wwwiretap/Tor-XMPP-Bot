import os.path
import gdata.data
import gdata.acl.data
import gdata.docs.client
import gdata.docs.data
import gdata.sample_util

import gdata.docs.service


class SampleConfig(object):
  APP_NAME = 'GDataDocumentsListAPISample-v1.0'
  DEBUG = False



def PrintResource(resource):
  """Display a resource to Standard Out."""
  print resource.resource_id.text, resource.GetResourceType()



client = gdata.docs.client.DocsClient(source=SampleConfig.APP_NAME)
client.ClientLogin('torbot@redteam.io', 'vum-v0d7xaju',"","")

def PrintFeed(feed):
  print '\n'
  if not feed.entry:
    print 'No entries in feed.\n'
  for entry in feed.entry:
    print entry.title.text.encode('UTF-8'), entry.GetDocumentType(), entry.resource_id.text

    # List folders the document is in.
    for folder in entry.InFolders():
      print folder.title

feed = client.GetDocList()
PrintFeed(feed)

#client2 = gdata.docs.service.DocsService()

#client2.ClientLogin('torbot@redteam.io', 'vum-v0d7xaju')

#feed = client2.GetAllResources()

