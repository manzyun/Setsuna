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

閲覧オンリー
------------

- 基本

  - http://setsuna.org/api/<version>/

- 最新の投稿の表示

  - GET
  - news
  - posts=10
  - 例: GET http://setsuna.org/api/1/news?posts=10

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
  - 例：POST http://setsuna.org/api/1/tell?id=123456

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

ユーザー登録で使える機能
------------------------

ユーザー登録っつーか、OAuthで外部サイトからアクセスとか。

  - Twitter
  - Facebook
  - Instagram
  - Google

- 投稿
  
  - POST
  - post
  - content=""
  - 例: POST http://setsuna.org/api/1/post?content="焼肉食べたいけどなんたらかんたら"

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


- 投稿の削除

  - POST
  - delete
  - id=UnixTime
  - 例：POST http://setsuna.org/api/1/delete?id=123456

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
