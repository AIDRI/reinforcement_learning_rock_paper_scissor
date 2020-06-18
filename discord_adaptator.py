import discord
import time


class Bot(discord.Client):
	def __init__(self):
		super().__init__()
		self.input_ = ""
		self.num_it = 0
		self.num_match = 0
		self.match_start = False


	async def on_ready(self):
		print("Logged in as ")
		print(self.user.name)
		print(self.user.id)
		print('--------')

	async def on_message(self, message):
		if (message.author == self.user):
			return
		if (message.content.startswith("!launch")):
			self.match_start = True
			if(self.num_match == 0):
				self.num_match=1
			else:
				self.num_match=0
		if (message.content.startswith("P") or message.content.startswith("R") or message.content.startswith("S") and self.match_start == True):
			self.input_ = message.content[0]
			if(self.num_it == 0):
				self.num_it=1
			else:
				self.num_it=0
			print(self.input_)
			print(self.num_it)
			with open("markov.txt", "w+") as f:
				f.write(self.input_ + str(self.num_it) + str(self.num_match))

		if (message.content.startswith("S") or message.content.startswith("P") or message.content.startswith("R") and self.match_start == True):
			time.sleep(0.3)
			with open("response.txt", "r") as s:
				for line in s:
					line = line
			await message.channel.send(str(line))

		if self.num_it == 20:
			self.match_start = False
			self.num_it = 0
			await message.channel.send(str("End, please use !start another time to play"))

if __name__ == "__main__":
	bot = Bot()
	bot.run("NzIwMzY2MTg4NzQ3ODE3MDEx.XuE7cQ.PP4nayoqee1POZQ3_NiOAXv6Pmw")
	print(self.input)
