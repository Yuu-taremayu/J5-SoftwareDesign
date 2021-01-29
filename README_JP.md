# J5-SoftwareDesign
2020 ソフトウェア設計II

グループ開発

## チーム ｐｙてょｎ
### メンバー
 - 野口　蓮太 (班長)
 - 内藤　悟嗣
 - 山下　零司
 - 三上　竜也
 - 三浦　夢生

## 概要
Pythonでのフィールドすごろくの開発

名称　"Field Search Record ~凄録~"

## ルール
 - 縦4マス,横5マスのフィールド.
 - サイコロをふって出た目の数だけ上下左右に動くか,その場にとどまることができる.
 - イベントを駆使し,早く勝利条件を達成した者から勝ち抜ける.
 - プレイ人数 (2人～4人).
	 - 初期位置はフィールドの四隅のどれか.
 - 勝利条件
	 - プレイヤーがゲームをクリアするには,任意の条件を満たしている必要がある.
	 - 条件はゲーム開始時にプレイヤーごとに割り振られる.
 - イベント
	 - バトル
		 - プレイヤーが接近すると発生する.
	 - ショップ
		 - フィールド上に配置される.
		 - プレイヤーのステータスmoneyを消費してアイテムを手に入れることができる.
	 - ジョブチェンジ
		 - フィールド上に配置される.
		 - 与えられたジョブを変更することができる.

## 物の抽出
 - プレイヤー
	 - ステータス
		 - 財産
		 - 筋力
		 - 耐久
		 - ストレス
		 - 速さ
		 - 理解力
		 - 知性
	 - job
		- 無職
		- アスリート
		- 探偵
		- 医者
		- エンジニア
		- 狩猟者
		- 緊急医療者
		- 警察
		- 先生
	 - 目的
 - フィールド
	 - イベント
		 - 店
		 - 職業店
 - ダイス

## 物の振る舞い
 - プレイヤー
	 - フィールド内を上下左右に動く
	 - フィールド上で買い物をしたり,転職したりする
	 - 他のプレイヤーと戦う
 - フィールド
	 - 画面上に配置され,プレイヤーが動く場所を提供する
	 - 買い物,転職が行われる
 - ダイス
	 - 1~6の目を出し,プレイヤーの動きに影響を及ぼす

## データ構造
 - "ゲーム" クラス
```
class GAME():
	self.WIDTH		:ゲーム画面の横幅を持つ変数,main関数から渡される
	self.HEIGHT		:ゲーム画面の縦幅を持つ変数,main関数から渡される
	self.MAG		:ゲーム画面の倍率を持つ変数,main関数から渡される
	self.root		:TKinterを扱うためのインスタンス
	self.scene		:ゲームの画面遷移状態を表す数値
	self.var_start_menu	:関数start_menuのデータを保持するリスト
	self.var_select_menu	:関数select_menuのデータを保持するリスト
	self.frame		:フレーム作成のインスタンス
	self.pressed		:押されているキーが格納される配列
	canvas			:画面描写を行うためのインスタンス
	self.field		:フィールドの内部状態を保持するインスタンス
	self.player		:プレイヤーの内部状態を保持するインスタンスの配列
	self.turn		:現在行動するプレイヤーを指し示すフラグ
```
 - "プレイヤー" クラス
```
class PLAYER():
	self.x			:プレイヤーのx座標を持つ変数
	self.y			:プレイヤーのy座標を持つ変数
	self.money		:プレイヤーのステータスmoneyを持つ変数
	self.muscle		:プレイヤーのステータスmuscleを持つ変数
	self.stress		:プレイヤーのステータスstressを持つ変数
	self.dexterity		:プレイヤーのステータスdexterityを持つ変数
	self.job		:プレイヤーのステータスjobを持つ変数
	self.condition		:プレイヤーの勝利条件を持つ変数
	self.goal_flag	:
	self.item_num	:アイテムの個数
	self.item		:アイテムの情報（所持数，名前，値段，説明）
```
 - "フィールド" クラス
