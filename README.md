# atma16 3rd place solution
## 本リポジトリについて
- atmaCup#16の３位ソリューションコードを格納したもの
- 解法の詳細は[atmaCupのディスカッション](https://www.guruguru.science/competitions/22/discussions/10f89147-0db4-4279-9c86-f69c777cee5b/)を参照

## 実行方法
### 前準備
- `input/raw`フォルダに[データ](https://www.guruguru.science/competitions/22/data-sources)を配置
- ターミナルで以下のコマンドを実行してDockerコンテナを作成
```
docker compose up --build
```
- ブラウザから`localhost:8888`にアクセスし、`run.sh`に記載したtokenを入力してJupyterにアクセス

### モデル１による予測（exp206）
`exp/exp206`フォルダ配下の以下のnotebookを実行する

#### 候補生成
- already_clicked.ipynb
- co_visit_matrix.ipynb
- co_visit_matrix_trend.ipynb
- popular_yado.ipynb
- popular_yado_trend.ipynb
- matrix_factrization.ipynb
- matrix_factrization_trend.ipynb
- similar_item.ipynb

#### 特徴量作成
- create_session_item_features.ipynb
- create_session_features.ipynb
- create_item_features.ipynb

#### モデリング・予測の作成
- exp206.ipynb

### モデル２による予測（exp208）
`exp/exp208`フォルダ配下の以下のnotebookを実行する

#### 候補生成
- already_clicked.ipynb
- co_visit_matrix.ipynb
- co_visit_matrix_trend.ipynb
- popular_yado.ipynb
- popular_yado_trend.ipynb
- popular_yado_lrg.ipynb
- popular_yado_lrg_trend.ipynb
- matrix_factrization.ipynb
- matrix_factrization_trend.ipynb
- bpr.ipynb
- bpr_trend.ipynb
- item2vec.ipynb
- similar_item.ipynb

#### 特徴量作成
- create_session_item_features.ipynb
- create_session_features.ipynb
- create_item_features.ipynb

#### モデリング・予測の作成
- exp208.ipynb

### モデル３による予測（exp209）
`exp/exp209`フォルダ配下の以下のnotebookを実行する

#### 候補生成
- already_clicked.ipynb
- co_visit_matrix.ipynb
- co_visit_matrix_trend.ipynb
- co_visit_matrix_2hop.ipynb
- co_visit_matrix_2hop_trend.ipynb
- popular_yado.ipynb
- popular_yado_trend.ipynb
- popular_yado_lrg.ipynb
- popular_yado_lrg_trend.ipynb
- matrix_factrization.ipynb
- matrix_factrization_trend.ipynb
- bpr.ipynb
- bpr_trend.ipynb
- similar_item.ipynb
- item2vec.ipynb
- prone.ipynb

#### 特徴量作成
- create_session_item_features.ipynb
- create_session_features.ipynb
- create_item_features.ipynb
- create_cf_features.ipynb

#### モデリング・予測の作成
- exp209.ipynb

### アンサンブル
`exp/exp211`配下の以下のnotebookを実行する
- ensemble.ipynb

`output`フォルダに予測結果（exp211.csv）が出力される
