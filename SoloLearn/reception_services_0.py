# -*- coding: utf-8 -*-
"""
Created by AnonymouS at 11/28/2019
"""
def reception_service():
	print('您好，欢迎来到古灵阁，请问您需要帮助吗？')
	answer = input("Y.需要 N.不需要 :")
	question()

def question():
	print('您好，欢迎来到古灵阁，请问您需要帮助吗？')
	answer = input("Y.需要 N.不需要 :")

	if answer == "Y":

		print('请问您需要什么帮助?')
		answer_2 = input('1--存取款；2--货币兑换；3--咨询 :')

		if answer_2 == "1":
			print('推荐你去存取款窗口')

		elif answer_2 == "2":
			print('金加隆和人民币的兑换率为1:51.3，即 一金加隆 = 51.3人民币')
			exchange = float(input('请问你需要兑换多少金加隆'))
			print(f'好的，我知道了，您需要兑换{exchange}金加隆')
			print(f'那么，您需要付给我 {exchange * 51.3} 人民币。')

		elif answer_2 == "3":
			print('推荐你去咨询窗口')

		else:
			print('请输入正确的数字')
			question()

	else:
		reception_service()


reception_service()