```
class FIELD():
	self.x			:プレイヤーのx座標を持つ変数
	self.y			:プレイヤーのy座標を持つ変数
	self.WIDTH		:ゲーム画面の横幅を持つ変数,GAMEクラスから渡される
	self.HEIGHT		:ゲーム画面の縦幅を持つ変数,GAMEクラスから渡される
	self.MAG		:ゲーム画面の倍率を持つ変数,GAMEクラスから渡される
	self.num_shop		:ショップマスの数を持つ変数
	self.num_jobchange	:ジョブチェンジマスの数を持つ変数
	self.num_money	:マネーマスの数を持つ変数
	self.shop_flag	:ショップイベントマスにとまると1，抜け出すと0になる
	self.useitem_flag	:サイコロを振った後1，アイテム使用画面から抜け出すと0になる
	self.select_item	:ショップで選ばれてるアイテムを持つ変数
	self.cantbuy_flag	:所持金が選んだアイテムより低いと1になる
	self.donthave_flag	:使用するアイテムを持っていないとき1になる
```

## 関数仕様
### 基本データ構造
 - "ゲーム" クラス
```
class GAME():
	self.WIDTH		:ゲーム画面の横幅を持つ変数,main関数から渡される
	self.HEIGHT		:ゲーム画面の縦幅を持つ変数,main関数から渡される
	self.MAG		:ゲーム画面の倍率を持つ変数,main関数から渡される
	self.root		:TKinterを扱うためのインスタンス
	self.scene		:ゲームの画面遷移状態を表す数値
	self.var_start_menu	:関数start_menuのデータを保持するリスト
	self.var_select_menu	:関数select_menuのデータを保持するリスト
	self.frame		:フレーム作成のインスタンス
	self.pressed		:押されているキーが格納される配列
	canvas			:画面描写を行うためのインスタンス
	self.field		:フィールドの内部状態を保持するインスタンス
	self.player		:プレイヤーの内部状態を保持するインスタンスの配列
	self.turn		:現在行動するプレイヤーを指し示すフラグ
```
 - "プレイヤー" クラス
```
class PLAYER():
	self.x			:プレイヤーのx座標を持つ変数
	self.y			:プレイヤーのy座標を持つ変数
	self.money		:プレイヤーのステータスmoneyを持つ変数
	self.muscle		:プレイヤーのステータスmuscleを持つ変数
	self.stress		:プレイヤーのステータスstressを持つ変数
	self.dexterity		:プレイヤーのステータスdexterityを持つ変数
	self.job		:プレイヤーのステータスjobを持つ変数
	self.condition		:プレイヤーの勝利条件を持つ変数
	self.goal_flag		:
	self.item_num		:アイテムの個数
	self.item		:アイテムの情報（所持数，名前，値段，説明）
```
 - "フィールド" クラス
```
class FIELD():
	self.x			:プレイヤーのx座標を持つ変数
	self.y			:プレイヤーのy座標を持つ変数
	self.WIDTH		:ゲーム画面の横幅を持つ変数,GAMEクラスから渡される
	self.HEIGHT		:ゲーム画面の縦幅を持つ変数,GAMEクラスから渡される
	self.MAG		:ゲーム画面の倍率を持つ変数,GAMEクラスから渡される
	self.num_shop		:ショップマスの数を持つ変数
	self.num_jobchange	:ジョブチェンジマスの数を持つ変数
	self.num_money	:マネーマスの数を持つ変数
	self.shop_flag	:ショップイベントマスにとまると1，抜け出すと0になる
	self.useitem_flag	:サイコロを振った後1，アイテム使用画面から抜け出すと0になる
	self.select_item	:ショップで選ばれてるアイテムを持つ変数
	self.cantbuy_flag	:所持金が選んだアイテムより低いと1になる
	self.donthave_flag	:使用するアイテムを持っていないとき1になる
```

### 基本関数仕様
 - "ゲーム" クラス
