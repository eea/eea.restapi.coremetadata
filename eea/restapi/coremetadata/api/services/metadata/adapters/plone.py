# -*- coding: utf-8 -*-
from .dexterity import BaseDexterityCoreMetadataAdapter
from .interfaces import ICoreMetadata
from plone.dexterity.content import CEILING_DATE
from plone.dexterity.content import FLOOR_DATE
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.CMFPlone.utils import getSiteLogo
from zope.component import adapter
from zope.interface import implementer


@implementer(ICoreMetadata)
@adapter(IPloneSiteRoot)
class PloneSiteCoreMetadataAdapter(BaseDexterityCoreMetadataAdapter):
    """This is the base core metadata adapter.
    When building a custom adapter for your content-type, just inherit from this,
    modify the relevant method and register the adapter for your content-type.
    """

    def __init__(self, context):
        self.context = context

    def title(self):
        return self.context.Title()

    def abstract(self):
        return self.context.Description()

    def description(self):
        return self.context.Description()

    def creation_date(self):
        return self.context.creation_date.ISO8601()

    def issued_date(self):
        if self.context.effective and self.context.effective() != FLOOR_DATE:
            return self.context.effective().ISO8601()

        return None

    def expiration_date(self):
        if self.context.expires and self.context.expires() != CEILING_DATE:
            return self.context.expires().ISO8601()

        return None

    def publisher(self):
        return None

    def data_provenance(self):
        return None

    def contributors(self):
        return None

    def format(self):
        return None

    def word_count(self):
        return None

    def rights(self):
        return None

    def depiction(self):
        return getSiteLogo()
