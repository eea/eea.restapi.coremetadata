==========================
eea.restapi.coremetadata
==========================
.. image:: https://ci.eionet.europa.eu/buildStatus/icon?job=eea/eea.restapi.coremetadata/develop
  :target: https://ci.eionet.europa.eu/job/eea/job/eea.restapi.coremetadata/job/develop/display/redirect
  :alt: Develop
.. image:: https://ci.eionet.europa.eu/buildStatus/icon?job=eea/eea.restapi.coremetadata/master
  :target: https://ci.eionet.europa.eu/job/eea/job/eea.restapi.coremetadata/job/master/display/redirect
  :alt: Master

The eea.restapi.coremetadata is a Plone add-on

.. contents::


Main features
=============

This product provides a Plone REST API endpoint called @metadata and available for all dexterity
content-types providing the `EEA Core Metadata`_. This metadata endpoint is expandable_.

The basic implementation provides generic metadata for both the Plone Site and basic Dexterity
content-type. If you need to provide this metadata information from some other fields in your
specific content-types, you can provide a ZCA adapter for your content-type.

You can look at `eea.restapi.coremetadata.api.servidces.metadata.adapters.dexterity` and inherit
the default BaseDexterityCoreMetadataAdapter to provide your own. Do not forget to register the
adapter in ZCML, look at the configure.zcml file in the same folder to know how to register it.


Install
=======

* Add eea.restapi.coremetadata to your eggs section in your buildout and
  re-run buildout::

    [buildout]
    eggs +=
      eea.restapi.coremetadata

* You can download a sample buildout from:

  - https://github.com/eea/eea.restapi.coremetadata/tree/master/buildouts/plone4
  - https://github.com/eea/eea.restapi.coremetadata/tree/master/buildouts/plone5

* Or via docker::

    $ docker run --rm -p 8080:8080 -e ADDONS="eea.restapi.coremetadata" plone

* You do not need to install this product through the Plone Add-ons Control Panel.


Buildout installation
=====================

- `Plone 5+ <https://github.com/eea/eea.restapi.coremetadata/tree/master/buildouts/plone5>`_


Source code
===========

- `Plone 5+ on github <https://github.com/eea/eea.restapi.coremetadata>`_


Eggs repository
===============

- https://pypi.python.org/pypi/eea.restapi.coremetadata
- http://eggrepo.eea.europa.eu/simple


Plone versions
==============
It has been developed and tested for Plone 5. See buildouts section above.


How to contribute
=================
See the `contribution guidelines (CONTRIBUTING.md) <https://github.com/eea/eea.restapi.coremetadata/blob/master/CONTRIBUTING.md>`_.

Copyright and license
=====================

eea.restapi.coremetadata (the Original Code) is free software; you can
redistribute it and/or modify it under the terms of the
GNU General Public License as published by the Free Software Foundation;
either version 2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc., 59
Temple Place, Suite 330, Boston, MA 02111-1307 USA.

The Initial Owner of the Original Code is European Environment Agency (EEA).
Portions created by Eau de Web are Copyright (C) 2009 by
European Environment Agency. All Rights Reserved.


Funding
=======

EEA_ - European Environment Agency (EU)

.. _EEA: https://www.eea.europa.eu/
.. _`EEA Web Systems Training`: http://www.youtube.com/user/eeacms/videos?view=1
.. _`EEA Core Metadata`: https://taskman.eionet.europa.eu/projects/netpub/wiki/EEA_Core_Metadata
.. _expandable: https://plonerestapi.readthedocs.io/en/latest/expansion.html
