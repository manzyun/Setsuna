##############
基本コンセプト
##############

3行でまとめる
=============

- 投稿はそのままだと24時間で消える
- 投稿するには下限200文字以上を超えなければならない
- 「伝われ」ボタンで投稿の延命ができる


APIを考える
===========

APIはAPIでJSONを渡す。
つまりHTML表示の方とはべつで作る。

閲覧オンリー
------------

- 基本

  - http://setsuna.org/api/<version>/posts

- 投稿を全件表示

  - GET
  - (None)
  - (None)
  - 例: GET http://setsuna.org/api/v1.0/posts

    - 返答

      .. code-block:: json

         [
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
  - posts
  - limit=10
  - 例: GET http://setsuna.org/api/v1.0/posts&limit=20

    - 返答

      .. code-block:: json

         [
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
  - unique_id=ObjectId
  - 例：POST http://setsuna.org/api/v1.0/tell/123456

    - 返答

      .. code-block:: json

          {
           "content" : "...",
           "limit" : "..."
          }

投稿周り
------------------------

投稿内容はパスワードで削除可能とする。

- 投稿
  
  - POST
  - post
  - content=""
  - delkey=""
  - 例: POST http://setsuna.org/api/v1.0/posts
  - contentとpasswordはjsonで渡す

    - 返答

      .. code-block:: json

          {
           "id" : 123456
           "content" : "焼肉食べたいけどなんたらかんたら",
           "password" : "hogefuga"
           "limit" : "..."
          }


- 投稿の削除

  - POST
  - delete
  - id=ObjectId
  - delkey=投稿時に指定したパスワード
  - 例：DELETE http://setsuna.org/api/v1.0/123456
  - passwordはjsonで渡す
    - 返答

      .. code-block:: json

          {
            'error': Not Found,
            'message': This post was deleted maybe.
          }
  
参考資料
========

- Web API Design - 開発者が愛するインターフェイスを作る http://www.infoq.com/jp/news/2012/04/web-api-design-book
