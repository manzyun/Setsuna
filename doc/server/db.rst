########
DBの設定
########

設計
====

- 投稿時間：投稿された時間。そのままならこの時間から8時間で投稿内容が消える。(UnixTime)

  - unique_id

    - 投稿内容: 投稿内容。200文字（or word）以上の入力で投稿可。

       - content

    - 寿命：投稿を消す時間。「伝われ」が押された場合は1回につき8時間延長される。

       - limit


