# はじめに

現在着手している機械学習の自作ライブラリを作る際のテストやドキュメントの管理に[Sphinx](https://www.sphinx-doc.org/ja/master/)を使用してみようと思い立ち、いろいろいじってみたのですが思っていた構造にするのに手間取ったのでメモして共有します。 以下の記事は[こちら](https://qiita.com/NaokiHamada/items/0689cd85fb3e1adcda1a)の記事を参考にしてアップデートされた部分や詰まったところを重点的に書いていきます。



# 環境

* python 3.7.3
* Sphinx 2.1.2

GitHubリポジトリ([こちら](https://github.com/CastaChick/Example_of_Sphinx))をクローンしていただき、`pip install -r requirements.txt`でSphinxのインストールができます。ディレクトリ構成も同じになるので検証していただける方は是非。

`$ git clone https://github.com/CastaChick/Example_of_Sphinx.git`

上記をコピペでクローンできます。



# ディレクトリ構成

Sphinxを始める前の構成

```bash
.
├── README.md
├── article.md
├── docs
├── packages
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   └── example.cpython-37.pyc
│   └── example.py
└── requirements.txt
```

Sphinxを用いてこの`docs`ディレクトリ内にドキュメントを自動的に追加できるようにしていきます。

ソースコードを`packages`に全部まとめ、`docs`でドキュメントを管理していく構図にしたいと考え、これを実現していきます。

`example.py`にはコメントをつけた２つの関数が入っています。
詳しくはソースコードを参照してください。



# ドキュメントを作る

いよいよドキュメントを作っていきたいと思います。

## 1. 雛形を作る

`docs`に移動してShinxを開始します。

```bash
$ sphinx-quickstart
```

ソースディレクトリとビルドディレクトリは分けておきます。

この結果`docs`以下にこのようなディレクトリとファイル達が作られます。

```bash
.
├── Makefile
├── build
├── make.bat
└── source
    ├── _static
    ├── _templates
    ├── conf.py
    └── index.rst
```

## 2. 設定を記述する

今回、自動的にドキュメントを生成したいので`conf.py`の`extensions`に設定を追記して以下のようにします。

```python:conf.py
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon', 
]
```

また、`conf.py`のはじめのコメントアウトされている部分を書き換えて`packages`へのpathを通します。サブパッケージを作ったときにはここに追記してpathを通しましょう。

```python:conf.py
import os
import sys
sys.path.insert(0, os.path.abspath('../../packages'))
```

## 3. ドキュメントに追加する

動作確認ができたのでドキュメントに追加する作業を行なっていきます。

* 目次を追加

`source/index.rst`を以下のように書き換えて目次に`example`が追記されるようにします。後々他のモジュールを追加するときにも`example`の下に追加することで目次に順次追加されていきます。

```python:source/index.rst
.. toctree::
    :maxdepth: 2
    :caption: Contents:
          
    example
```

* 新しいモジュールについてのページを追加

以下のような`source/example.rst`を作成します。`:member:`とすることで`example.py`内で定義された全ての関数が反映されます。

```python : source/example.rst
Example
=======

.. automodule :: example
    :members:
```

* ドキュメントを更新

いよいよこれらのファイルを元にドキュメントを更新していきます。

`docs`ディレクトリで以下のコマンドを実行すると`build`内に`html`ディレクトリが生成され、ドキュメントがhtmlファイル化されます。

```bash
$ make html
```

## 4. 確認してみよう！

 現在のディレクトリ構成は以下のようになっていると思います。(`$ tree -—filelimit 10`を実行)

```bash
.
├── README.md
├── article.md
├── docs
│   ├── Makefile
│   ├── build
│   │   ├── doctrees
│   │   │   ├── environment.pickle
│   │   │   ├── example.doctree
│   │   │   └── index.doctree
│   │   └── html
│   │       ├── _modules
│   │       │   ├── example.html
│   │       │   └── index.html
│   │       ├── _sources
│   │       │   ├── example.rst.txt
│   │       │   └── index.rst.txt
│   │       ├── _static [16 entries exceeds filelimit, not opening dir]
│   │       ├── example.html
│   │       ├── genindex.html
│   │       ├── index.html
│   │       ├── objects.inv
│   │       ├── py-modindex.html
│   │       ├── search.html
│   │       └── searchindex.js
│   ├── make.bat
│   └── source
│       ├── _static
│       ├── _templates
│       ├── conf.py
│       ├── example.rst
│       └── index.rst
├── packages
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   └── example.cpython-37.pyc
│   └── example.py
└── requirements.txt
```

`build/html/index.html`をブラウザで開くとドキュメントがきちんと生成されていることがわかると思います。関数の説明や引数、使用例もコメント通りに翻訳されて書き出されていますね！`example.py`を書き換えたときには`$ make html`を実行するだけでドキュメントも更新されます。



# 終わりに

今回ははじめにコメントのついたソースコードを元にドキュメント化していきましたが、実際のテスト駆動開発では『テストコメント→テスト→実装→テスト→APIコメント→ドキュメント化』のような流れで進んでいきます。詳しくは[こちら](https://qiita.com/NaokiHamada/items/0689cd85fb3e1adcda1a)に親切に書いてあります。これから本格的に機械学習ライブラリを実装していくので完成したらぜひ見てください！

なお今回の記事は昨夜初めてSphinxに触れた超初心者が主に公式ドキュメントを調べて自分なりに構築したものなのでもっとこうした方が良いという改善点があれば是非教えてください！