#######################
Ansibleを使うための云々
#######################

とりあえずSSHで接続するため、鍵を生成しなければいけないのである。

   .. code-block:: guess

      ssh-keygen -f ~/.ssh/hoge


テスト環境編
============


lxdを使用している場合、以下のコマンドで公開鍵をゲストOSに渡しておく。

   .. code-block:: guess

      lxc file push .ssh/hoge.pub guest/root/.ssh/authorized_keys

      # ログインできるか確認
      ssh root@10.0.3.x -i .ssh/hoge


デプロイ編
==========

踏み台サーバーには秘密鍵は置かずにアクセスするため、
ssh-agentを使ってアクセスする。

参考資料
========

- Ubuntu 15.10でLXDとAnsibleを使う - Technically, technophobic. http://notchained.hatenablog.com/entry/2015/11/07/000415
- ssh-agentの使い方 - Qiita http://qiita.com/isaoshimizu/items/84ac5a0b1d42b9d355cf
