# -*- coding: utf-8 -*-
from .interfaces import ICoreMetadata
from plone.app.contenttypes.behaviors.leadimage import ILeadImageBehavior
from plone.dexterity.content import CEILING_DATE
from plone.dexterity.content import FLOOR_DATE
from plone.dexterity.interfaces import IDexterityContent
from zope.component import adapter
from zope.component import getMultiAdapter
from zope.interface import implementer
from zope.interface import providedBy


@implementer(ICoreMetadata)
@adapter(IDexterityContent)
class BaseDexterityCoreMetadataAdapter(object):
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

    def topics(self):
        if self.context.subject:
            return self.context.subject

        return None

    def geo_coverage(self):
        return None

    def temporal_coverage(self):
        return None

    def content_type(self):
        return self.context.portal_type

    def provides(self):
        return [
            "{}.{}".format(I.__module__, I.__name__) for I in providedBy(self.context)
        ]

    def publisher(self):
        return None

    def data_provenance(self):
        return None

    def contributors(self):
        if self.context.contributors:
            return self.context.contributors

        return None

    def format(self):
        return None

    def word_count(self):
        return None

    def rights(self):
        if self.context.rights:
            return self.context.rights

        return None

    def depiction(self):
        if ILeadImageBehavior.providedBy(self.context):
            images_view = getMultiAdapter((self.context, self.request), name="images")
            scale = images_view.scale("image", scale="preview")
            if scale:
                return scale.url

        return None

    def render_metadata(self):
        data = {}

        data["title"] = self.title()
        data["abstract"] = self.abstract()
        data["description"] = self.description()
        data["creation_date"] = self.creation_date()

        # All these are optional, so check before exporting None as a value
        if self.issued_date():
            data["issued_date"] = self.issued_date()
        if self.expiration_date() is not None:
            data["expiration_date"] = self.expiration_date()
        if self.topics() is not None:
            data["topics"] = self.topics()
        if self.geo_coverage() is not None:
            data["geo_coverage"] = self.geo_coverage()
        if self.temporal_coverage() is not None:
            data["temporal_coverage"] = self.temporal_coverage()
        if self.content_type() is not None:
            data["content_type"] = self.content_type()
        if self.provides() is not None:
            data["provides"] = self.provides()
        if self.publisher() is not None:
            data["publisher"] = self.publisher()
        if self.data_provenance() is not None:
            data["data_provenance"] = self.data_provenance()
        if self.contributors() is not None:
            data["contributors"] = self.contributors()
        if self.format() is not None:
            data["format"] = self.format()
        if self.word_count() is not None:
            data["word_count"] = self.word_count()
        if self.rights() is not None:
            data["rights"] = self.rights()
        if self.depiction() is not None:
            data["depiction"] = self.depiction()

        return data
