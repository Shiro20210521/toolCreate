# DDLCreator 使用方法

このリポジトリには、Streamlit を利用して SQL の DDL を自動生成するツール `DDLCreator` が含まれています。

## 1. Python のインストール

1. [Python 公式サイト](https://www.python.org/downloads/) から Python 3 系をダウンロードしてインストールします。
   - Windows の場合はインストール時に **Add Python to PATH** にチェックを入れてください。
2. 以下のコマンドでインストールが成功しているか確認します。

```bash
python --version
```

## 2. リポジトリの取得と依存ライブラリのインストール

1. 本リポジトリをクローンします。

```bash
git clone <このリポジトリのURL>
cd toolCreate
```

2. `streamlit` をインストールします。

```bash
pip install streamlit
```

## 3. アプリケーションの起動

以下のコマンドで DDL 作成アプリを起動します。

```bash
streamlit run DDLCreator/ddlCreator.py
```

ブラウザが自動で開かない場合は、ターミナルに表示された URL をブラウザに貼り付けてアクセスしてください。

## 4. 使い方

1. 画面上部の入力欄で **テーブル名** を指定します。
2. **カラム数** を指定し、各カラムについて名前・型・デフォルト値・主キー/外部キーなどを入力します。
3. 「次のテーブルを生成」ボタンで複数のテーブルを追加できます。
4. 「出力」ボタンを押すと、入力内容から DDL が生成され、`DDL.sql` としてダウンロードできます。
5. 「クリア」ボタンで入力内容をリセットし、再度入力を行えます。

