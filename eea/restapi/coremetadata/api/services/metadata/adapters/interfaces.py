# -*- coding: utf-8 -*-
from zope.interface import Interface


class ICoreMetadata(Interface):
    """Base interface to provide core metadata fields for @metadata endpoint .

    EEA Core Metadata list is here:
    https://taskman.eionet.europa.eu/projects/netpub/wiki/EEA_Core_Metadata
    """

    def title():
        """ return the title of the item """

    def abstract():
        """ return the abstract of the item """

    def description():
        """ return the description of the item """

    def creation_date():
        """ return the creation date of the item. ISO 8601 format."""

    def issued_date():
        """ return the issued date (publication date, effective date). ISO 8601 format. """

    def expiration_date():
        """ OPTIONAL: return the expiration date of the item. ISO 8601 format. """

    def topics():
        """ return the list of topics of the item """

    def geo_coverage():
        """ return the geocoverage of the item """

    def temporal_coverage():
        """ return the years covered by the resource. It must be a list of years. Ex.: [2002, 2004] """

    def content_type():
        """ return the content-type id for the item """

    def provides():
        """ return the interfaces provided by the item """

    def publisher():
        """ return the information about the publisher of the item (normally the website owner)"""

    def data_provenance():
        """ return the data provenance information, it should be a list """

    def contributors():
        """ the list of contributors to this item """

    def format():
        """ the format of the item """

    def word_count():
        """ word count of the item """

    def rights():
        """ use rights of the item """

    def depiction():
        """ the url of a image representing this item """

    def render_metadata():
        """ return all metadata rendered in a dict """
