import os.path
import gdata.data
import gdata.acl.data
import gdata.docs.client
import gdata.docs.data
import gdata.sample_util

class SampleConfig(object):
  APP_NAME = 'GDataDocumentsListAPISample-v1.0'
  DEBUG = True

def CreateClient():
  """Create a Documents List Client."""
  client = gdata.docs.client.DocsClient(source=SampleConfig.APP_NAME)
  client.http_client.debug = SampleConfig.DEBUG
  # Authenticate the user with CLientLogin, OAuth, or AuthSub.
  try:
    client.client_login('torbot@redteam.io', 'vum-v0d7xaju', source=None, service='writely')
    doc = client.GetAllResources():
    acl_entry = gdata.docs.data.AclEntry(
    scope=gdata.acl.data.AclScope(value='sina.rabbani@gmail.com', type='user'),
    role=gdata.acl.data.AclRole(value='reader'),
    )
    client.AddAclEntry(doc, acl_entry, send_notification=False)
  except gdata.client.BadAuthentication:
    exit('Invalid user credentials given.')
  except gdata.client.Error:
    exit('Login Error')
  return client

def PrintResource(resource):
  """Display a resource to Standard Out."""
  print resource.resource_id.text, resource.GetResourceType()
    
def GetAllResourcesSample():
  """Get and display all resources, using pagination."""
  client = CreateClient()
  # Unlike client.GetResources, this returns a list of resources
  for resource in client.GetAllResources():
    PrintResource(resource)

if __name__ == '__main__':
        GetAllResourcesSample()
