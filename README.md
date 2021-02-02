# pr_analysis
web上の記事の分析（インターン用）

### ファイル構造
```bash
.
├── README.md
├── data: 分析に用いるデータを格納しているフォルダ
│   ├── extracted: 外部から取得したデータ
│   ├── interim: 加工途中データ
│   ├── processed: 分析用データ
│   └── raw: 生データ
├── doc: ドキュメントを格納しているフォルダ
│   └── models
├── result: 結果格納用フォルダ
│   └── figures: 画像格納用フォルダ
└── src: 分析コードを格納しているフォルダ
    ├── __init__.py
    ├── data: データ取得用コードを格納しているフォルダ
    │   ├── extracted: 外部からデータを取得するコードを格納しているフォルダ
    │   │   ├── scrape_func.py
    │   │   └── scrape_note.py
    │   └── read: rawデータ読み込みするコードを格納しているフォルダ
    ├── features: データをクリーニングして分析用datasetを作成するコードを格納しているフォルダ
    ├── models: 分析用コードを格納しているフォルダ
    └── result: 分析結果を格納しているフォルダ
        ├── disc: 記述統計結果
        ├── est: 推計結果
        └── visualize: 可視化
```
