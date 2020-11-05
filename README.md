# J5-SoftwareDesign
2020 SoftwareDesgin 2
group development

## Team ｐｙてょｎ
### Members
 - Renta Noguchi (Leader)
 - Satoshi Naito
 - Reiji Yamashita
 - Tatsuya Mikami
 - Yu Miura

## Descriptions
development of Field Sugoroku with Python
The name is "日曜から夜ふかし \~Sunday midnight\~"

## Rule
 - 4\*5 Field
 - player (2-4)
	 - initial position is corner of field.
 - win condition
	 - you have to satisfy any condition if you want to clear the game.
	 - when the game start, you get a condition.
 - event
	 - when initialize field, events initialize at same time.

## Extraction of materials
 - player
	 - money
	 - muscle
	 - stress
	 - job
	 - DEX
	 - win condition
 - event
	 - shop
	 - battle
	 - job change
 - dice
 - job
	 - teacher
	 - enginner
	 - sports man
	 - no job

## Behiviour of materials

## Data structure
 - class "game"
```
class GAME():
	def __init__():
		argument:self, width, height, root
		return value:none
		# any discription
	def key_pressed()
		argument:event
		return value:none
		# any discription
	def key_released()
		argument:event
		return value:none
		# any discription
	def start_menu()
		argument:none
		return value:0
		# any discription
	def select_menu()
		argument:none
		return value:0
		# any discription
```
 - class "player"
```
class PLAYER():
	def __init__():
		argument:none
		return value:none
		# any discription
	def decide_job():
		argument:none
		return value:none
		# any discription
```
 - class "field"
```
class FIELD():
	def __init__():
		argument:none
		return value:none
		# any discription
	def set_field():
		argument:none
		return value:x, y
		# any discription
```
