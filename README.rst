tw2.protovis.custom
===================

:Author: Ralph Bean <rbean@redhat.com>

.. comment: split here

.. _toscawidgets2 (tw2): http://toscawidgets.org/documentation/tw2.core/
.. _protovis: http://vis.stanford.edu/protovis/

tw2.protovis.custom is a `toscawidgets2 (tw2)`_ wrapper for `protovis`_.

Live Demo
---------

Peep the `live demonstration <http://tw2-demos.threebean.org/module?module=tw2.protovis.custom>`_.

Links
-----

You can `get the source from github <http://github.com/toscawidgets/tw2.protovis.custom>`_,
check out `the PyPI page <http://pypi.python.org/pypi/tw2.protovis.custom>`_, and
report or look into `bugs <http://github.com/toscawidgets/tw2.protovis.custom/issues/>`_.

Description
-----------

`toscawidgets2 (tw2)`_ aims to be a practical and useful widgets framework
that helps people build interactive websites with compelling features, faster
and easier. Widgets are re-usable web components that can include a template,
server-side code and JavaScripts/CSS resources. The library aims to be:
flexible, reliable, documented, performant, and as simple as possible.

`protovis`_ composes custom views of data with simple marks such as bars and dots. Unlike low-level graphics libraries that quickly become tedious for visualization, Protovis defines marks through dynamic properties that encode data, allowing inheritance, scales and layouts to simplify construction.

This module, tw2.protovis.custom, provides `toscawidgets2 (tw2)`_ widgets that render `protovis`_ data visualizations.

Sampling tw2.protovis.custom in the WidgetBrowser
-------------------------------------------------

The best way to scope out ``tw2.protovis.custom`` is to load its widgets in the
``tw2.devtools`` WidgetBrowser.  To see the source code that configures them,
check out ``tw2.protovis.custom/tw2/protovis/custom/samples.py``

To give it a try you'll need git, python, and `virtualenvwrapper
<http://pypi.python.org/pypi/virtualenvwrapper>`_.  Run::

    $ git clone git://github.com/toscawidgets/tw2.protovis.custom.git
    $ cd tw2.protovis.custom
    $ mkvirtualenv tw2.protovis.custom
    (tw2.protovis.custom) $ pip install tw2.devtools
    (tw2.protovis.custom) $ python setup.py develop
    (tw2.protovis.custom) $ paster tw2.browser

...and browse to http://localhost:8000/ to check it out.
