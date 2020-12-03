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
 - class "player"
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
 - class "field"
```
class FIELD():
	self.x			:
	self.y			:
	self.WIDTH		:
	self.HEIGHT		:
	self.num_shop		:
	self.num_jobchange	:
```

## Function specification
 - Basic data structure
 - class "game"
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
 - class "player"
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
 - class "field"
```
class FIELD():
	self.x			:
	self.y			:
	self.WIDTH		:
	self.HEIGHT		:
	self.num_shop		:
	self.num_jobchange	:
```

 - Basic function specification
 - class "game"
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
 - class "player"
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
 - class "field"
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
