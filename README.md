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

The name is "Field Search Record \~凄録\~"

## Rule
 - 4\*5 Field
 - you can move Up,Down,Left,Right or stay only dice number
 - you should use events and satisfy win condition, you can win through.
 - player (2-4)
	 - initial position is corner of field.
 - win condition
	 - you have to satisfy any condition if you want to clear the game.
	 - when the game start, you get a condition.
 - event
	 - shop
		 - placed on field
		 - you can get items by spend player status money
	 - job change
		 - placed on field
		 - you can change given job
	 - work
		 - increase or decrease money
		 - increase stress

## Extraction of materials
 - player
	 - status
		 - money
		 - muscle
		 - stress
		 - dexterity
	 - job
		 - teacher
		 - enginner
		 - sports man
		 - no job
	 - win condition
 - field
	 - event
		 - shop
		 - job change
		 - work
 - dice
 - item
	 - protain
	 - energy drink

## Behiviour of materials
 - player
	 - moving Up,Down,Left,Right on field
	 - shopping and changing job in field
 - field
	 - placed on display, and provide field that player move
	 - player can earn money, shop items and change job here
 - dice
	 - put out 1~6 and effect player action
 - item
	 - effects player's status

## Data structure
 - class "game"
```
class GAME():
	self.WIDTH		:variable of display width, passed from main function
	self.HEIGHT		:variable of display height, passed from main function
	self.MAG		:variable of display magnification, passed from main function
	self.root		:instance for treating Tkinter
	self.scene_cnt		:value of game display status
	self.goal_order		:array for storing goal order
	self.var_start_menu	:list save data of start_menu function
	self.var_select_menu	:list save data of select_menu function
	self.frame		:instance for creating frame
	self.pressed		:array storing pressed key
	canvas			:instance for drawing display
	self.field		:instance of field inner status
	self.player		:instance array of player inner status
	self.turn		:flag that indicates active player
	self.old_turn		:old flag that indicates active player
```
 - class "player"
```
class PLAYER():
	self.x			:variable of player x coordinate
	self.y			:variable of player y coordinate
	self.money		:variable of player money status
	self.muscle		:variable of player muscle status
	self.stress		:variable of player stress status
	self.job		:variable of player job
	self.condition		:variable of player win condition
	self.goal_flag		:variable of player goal flag
	self.bad_event		:variable of player bad event
	self.item_num		:variable of player number of item it has
	self.item		:array of item player has
```
 - class "field"
```
class FIELD():
	self.x			:variable of player x coordinate
	self.y			:variable of player y coordinate
	self.WIDTH		:variable of display width, passed from main function
	self.HEIGHT		:variable of display height, passed from main function
	self.MAG		:variable of display magnification, passed from main function
	self.num_shop		:variable of the number of shop
	self.num_jobchange	:variable of the number of jobchange
	self.num_work		:variable of the number of work
	self.shop_flag		:flag that player on the shop
	self.useitem_flag	:flag that player useing item
	self.select_flag	:flag that player selecting item
	self.cantbuy_flag	:flag that when player buy item
	self.donthave_flag	:flag that when player use item
```

## Function specification
### Basic data structure
 - class "game"
```
class GAME():
	self.WIDTH		:variable of display width, passed from main function
	self.HEIGHT		:variable of display height, passed from main function
	self.MAG		:variable of display magnification, passed from main function
	self.root		:instance for treating Tkinter
	self.scene_cnt		:value of game display status
	self.goal_order		:array for storing goal order
	self.var_start_menu	:list save data of start_menu function
	self.var_select_menu	:list save data of select_menu function
	self.frame		:instance for creating frame
	self.pressed		:array storing pressed key
	canvas			:instance for drawing display
	self.field		:instance of field inner status
	self.player		:instance array of player inner status
	self.turn		:flag that indicates active player
	self.old_turn		:old flag that indicates active player
```
 - class "player"
```
class PLAYER():
	self.x			:variable of player x coordinate
	self.y			:variable of player y coordinate
	self.money		:variable of player money status
	self.muscle		:variable of player muscle status
	self.stress		:variable of player stress status
	self.job		:variable of player job
	self.condition		:variable of player win condition
	self.goal_flag		:variable of player goal flag
	self.bad_event		:variable of player bad event
	self.item_num		:variable of player number of item it has
	self.item		:array of item player has
```
 - class "field"
