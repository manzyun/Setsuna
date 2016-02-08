#######################
Ansibleを使うための云々
#######################

とりあえずSSHで接続するため、鍵を生成しなければいけないのである。

.. code-block:: shell

   ssh-keygen -f ~/.ssh/hoge


テスト環境編
============

鍵を渡す
--------

lxdを使用している場合、以下のコマンドで公開鍵をゲストOSに渡しておく。

lxcの使用に関しては以下のドキュメント参照。


.. code-block:: shell

   lxc file push .ssh/hoge.pub guest/root/.ssh/authorized_keys

   # ログインできるか確認
   ssh root@10.0.3.x -i .ssh/hoge

Inventry fileにサーバーを書き出す。
-----------------------------------

以下の様な具合でhostsファイルに書いておく。

.. code-block:: guess

   [guest]
   10.0.3.xx

   [guest:vars]
   ansible_ssh_private_key_file=path/to/directry/key


疎通しているか確認
------------------

先にhostsファイルやplaybookのあるディレクトリに移動しておく。
以下コマンドでAnsibleでlxcコンテナにアクセスできるか確認する。

.. code-block:: shell

   ansible guest -i hosts -u guest_user -m ping -vvvv

-vvvv オプションをつけるのは、どこで転んでいるのかを確認するために念の為付けておく。
必要ないなら抜いても良い。

Playbook実行

以下コマンドでplaybookを読み込んで実行。

.. code-block:: shell

   ansible-playbook -i hosts guest.yml





デプロイ編
==========

踏み台サーバーには秘密鍵は置かずにアクセスするため、
ssh-agentを使ってアクセスする。

参考資料
========

- Ubuntu 15.10でLXDとAnsibleを使う - Technically, technophobic. http://notchained.hatenablog.com/entry/2015/11/07/000415
- ssh-agentの使い方 - Qiita http://qiita.com/isaoshimizu/items/84ac5a0b1d42b9d355cf
- Ubuntu 15.04とLXDではじめるコンテナ型仮想化 | 株式会社インフィニットループ技術ブログ https://www.infiniteloop.co.jp/blog/2015/05/lets_start_lxd_with_vivid/
- 構成管理ツール Ansibleを使ってみる ｜ Developers.IO http://dev.classmethod.jp/?p=103332
- AnsibleでのSSH接続ユーザー指定方法 - Qiita http://qiita.com/NewGyu/items/6a6ba033588514dbca9a
- Inventory File · yteraoka/ansible-tutorial Wiki https://github.com/yteraoka/ansible-tutorial/wiki/Inventory-File