```
class GAME():
	def __init__():
		引数:ウィンドウの幅, 高さ, tkinterを使うための変数
		戻り値:なし
		# initialize some constant and variables in GAME class
		# Gameクラスの変数と定数を初期化
		# キーボード設定の初期化
		# start_menu()を呼び出す
	def key_pressed()
		引数:イベント
		戻り値:なし
		# 何かキーが押されたときに呼び出される
		# 現在押されているキーをpressedへ格納する
	def key_released()
		引数:イベント
		戻り値:なし
		# 押されていたキーが離されたときに呼び出される
		# pressedから離されたキーを削除する
	def start_menu()
		引数:なし
		戻り値:0
		# スタートメニューを表示する関数
		# キー操作によってゲームスタートか終了を制御する
		# ゲームスタートのボタンでselect_menu()を呼び出す
	def select_menu()
		引数:なし
		戻り値:0
		# セレクトーを表示する関数
		# キー操作で人数を、マウスとキー操作でプレイヤ名を決定する
		# ゲームスタートのボタンを押すとstart()を呼び出す
		# プレイヤー数に応じて各プレイヤーの初期位置を決める
	def start()
		引数:なし
		戻り値:なし
		# ゲームの各処理をする関数を呼び出す関数
		# print_field()を呼び出す
		# print_player()を呼び出す
		# move_player()を呼び出す
		# check_win_condition()を呼び出す
		# check_exit_condition()を呼び出す
	def print_field()
		引数:なし
		戻り値:なし
		# フィールドのインスタンスを用いてフィールドを表示する
		# プレイヤーのインスタンスを用いてプレイヤーのステータスを表示する
		# プレイヤー数に応じてステータスの数、位置を変える
	def print_player()
		引数:なし
		戻り値:なし
		# プレイヤーを表示する
	def roll_dice()
		引数:なし
		戻り値:なし
		# サイコロの目を乱数を用いて決定する関数
	def check_win_condition()
		引数:なし
		戻り値:なし
		# プレイヤが勝利条件を満たしているかを確認する関数
		# 満たしているならplayerクラスのconditionにTrueを格納
	def check_exit_condition()
		引数:なし
		戻り値:なし
		# ゲームの終了条件を判定する関数
		# もし全てのプレイヤの勝利条件が満たされていればshow_result()を呼び出す
	def move_player()
		引数:なし
		戻り値:なし
		# フィールド上に配置されたプレイヤーを動かす関数
		# フィールドに存在する範囲のみ動ける
		# 止まったマスのイベントの実行
	def show_result()
		引数:なし
		戻り値:なし
		# プレイヤの勝利条件を満たした順に順位を表示する関数
	def shop()
		引数:プレイヤー
		戻り値:なし
		# ショップイベントの実行
	def item()
		引数:プレイヤー
		戻り値:なし
		# アイテム使用の実行

```
 - "プレイヤー" クラス
```
class PLAYER():
	def __init__():
		引数:なし
		戻り値:なし
		# プレイヤの各ステータスを初期化する
		# ステータスはmoney, muscle, stress, job, DEX
		# 各プレイヤに勝利条件を付与する
		# decide_jobを呼び出して職業を付与する
	def decide_job():
		引数:なし
		戻り値:なし
		# ランダムで職業を決める
		# 職業は'Teacher', 'Engineer', 'SportsMan' and 'Nojob'の４つ
```
 - "フィールド" クラス
```
class FIELD():
	def __init__():
		引数:なし
		戻り値:なし
		# フィールドの初期化
		# x, y, number of shop, number of job change point and field array
	def set_field():
		引数:なし
		戻り値:フィールドの横マス数, 縦マス数
		# フィールドの大きさを定める
	def set_events()
		引数:なし
		戻り値:ショップのマス数, ジョブチェンジのマス数，マネーマスのマス数
		# 各イベントの数を定める
	def init_field():
		引数:フィールドの横マス数, 縦マス数, ショップの数, ジョブチェンジの数
		戻り値:フィールドの配列
		# ランダムにイベントを配置
		# イベントのないマスは「ノーマル」
	def event_money():
		引数:プレイヤー
		戻り値:なし
		# お金が増える，もしくは減るイベント
		# プレイヤーの職業によってお金を増やす
		# ランダムに（50, 100, 150）お金が減る
	def event_jobchange():
		引数:プレイヤー
		戻り値:なし
		# 職業を変えるイベント
	def print_shop():
		引数:プレイヤー
		戻り値:なし
		# 所持金を表示する
		# アイテムの情報（所持数，名前，値段）を表示する
		# 選択されているアイテムを表示する
	def select_shop():
		引数:プレイヤー，押されたキー
		戻り値:exitでショップを出るとき0
		# Up, Downキーでアイテムを選択
		# Returnキーでアイテムを購入，もしくはショップを出る
	def print_use_item():
		引数:プレイヤー
		戻り値:なし
		# プレイヤーのステータスを表示する
		# アイテムの情報（名前，所持数，説明）を表示する
		# 選択されているアイテムを表示する
	def use_item():
		引数:プレイヤー，押されたキー
		戻り値:exitでアイテム使用画面から抜け出す
		# Up, Downキーでアイテムを選択
		# Returnキーでアイテムを使用，もしくは抜け出す
	def event_run():
		引数:プレイヤー
		戻り値:なし
		# イベントを実行する
	
```
