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

Get contributions
~~~~~~~~~~~~~~~~~~~~


Get all contributions
+++++++++++++++++++++++

api/posts access GET method.


Get new some contributions
+++++++++++++++++++++++++++++++

api/posts/save/<integer> access GET method.

example::

  api/posts/save/10

You get 10 contributions.


Get between date and time
+++++++++++++++++++++++++++++++++++++

api/posts/start/<datetime_s>/end/<datetime_e> access GET method.

datetime format is ISO 8601 default format.

example::

  api/posts/start/20150312T000000+0900/end/20150314T000000+0900

You get between 2015/3/12 to 2015/3/14 contributions.


Get filtered language contributions
++++++++++++++++++++++++++++++++++++++++++

/api/<lang>/posts access GET method.

language code is ISO 639-3

example::

  api/jpn/posts/

You get Japanese language contributions.


Get filtered language and some new contributions
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

api/<lang>/posts/<integer> access GET method.

example::

  api/jpn/posts/save/10

You get Japanese language new 10 contributions.  


Get between date and time and filtered language
++++++++++++++++++++++++++++++++++++++++++++++++++

/api/<lang>/posts/start/<datetime_s>/end/<datetime_e>

example::

  /api/jpn/posts/start/20150312T000000+0900/end/20150314T000000+0900

You get between 2015/3/12 to 2015/3/14 and Japanese language contributions.


Get one post
++++++++++++++++

/api/post/<id> access GET method.


Contribution
~~~~~~~~~~~~~~

1. Make JSON::

  {
    "content":your content here,
    "password": you want delete contribution password.
    "lang": Language code by ISO 639-2.
  }

.. note:: If "password" is empty then make random 4 digit password.

2. Contribute this address or api/post your JSON on POST method.
3. 'Comming server response::

  {
    "id": Your contribution id,
    "content": You contribute content,
    "limit": Contribution delete time(Unix Time),
    "password": Delete contribution password,
    "lang": Language code by ISO 639-3.
  }


Response(no comment)
~~~~~~~~~~~~~~~~~~~~~~~

1. Access contribution on POST method.
2. Comming server response::

  {
    "id": Your responsed contribution id,
    "content": Your responsed contribution
    "limit": Contribution delete time(Unix Time),
    "password": "Delete contribution password
    "lang": Language code by ISO 639-3,
    "link": Linked to contribution.
  }


Response(comment)
~~~~~~~~~~~~~~~~~~~~

1. Make JSON::

  {
    "content":your content here,
    "password": you want delete contribution password,
    "lang": Language code by ISO 639-3.
  }

.. note:: If "password" is nothing then make random 4 digit password.


2. Contribute you want response contribution address on POST method
3. Comming server response::

  {
    "id": Your responsed contribution id,
    "content": Your responsed contribution
    "limit": Contribution delete time(Unix Time),
    "password": "Delete contribution password
    "lang": Language code by ISO 639-3,
    "link": Linked to contribution.
  }


Delete Contribution
~~~~~~~~~~~~~~~~~~~~~~

1. Make JSON::

  {
    "password": your contribution has delete password.
  }


2. Contribute this address your JSON on DELETE method.
3. 'Comming server response::

  {
    "message": "Your post deleted ;)"
  }


FAQ
-----

Where web page?
  Nothing special. Because, I want make a service and I'm poor sense web design. Because so only Web and JSON API.

Am I not user requiring?
  Yes. This service is anonymity. And I can't manage a server that is managing the large amount of user information.
