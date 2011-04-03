from zope import component

from Acquisition import aq_inner

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

from raptus.article.maps.interfaces import IMarkers

class View(BrowserView):
    
    __call__ = ViewPageTemplateFile('junaio.pt')
    
    def __init__(self, context, request):
        super(View,self).__init__(context, request)
        self.props = getToolByName(self.context, 'portal_properties').raptus_article
    
    def markers(self):
        context = aq_inner(self.context)
        markers = list()
        for brain in IMarkers(context).getMarkers():
            object = brain.getObject()
            scales = component.queryMultiAdapter((object, object.REQUEST), name='images')
            di = dict(brain = brain,
                      obj = object,
                      uid = brain.UID,
                      title = object.Title(),
                      text = object.getText(),
                      latitude = object.getLatitude(),
                      longitude = object.getLongitude(),
                      icon = self._thumbnail(object, scales),
                      thumbnail = self._icon(object, scales)
                      )
            markers.append(di)
        return markers
            
    def _thumbnail(self, object, scales):
        thumb = None
        thumbnail_w = self.props.getProperty('junaio_thumbnail_width')
        thumbnail_h = self.props.getProperty('junaio_thumbnail_height')
        if scales.field('image'):
            thumb = scales.scale('image', width=thumbnail_w, height=thumbnail_h)
        if thumb is not None:
            return thumb.absolute_url()
        else:
            return self._default(self.props.getProperty('junaio_thumbnail_default'))
        
    def _icon(self, object, scales):
        icon = None
        icon_w = self.props.getProperty('junaio_icon_width')
        icon_h = self.props.getProperty('junaio_icon_height')
        if scales.field('image'):
            icon = scales.scale('image', width=icon_w, height=icon_h)
        if icon is not None:
            return icon.absolute_url()
        else:
            return self._default(self.props.getProperty('junaio_icon_default'))
    
    def _default(self, name):
        portal_state = component.getMultiAdapter((self.context, self.request), name=u'plone_portal_state')
        site = portal_state.portal()
        return '%s/%s' %(site.absolute_url(), name)
    
    
 