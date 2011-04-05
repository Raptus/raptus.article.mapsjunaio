import re

from zope import interface, component

from Products.CMFCore.utils import getToolByName

from raptus.article.mapsjunaio.interfaces import IHtmlParser
from raptus.article.maps.interfaces import IMarker



class HtmlParser(object):
    """ Provider for maps contained in an article
    """
    interface.implements(IHtmlParser)
    component.adapts(IMarker)

    BLOCK_ELEMENT = ( 'address', 'blockquote', 'center', 'del', 'dir', 'div', 'dl', 'fieldset',
                      'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'ins', 'isindex', 'menu',
                      'noframes', 'noscript', 'ol', 'p', 'pre', 'table', 'ul' )

    def __init__(self, context):
        self.context = context
        
    def getText(self):
        text = self.context.getText()
        regs = list()
        for el in self.BLOCK_ELEMENT:
            reg = re.compile('<[\s]*[\/]?[\s]*%s[\s]*[\/]?[\s]*>' % el)
            regs.append(reg)
        regs.append(re.compile('<[a-zA-Z\/][^>]*>'))
        regs.append(re.compile(r'^(.+)(?:\n|\r\n?)((?:(?:\n|\r\n?).+)+)', re.MULTILINE))
        regs.append(re.compile(r'^[\s]*', re.MULTILINE))
        for reg in regs:
            text = reg.sub(' ', text)
        text = text.strip()
        return text