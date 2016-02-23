##############
基本コンセプト
##############

3行でまとめる
=============

- 投稿はそのままだと8時間で消える
- 投稿するには下限200文字以上を超えなければならない
- 「伝われ」ボタンで投稿の延命ができる


APIを考える
===========

APIはAPIでJSONを渡す。
つまりHTML表示の方とはべつで作る。

閲覧オンリー
------------

- 基本

  - http://setsuna.org/api/<version>/

- 最新投稿を複数表示

  - GET
  - (None)
  - (None)
  - 例: GET http://setsuna.org/api/1/

    - 返答

      .. code-block:: json

         [
          {
           "developerMessage" : "...",
           "userMessage" : "...",
           "errorCode" : 100,
           "moreInfo" : "http://developers.setsuna.org/errors/100"
          },
          {
           "content" : "...",
           "limit" : "..."
          },
          {
           "content" : "...",
           "limit" : "..."
          }
         ]

- 投稿の複数表示

  - GET
  - news
  - posts=10
  - 例: GET http://setsuna.org/api/1/news?start=0&end=20

    - 返答

      .. code-block:: json

         [
          {
           "developerMessage" : "...",
           "userMessage" : "...",
           "errorCode" : 100,
           "moreInfo" : "http://developers.setsuna.org/errors/100"
          },
          {
           "content" : "...",
           "limit" : "..."
          },
          {
           "content" : "...",
           "limit" : "..."
          }
         ]

- 「伝われ」

  - POST
  - tell
  - id=<UnixTime>
  - 例：POST http://setsuna.org/api/1/123456

    - 返答

      .. code-block:: json

         [
          {
           "developerMessage" : "...",
           "userMessage" : "...",
           "errorCode" : 100,
           "moreInfo" : "http://developers.setsuna.org/errors/100"
          }
          {
           "content" : "...",
           "limit" : "..."
          }
         ]

投稿周り
------------------------

投稿内容はパスワードで削除可能とする。

- 投稿
  
  - POST
  - post
  - content=""
  - password=""
  - 例: POST http://setsuna.org/api/1/post?content="焼肉食べたいけどなんたらかんたら"&password="hogefuga"

    - 返答

      .. code-block:: json

         [
          {
           "developerMessage" : "...",
           "userMessage" : "...",
           "errorCode" : 100,
           "moreInfo" : "http://developers.setsuna.org/errors/100"
          }
          {
           "id" : 123456
           "content" : "焼肉食べたいけどなんたらかんたら",
           "password" : "hogefuga"
           "limit" : "..."
          }
         ]


- 投稿の削除

  - POST
  - delete
  - id=UnixTime
  - password=投稿時に指定したパスワード
  - 例：DELETE http://setsuna.org/api/1/123456

    - 返答

      .. code-block:: json

         [
          {
           "developerMessage" : "...",
           "userMessage" : "...",
           "errorCode" : 100,
           "moreInfo" : "http://developers.setsuna.org/errors/100"
          }
          {
           "id" : 123456
           "content" : "焼肉食べたいけどなんたらかんたら",
           "limit" : "..."
          }
         ]
  
参考資料
========

- Web API Design - 開発者が愛するインターフェイスを作る http://www.infoq.com/jp/news/2012/04/web-api-design-book
