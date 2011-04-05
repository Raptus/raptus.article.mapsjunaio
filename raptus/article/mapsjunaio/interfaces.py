from zope.interface import Interface

class IJunaioBrowserLayer(Interface):
    """Browser layer marker interface
    """

class IHtmlParser(Interface):
    """ Parse html to plain text
    """
    
    def getText(self):
        """ return plain text
        """