from zope.interface import implements
from zope.component import adapts

from archetypes.schemaextender.interfaces import ISchemaExtender
from archetypes.schemaextender.field import ExtensionField

from Products.Archetypes import atapi
from Products.validation import V_REQUIRED
from Products.ATContentTypes.configuration import zconf

try: # blob
    from plone.app.blob.field import ImageField
except:
    from Products.Archetypes.Field import ImageField

from raptus.article.maps.content.map import Map
from raptus.article.maps.content.marker import Marker
from raptus.article.core import RaptusArticleMessageFactory as _



class StringField(ExtensionField, atapi.StringField):
    """ StringField
    """
class ImageField(ExtensionField, ImageField):
    """ ImageField
    """



class MapsExtender(object):
    """ add junaio link in maps edit view
    """
    implements(ISchemaExtender)
    adapts(Map)

    fields = [
        StringField('junaiolink',
            required = False,
            widget = atapi.StringWidget(
                description = '',
                macro = 'widget_junaio_link',
                label = _(u'label_junaio_label', default=u'Link for Junaio channel'),
            )
        ),
    ]

    def __init__(self, context):
        self.context = context
         
    def getFields(self):
        return self.fields

class MarkerExtender(object):
    """ add junaio link in maps edit view
    """
    implements(ISchemaExtender)
    adapts(Marker)

    fields = [
        ImageField('image',
            required=False,
            languageIndependent=True,
            storage = atapi.AnnotationStorage(),
            swallowResizeExceptions = zconf.swallowImageResizeExceptions.enable,
            pil_quality = zconf.pil_config.quality,
            pil_resize_algo = zconf.pil_config.resize_algo,
            max_size = zconf.ATImage.max_image_dimension,
            sizes= {'large'   : (768, 768),
                    'preview' : (400, 400),
                    'mini'    : (200, 200),
                    'thumb'   : (128, 128),
                    'tile'    :  (64, 64),
                    'icon'    :  (32, 32),
                    'listing' :  (16, 16),
                   },
            validators = (('isNonEmptyFile', V_REQUIRED),
                          ('checkImageMaxSize', V_REQUIRED)),
            widget = atapi.ImageWidget(
                description = '',
                label= _(u'label_image', default=u'Image to display on junaio'),
                show_content_type = False,
            )
        ),
        ]

    def __init__(self, context):
        self.context = context
         
    def getFields(self):
        return self.fields
