====================
Django World Regions
====================

Simple Django app to group countries in world's regions like *Northern America*, *Eastern Europe*, etc.

Regions data are based in http://techydiary.com/region-yaml-for-django-fixtures/ thanks Stephen for that.

`Django Countries`_ is used to handle countries.

.. note:: Currently this package don't use GeoDjango neither map data.

Installation
============
1. ``pip install django-world-regions``
2. Add ``world_regions`` to ``INSTALLED_APPS``
3. ``python manage.py migrate``

Usage
=====

.. code::

   from world_regions.models import Region

   region = Region.objects.get(countries__country='US')
   print region.name

.. _Django Countries: https://github.com/SmileyChris/django-countries