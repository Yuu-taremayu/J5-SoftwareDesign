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
		 - フィールド状に配置される.
		 - プレイヤーのステータスmoneyを消費してアイテムを手に入れることができる.
	 - ジョブチェンジ
		 - フィールド状に配置される.
		 - 与えられたジョブを変更することができる.

## 物の抽出
 - プレイヤー
	 - money
	 - muscle
	 - endurance
	 - stress
	 - speed
	 - idea
	 - intelligence
	 - job
	 - status
	 - purpose
 - イベント
	 - shop
	 - battle
	 - work shop
 - ダイス
 - 職業
	 - free
	 - athlete
	 - detective
	 - doctor
	 - engineer
	 - hunter
	 - paramedic
	 - police
	 - teacher

## 物の振る舞い

## データ構造
 - "ゲーム" クラス
```
class GAME():
	self.WIDTH		:ゲーム画面の横幅を持つ変数,main関数から渡される
	self.HEIGHT		:ゲーム画面の縦幅を持つ変数,main関数から渡される
	self.MAG		:ゲーム画面の倍率を持つ変数,main関数から渡される
	self.root		:
	self.scene		:
	self.var_start_menu	:
	self.var_select_menu	:
	self.frame		:
	self.pressed		:
	canvas			:
	self.field		:フィールドの内部状態を保持するインスタンス
	self.player		:プレイヤーの内部状態を保持するインスタンスの配列
	self.turn		:現在行動するプレイヤーを指し示すフラグ
```
 - "プレイヤー" クラス
```
class PLAYER():
	self.x			:
	self.y			:
	self.money		:
	self.muscle		:
	self.stress		:
	self.dexterity		:
	self.job		:
	self.condition		:
```
 - "フィールド" クラス
```
class FIELD():
	self.x			:
	self.y			:
	self.WIDTH		:
	self.HEIGHT		:
	self.num_shop		:
	self.num_jobchange	:
```

## 関数仕様
### 基本データ構造
 - "ゲーム" クラス
```
class GAME():
	self.WIDTH		:
	self.HEIGHT		:
	self.MAG		:
	self.root		:
	self.scene		:
	self.var_start_menu	:
	self.var_select_menu	:
	self.frame		:
	self.pressed		:
	canvas			:
	self.field		:
	self.player		:
	self.turn		:
```
 - "プレイヤー" クラス
```
class PLAYER():
	self.x			:
	self.y			:
	self.money		:
	self.muscle		:
	self.stress		:
	self.dexterity		:
	self.job		:
	self.condition		:
```
 - "フィールド" クラス
```
class FIELD():
	self.x			:
	self.y			:
	self.WIDTH		:
	self.HEIGHT		:
	self.num_shop		:
	self.num_jobchange	:
```

### 基本関数仕様
 - "ゲーム" クラス
```
class GAME():
	def __init__():
		引数:self, width, height, root
		戻り値:none
		# initialize some constant and variables in GAME class
		# initialize keyboard config
		# call start_menu() function
	def key_pressed()
		引数:event
		戻り値:none
		# when key pressed, call this function
		# add pressed key from array
	def key_released()
		引数:event
		戻り値:none
		# when key released, call this function
		# delete released key from array
	def start_menu()
		引数:none
		戻り値:0
		# display start menu
		# create menu screen by canvas and label
		# control Up, Down and Enter key
		# you can be Game Start or Exit here
	def select_menu()
		引数:none
		戻り値:0
		# display select manu
		# create menu screen by some label
		# control Up, Down, Left, Right and Enter key
		# you can be select the number of player and start game
```
 - "プレイヤー" クラス
```
class PLAYER():
	def __init__():
		引数:none
		戻り値:none
		# initialize player's status
		# money, muscle, stress, job, DEX
		# give player win condition
		# call decide_job and give player job
	def decide_job():
		引数:none
		戻り値:none
		# decide job by random
		# there are 4 jobs 'Teacher', 'Engineer', 'SportsMan' and 'Nojob'
```
 - "フィールド" クラス
```
class FIELD():
	def __init__():
		引数:none
		戻り値:none
		# initialize field properties
		# x, y, number of shop, number of job change point and field array
	def set_field():
		引数:none
		戻り値:x, y
		# setting　field size x, y
	def set_events()
		引数:none
		return:number of shop, number of job change point
		# setting number of event point shop and job change
	def init_field():
		引数:x, y, number of shop, number of job change point
		return:field array
		# initialize internal information of field
		# random create point of shop and jobchange
		# other points initialized by 'Normal'
```
