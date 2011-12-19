import pickle

picklelist = open('google-doc-filelist', 'r')
list = pickle.load(picklelist)
#list =["tor-browser-farsi-win64","tor-browser-farsi-win32","tor-browser-farsi-mac64","tor-browser-farsi-mac32"]
file = open('google-doc-filelist','w')
list.del('tor-browser-farsi-win64TEST')
pickle.dump(list,file)
file.close()
picklelist.close()
picklelist.close()

for item in list:
    print item
    