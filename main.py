from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, input_message_content
import urllib.request
import json

API_TOKEN = '5956594818:AAEp9BGUz_gVAYnCak5BEyhviLDHJEvLvVA'


bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text="Лиса")
b2 = KeyboardButton(text="Волк")
b3 = KeyboardButton(text="Медведь")
b4 = KeyboardButton(text="Заяц")
kb.add(b1, b2, b3, b4)

source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=rostov-on-don&units=metric&appid=6ea7eea1022f91ef7b34b0fbe48c4772').read()


list_of_data =json.loads(source)

data ={
'city':'rostov-on-don',
'country_code':str(list_of_data['sys']['country']),
'cor':str(list_of_data["coord"]["lon"])+" "+str(list_of_data["coord"]["lat"]),
'temp':str(list_of_data["main"]['temp']),
'pressure':str(list_of_data['main']["pressure"]),
'Pogoda':str(list_of_data["weather"][0]['main']),
'Opisanie':str(list_of_data["weather"][0]['description']),
'Skorost vetra': str(list_of_data['wind']['speed']),
'temp_max': str(list_of_data['main']['temp_max']),
'temp_min': str(list_of_data['main']['temp_min'])}


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(text="Privet, napishi /help")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply(text="/animals - vibor zhivotnogo\n"
                             "/weather - pogoda v regione")

@dp.message_handler(commands=['animals'])
async def send_welcome(message: types.Message):
    await message.reply(text="Vibiri zhivotnogo", reply_markup=kb)

@dp.message_handler(commands=['weather'])
async def send_welcome(message: types.Message):
    await message.answer(data)

@dp.message_handler(text='Лиса')
async def lisa(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id, photo="https://fanibani.ru/images/wp-content/uploads/2021/05/image047-2-968x720.jpg", reply_markup=kb)

@dp.message_handler(text='Волк')
async def lisa(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id, photo="https://icdn.lenta.ru/images/2018/12/17/15/20181217150622168/square_320_046bf3cec475de2a9f71e5be6e6077c4.jpg", reply_markup=kb)

@dp.message_handler(text='Медведь')
async def lisa(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id, photo="https://s9.travelask.ru/uploads/post/000/017/495/main_image/full-5f3da4078042c2a7eb07684a7f55b232.jpg", reply_markup=kb)

@dp.message_handler(text='Заяц')
async def lisa(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id, photo="https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Lepus_europaeus_%28Causse_Méjean%2C_Lozère%29-cropped.jpg/275px-Lepus_europaeus_%28Causse_Méjean%2C_Lozère%29-cropped.jpg", reply_markup=kb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)