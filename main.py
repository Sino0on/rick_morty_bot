DONT USE
DONT USE
DONT USE
DONT USE
DONT USE
DONT USE
DONT USE
DONT USE
DONT USE
DONT USE

# import requests
# from pprint import pprint as pp
# from aiogram import Bot, types
# from aiogram.utils import executor
# from aiogram.dispatcher import Dispatcher
# from aiogram.types import ReplyKeyboardRemove, \
#     ReplyKeyboardMarkup, KeyboardButton, \
#     InlineKeyboardMarkup, InlineKeyboardButton
#
# tg_bot_token = '5035371106:AAGMYWUfSbwlqCn2La8WAA5OxrQ5UJrDeoE'
# bot = Bot(token=tg_bot_token)
# dp = Dispatcher(bot)
#
# page = 1
# url = f'https://rickandmortyapi.com/api/character?page={page}'
# r = requests.get(url)
# character = r.json()
# markup = InlineKeyboardMarkup()
#
# for i in range(len(character['results'])):
#     inline_btn_1 = InlineKeyboardButton(character['results'][i]['name'], callback_data=f'{i}')
#     markup.add(inline_btn_1)
# inline_btn_next = InlineKeyboardButton('Next', callback_data='next')
# markup.add(inline_btn_next)
#
# for i in range(len(character['results'])):
#     pp(character['results'][i]['name'])
#
#
# @dp.message_handler(commands=['start'])
# async def start_command(message: types.Message):
#     await message.reply("A chto", reply_markup=markup)
#
#
# @dp.callback_query_handler()
# async def process_callback(call: types.CallbackQuery):
#         if call.data in [f'{i}' for i in range(len(character['results']))]:
#             await bot.edit_message_text(text = f'''
# fullname - {character['results'][int(call.data)]['name']}
# status - {character['results'][int(call.data)]['status']}
# species - {character['results'][int(call.data)]['species']}
# type - {character['results'][int(call.data)]['type']}
# gender - {character['results'][int(call.data)]['gender']}
# image - {character['results'][int(call.data)]['image']}
#                                                 ''', chat_id=call.message.chat.id,
#                                         message_id=call.message.message_id)
#         if call.data == 'next':
#             global page
#             page += 1
#             await bot.edit_message_text(text="/start", chat_id=call.message.chat.id,
#                                         message_id=call.message.message_id)
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp)
