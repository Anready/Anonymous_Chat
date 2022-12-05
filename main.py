import telebot
from telebot import types
from itertools import groupby
'''


API_TOKEN = '5501074235:AAEQ1TNisX8SPGDVK70NOOtuiJ3Le8qCEEQ'

bot = telebot.TeleBot(API_TOKEN)
bot = Bot(token =' ') 
dispatcher - Dispatcher(bot=bot)
'''

all = []

waiting_rooms = set()
chat_rooms = {}
photo_id =''
admin = 0
API_TOKEN = '5501074235:AAEQ1TNisX8SPGDVK70NOOtuiJ3Le8qCEEQ'

bot = telebot.TeleBot(API_TOKEN)
token = '5501074235:AAEQ1TNisX8SPGDVK70NOOtuiJ3Le8qCEEQ'


@bot.message_handler(commands=['start'])
def cmd_random(message):
    my_user_id = message.from_user.id
    all.append(my_user_id)
    new_x = [el for el, _ in groupby(all)]
    bot.send_message(chat_id=-1001608937428, text=f'В боте Анонимный чат новый пользователь, теперь их {len(new_x)}')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Qanhack", url="https://t.me/qanhack"))
    keyboard.add(types.InlineKeyboardButton(text="О боте", callback_data="button2"))
    keyboard.add(types.InlineKeyboardButton(text="Проверить", callback_data="button1"))

    bot.send_message(chat_id=my_user_id, text="Привет! Ты находишься в Анонимном чате. Чтобы продолжить подпишись на этот канал (Создано Anready)", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    my_user_id = call.from_user.id
    if call.data == "button1":
        statuss = ['creator', 'administrator', 'member']
        user_status = str(bot.get_chat_member(chat_id='@qanhack', user_id=call.from_user.id).status)
        if user_status in statuss:
            bot.send_message(chat_id=my_user_id, text="/next — искать нового собеседника \n /stop — закончить диалог")
        else:
            bot.send_message(my_user_id, 'Ты не подписан!')
    if call.data == "button2":
        bot.send_message(chat_id=my_user_id, text="О боте: \nДоброго времени суток! На связи Anready, создатель бота Анониный чат.\nКроме этого бота у мен есть еще пару, а также я создаю мобильные приложения \nПо рекламе сюда: @anredyx_bot \nОстальные боты:\nУзнать gps по ip: @gps_from_ip_bot")
    
@bot.message_handler(commands=['next'])
def join_room(message):
    my_user_id = message.from_user.id

    statuss = ['creator', 'administrator', 'member']
    user_status = str(bot.get_chat_member(chat_id='@qanhack', user_id=message.from_user.id).status)
    if user_status in statuss:
      try:
         another_user_id = waiting_rooms.pop()
         chat_rooms[another_user_id] = my_user_id
         chat_rooms[my_user_id] = another_user_id

         bot.send_message(chat_id=my_user_id, text="Собеседник найден!")
         bot.send_message(chat_id=another_user_id, text="Собеседник найден!")
      except KeyError:
        waiting_rooms.add(my_user_id)
        bot.send_message(chat_id=my_user_id, text="Идет подбор собеседника")
    else:
        bot.send_message(my_user_id, 'Ты не подписан на канал!')
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Qanhack", url="https://t.me/qanhack"))
        keyboard.add(types.InlineKeyboardButton(text="Проверить", callback_data="button1"))
        bot.send_message(chat_id=my_user_id, text="Чтобы продолжить подпишись на этот канал",reply_markup=keyboard)

@bot.message_handler(commands=['stop'])
def leave_room_handler(message):
    my_user_id = message.from_user.id
    try:
      another_user_id = chat_rooms[my_user_id]
      del chat_rooms[my_user_id], chat_rooms[another_user_id]
      bot.send_message(chat_id=another_user_id, text="Твой собоеседник завершил беседу")
      bot.send_message(chat_id=my_user_id, text="Ты завершил беседу")
    except KeyError:
      bot.send_message(chat_id=my_user_id, text="Ты сейчас не переписывайшся, напиши /next чтобы начать")


@bot.message_handler(content_types=['photo'])
def send_photo(message):
        my_user_id = message.from_user.id
        if admin==0:
         try:
             photo_id = message.photo[-1].file_id
             bot.send_photo(chat_id=chat_rooms[my_user_id], photo=photo_id, caption="")
             bot.send_message(chat_id=chat_rooms[my_user_id], text=message.text)
         except KeyError:
             bot.send_message(chat_id=my_user_id, text="Ты сейчас не переписывайшся, напиши /next чтобы начать")
        else:
            glob(message.photo[-1].file_id)
            mess1 = f'Отправьте описание к фото'
            bot.send_message(message.chat.id, mess1, parse_mode='html')
            glo1(1)
            glo(0)

@bot.message_handler(content_types=["sticker"])
def send_sticker(message):
    # Получим ID Стикера
    sticker_id = message.sticker.file_id
    my_user_id = message.from_user.id
    try:
        bot.send_sticker(chat_rooms[my_user_id], sticker_id)
    except KeyError:
        bot.send_message(chat_id=my_user_id, text="Ты сейчас не переписывайшся, напиши /next чтобы начать")
@bot.message_handler(commands=['?K5&7z{wk&YT7fR41WES,z$zfeNEgPct6LUFuhc$'])
def callback_worker(message):
    glo(1)
    user_id = message.chat.id
    bot.send_message(user_id, 'Отправьте фото', parse_mode='html')



@bot.message_handler(content_types=["video"])
def send_photo(message):
  my_user_id = message.from_user.id
  try:
      document_id = message.video.file_id
      file_info = bot.get_file(document_id)
      path = f'Собеседник отправил видео большого размера! Вот ссылка на его скачивание: \nhttp://api.telegram.org/file/bot{token}/{file_info.file_path}'
      bot.send_message(chat_rooms[my_user_id], path)
  except KeyError:
      bot.send_message(chat_id=my_user_id, text="Ты сейчас не переписывайшся, напиши /next чтобы начать")
@bot.message_handler(content_types=["audio"])
def send_photo(message):
  my_user_id = message.from_user.id
  try:
      document_id = message.audio.file_id
      file_info = bot.get_file(document_id)
      path = f'Собеседник отправил аудио-файл большого размера! Вот ссылка на его скачивание: \nhttp://api.telegram.org/file/bot{token}/{file_info.file_path}'
      bot.send_message(chat_rooms[my_user_id], path)
  except KeyError:
      bot.send_message(chat_id=my_user_id, text="Ты сейчас не переписывайшся, напиши /next чтобы начать")
@bot.message_handler(content_types=["document"])
def send_photo(message):
  my_user_id = message.from_user.id
  try:
      document_id = message.document.file_id
      file_info = bot.get_file(document_id)
      path = f'Собеседник отправил документ большого размера! Вот ссылка на его скачивание: \nhttp://api.telegram.org/file/bot{token}/{file_info.file_path}'
      bot.send_message(chat_rooms[my_user_id], path)
  except KeyError:
      bot.send_message(chat_id=my_user_id, text="Ты сейчас не переписывайшся, напиши /next чтобы начать")
@bot.message_handler()
def chat_room_message_handler(message):
    my_user_id = message.from_user.id
    if g == 0:
     try:
      bot.send_message(chat_id=chat_rooms[my_user_id], text=message.text)
     except KeyError:
      bot.send_message(chat_id=my_user_id, text="Ты сейчас не переписывайшся, напиши /next чтобы начать")
    else:
        global opis
        opis= message.text
        bot.send_message(message.chat.id, "Отправлено успешно!", parse_mode='html')
        glo1(0)
        new_x = [el for el, _ in groupby(all)]
        for i in range(len(new_x)):
            bot.send_photo(all[i], photo_id, caption=opis)

def glo1(i):
    global g
    g = i
def glo(i):
    global admin
    admin = i
def glob(i):
    global photo_id
    photo_id = i

bot.polling(none_stop=True)