from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from raptus.article.maps.interfaces import IMarkers

class View(BrowserView):
    
    __call__ = ViewPageTemplateFile('junaio.pt')
    
    
    def makers(self):
        return IMarkers(self.context)
