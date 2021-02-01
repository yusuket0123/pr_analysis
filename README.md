# pr_analysis
web上の記事の分析（インターン用）

### ファイル構造
```bash
.
├── data: 分析に用いるデータを格納しているフォルダ
├── doc: ドキュメントを格納しているフォルダ
├── renv: renvのconfigフォルダ。renvによる自動生成フォルダで、基本的にここは弄らない。
├── result: 分析結果を格納しているフォルダ
├── src: 分析以外のコードを格納しているフォルダ
│   └── config.yaml: 本レポジトリのconfigファイル。path関連などはここに記述すると良い。
├── task: 分析コード。分析の種類ごとに't\d+(.R|.py)'という名前のファイルに分けている。
├── README.md
└── taskrunner.R: Rを用いた分析のタスクランナー。
```
