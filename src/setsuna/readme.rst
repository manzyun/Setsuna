====================
Setsuna Web API
====================

author
-------------

Hidetsugu Takahashi a.k.a manzyun <manzyun@gmail.com>


What's this?
---------------------

This is Micro SNS. Your post will delete 6 hour.

But, your post is gotten response of 1 hour plus every,


How to use
--------------

Contribution
~~~~~~~~~~~~~~

1. Make JSON::

  {
    "content":your content here,
    "password": you want delete contribution password.
    "lang": Language code by ISO 639-2.
  }

.. note:: If "password" is empty then make random 4 digit password.

2. Contribute this address your JSON on POST method.
3. 'Comming server response your contribut infomartion in "data" section::

  {
    "id": Your contribution id,
    "content": You contribute content,
    "password": Delete contribution password,
    "lang": Language code by ISO 639-2.
  }


Response(no comment)
~~~~~~~~~~~~~~~~~~~~~~~

1. Access contribution on POST method.
2. Comming server response your responsed contribution information in "data" section::

  {
    "id": Your responsed contribution id,
    "content": Your responsed contribution
  }


Response(comment)
~~~~~~~~~~~~~~~~~~~~

1. Make JSON::

  {
    "content":your content here,
    "password": you want delete contribution password,
    "lang": Language code by ISO 639-2.
  }

.. note:: If "password" is nothing then make random 4 digit password.


2. Contribute you want response contribution address on POST method
3. Comming server response your contribution information in "data" section::

  {
    "id": Your contribution id,
    "content": You contribute content,
    "password": Delete contribution password,
    "lang": Language code by ISO 639-2.
  }


Delete Contribution
~~~~~~~~~~~~~~~~~~~~~~

1. Make JSON::

  {
    "password": your contribution has delete password.
  }


2. Contribute this address your JSON on DELETE method.
3. 'Comming server response your contribute infomartion in "data" section::

  {
    "message": "Your post deleted ;)"
  }


.. note:: If contribution has response then delete with responsed contribution.

FAQ
-----

Where web page?
  Nothing special. Because, I want make a service and I'm poor sense web design. Because so only Web and JSON API.

Am I not user requiring?
  Yes. This service is anonymity. And I can't manage a server that is managing the large amount of user information.