```
class FIELD():
	self.x			:variable of player x coordinate
	self.y			:variable of player y coordinate
	self.WIDTH		:variable of display width, passed from main function
	self.HEIGHT		:variable of display height, passed from main function
	self.MAG		:variable of display magnification, passed from main function
	self.num_shop		:variable of the number of shop
	self.num_jobchange	:variable of the number of jobchange
	self.num_work		:variable of the number of work
	self.shop_flag		:flag that player on the shop
	self.useitem_flag	:flag that player useing item
	self.select_flag	:flag that player selecting item
	self.cantbuy_flag	:flag that when player buy item
	self.donthave_flag	:flag that when player use item
```

### Basic function specification
 - class "game"
```
class GAME():
	def __init__():
		argument:self, w, h, mag, root
		return value:none
		# initialize some constant and variables in GAME class
		# create canvas instance
		# create player instance
		# initialize keyboard config
		# call start_menu() function
	def key_pressed():
		argument:self, event
		return value:none
		# when key pressed, call this function
		# add pressed key from array
		# branch by scene count and some flag
	def key_released():
		argument:self, event
		return value:none
		# when key released, call this function
		# delete released key from array
	def click_button():
		argument:self, l_name
		return value:none
		# when clicked by mouse, call this function
		# set focus to frame
		# set player's name
	def start_menu():
		argument:self
		return value:0
		# display start menu
		# create menu screen by canvas and label
		# control Up, Down and Enter key
		# you can be Game Start or Exit here
	def select_menu():
		argument:self
		return value:0
		# display select manu
		# create menu screen by some label
		# control Up, Down, Left, Right and Enter key
		# you can be select the number of player and start game
		# decide each player's initial position by the number of player
	def start():
		argument:self
		return value:none
		# function calling function that processing
		# control the game of the flow
		# call print_field()
		# call print_player()
		# call move_player()
		# call check_win_condition()
		# call check_exit_condition()
	def print_field():
		argument:self
		return value:none
		# print field using field instance
		# print player status using player instance
		# change the number of status display and position by the number of player
	def print_player():
		argument:self
		return value:none
		# print player's location by each coodinate
	def roll_dice():
		argument:self
		return value:dice
		# function that decide dice number using random number
		# change probability of high number by player's status
	def check_win_condition():
		argument:self
		return value:none
		# function that checking satisfy condition
		# if player satisfy conidition, put true to condition of class player
	def check_exit_condition():
		argument:self
		return value:none
		# checking function exit condition of game
		# call show_result() if all player win condition satisfy
	def move_player():
		argument:self
		return value:none
		# function that move placed player on field
		# player can move range of field
		# player can the number of moving by dice
	def show_result():
		argument:self
		return value:none
		# show grade of player
	def shop():
		argument:self, player
		return value:none
		# if player is in the shop, call this funtion
		# run shop event
		# print shop display and player can buy some items
	def item():
		argument:self, player
		return value:none
		# when each player's turn start, call this function
		# player can use items if player has items
```
 - class "player"
```
class PLAYER():
	def __init__():
		argument:self, order
		return value:none
		# initialize player's status
		# money, muscle, stress, job, dexterity
		# call decide_job and give player job
		# call decide_win_condition and give player win condition
	def decide_job():
		argument:self
		return value:none
		# decide job by random
		# there are 4 jobs 'Teacher', 'Engineer', 'SportsMan' and 'Nojob'
	def decide_win_condition()
		argument:self
		return value:none
		# decide player's win condition by random
```
 - class "field"
```
class FIELD():
	def __init__():
		argument:self, w, h, mag
		return value:none
		# initialize field properties
		# x, y, number of shop, number of job change point and field array
	def set_field():
		argument:self
		return value:x, y
		# setting field size x, y
	def set_events()
		argument:self
		return value:num_shop, num_jobchange, num_work
		# setting number of event point shop, job change and work
	def init_field():
		argument:self, x, y, num_shop, num_jobchange, num_work
		return value:field_array
		# initialize internal information of field
		# random create point of shop, jobchange and work
		# other points initialized by 'Normal'
	def event_work():
		argument:self, player
		return value:none
		# when player is in work, run this function
		# change money and stress status by job and random
		# print message
	def event_job_change():
		argument:self, player
		return value: none
		# when player is in job change, run this function
		# change job by random
		# print message
	def print_shop():
		argument:self, player
		return value:none
		# when run shop event, call this function
		# print item, item infomation nad more
	def select_shop():
		argument:self, player, pressed
		return value:0
		# if player's in shop display, call this function
		# selecting items
	def print_use_item():
		argument:self, player
		return value:none
		# when each player's turn start, call this function by item() in "game" class
		# print item that player can use it
	def use_item():
		argument:self, player
		return value:none
		# when each player's turn start, call this function by item() in "game" class
		# select and use item which player has
	def event_run():
		argument:self, player
		return value:none
		# judge whether or do not to call function by player's coodinate
```
