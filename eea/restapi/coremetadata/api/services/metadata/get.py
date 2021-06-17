# -*- coding: utf-8 -*-
from .adapters.interfaces import ICoreMetadata
from plone import api
from plone.restapi.interfaces import IExpandableElement
from plone.restapi.services import Service
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface


@implementer(IExpandableElement)
@adapter(Interface, Interface)
class Metadata(object):
    def __init__(self, context, request):
        self.context = context.aq_explicit
        self.request = request

    def __call__(self, expand=False):
        result = {
            "metadata": {
                "@id": "{}/@metadata".format(
                    self.context.absolute_url(),
                ),
            },
        }
        if not expand:
            return result

        adapter = ICoreMetadata(self.context)

        items = adapter.render_metadata()

        result["metadata"]["items"] = items
        return result


class MetadataGet(Service):
    def reply(self):
        service_factory = Metadata(self.context, self.request)
        return service_factory(expand=True)["metadata"]
