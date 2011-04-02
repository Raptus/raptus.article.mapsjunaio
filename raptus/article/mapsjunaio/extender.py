from zope.interface import implements
from zope.component import adapts

from archetypes.schemaextender.interfaces import ISchemaExtender
from archetypes.schemaextender.field import ExtensionField

from Products.Archetypes import atapi

class StringField(ExtensionField, atapi.StringField):
    """ StringField
    """


class MapsExtender(object):
    """ add junaio link in maps edit view
    """
    implements(ISchemaExtender)
    adapts(IArticle)

    fields = [        
        StringField('junaiolink',
            required = False,
            searchable = False,
            widget = atapi.StringWidget(
                description = '',
                label = _at(u'label_junaio_label', default=u'Link for Junaio channel'),
            )
        ),
    ]

    def __init__(self, context):
         self.context = context
         
    def getFields(self):
        return self.fields
