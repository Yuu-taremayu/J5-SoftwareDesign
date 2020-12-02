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
 - プレイ人数 (2人～4人).
	 - 初期位置はフィールドの端.
 - 勝利条件
	 - プレイヤーがゲームをクリアするには,任意の条件を満たしている必要がある.
	 - 条件はゲーム開始時にプレイヤーごとに割り振られる.
 - イベント
	 - フィールドが初期化されるとイベントも同時に初期化される.

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
 - class "ゲーム"
```
class GAME():
	def __init__():
		argument:self, width, height, root
		return value:none
		# initialize some constant and variables in GAME class
		# initialize keyboard config
		# call start_menu() function
	def key_pressed()
		argument:event
		return value:none
		# when key pressed, call this function
		# add pressed key from array
	def key_released()
		argument:event
		return value:none
		# when key released, call this function
		# delete released key from array
	def start_menu()
		argument:none
		return value:0
		# display start menu
		# create menu screen by canvas and label
		# control Up, Down and Enter key
		# you can be Game Start or Exit here
	def select_menu()
		argument:none
		return value:0
		# display select manu
		# create menu screen by some label
		# control Up, Down, Left, Right and Enter key
		# you can be select the number of player and start game
```
 - class "プレイヤー"
```
class PLAYER():
	def __init__():
		argument:none
		return value:none
		# initialize player's status
		# money, muscle, stress, job, DEX
		# give player win condition
		# call decide_job and give player job
	def decide_job():
		argument:none
		return value:none
		# decide job by random
		# there are 4 jobs 'Teacher', 'Engineer', 'SportsMan' and 'Nojob'
```
 - class "フィールド"
```
class FIELD():
	def __init__():
		argument:none
		return value:none
		# initialize field properties
		# x, y, number of shop, number of job change point and field array
	def set_field():
		argument:none
		return value:x, y
		# setting　field size x, y
	def set_events()
		argument:none
		return:number of shop, number of job change point
		# setting number of event point shop and job change
	def init_field():
		argument:x, y, number of shop, number of job change point
		return:field array
		# initialize internal information of field
		# random create point of shop and jobchange
		# other points initialized by 'Normal'
```
