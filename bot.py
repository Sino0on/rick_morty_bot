import json
import requests
from pprint import pprint as pp
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

tg_bot_token = '5035371106:AAGMYWUfSbwlqCn2La8WAA5OxrQ5UJrDeoE'
bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)
markup = InlineKeyboardMarkup()

# new_list = []
# for i in range(1, 43):
#     r = requests.get(f'https://rickandmortyapi.com/api/characters?page={i}')
#     data = r.json()
#     new_list.append(data)



# with open('dass.json', 'w') as f:
#     json.dump(new_list, f)
with open('characters.json', 'r') as f:
    das = json.load(f)

char = 0
page = 0

@dp.message_handler(commands=['next'])
async def next(message: types.Message):
    global char
    global page
    if page != 42:
        char += 10
        if char == 20:
            char = 0

            page += 1
        await start_command(message=message)
    else:
        await start_command(message=message)

@dp.message_handler(commands=['prev'])
async def prev(message: types.Message):
    global char
    global page
    if page != 0:
        page -= 1
    else:
        char = 0
        await start_command(message=message)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    markup = InlineKeyboardMarkup(row_width=2)
    for i in range(char, char + 10):
        print(i, page, char)
        inline_btn_1 = InlineKeyboardButton(das[page]['results'][i]['name'], callback_data=f'{i}')
        markup.add(inline_btn_1)
    print(' ')
    inline_btn_next = InlineKeyboardButton('Next', callback_data='next')
    inline_btn_prev = InlineKeyboardButton('Prev', callback_data='prev')
    markup.add(inline_btn_prev, inline_btn_next)
    await message.reply("A chto", reply_markup=markup)
#
@dp.callback_query_handler()
async def process_callback(call: types.CallbackQuery):
    if call.data in [f'{i}' for i in range(42)]:
        caption = f'''
        fullname - {das[page]['results'][int(call.data)]['name']}
        status - {das[page]['results'][int(call.data)]['status']}
        species - {das[page]['results'][int(call.data)]['species']}
        type - {das[page]['results'][int(call.data)]['type']}
        gender - {das[page]['results'][int(call.data)]['gender']}
                                                        '''
        await bot.send_photo(chat_id=call.from_user.id, photo=das[page]['results'][int(call.data)]['image'], caption=caption)
    if call.data == 'next':
        await next(message=call.message)
    elif call.data == 'prev':
        await prev(message=call.message)

if __name__ == '__main__':
    executor.start_polling(dp)