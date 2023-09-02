from state import UserState
from aiogram import types, Dispatcher
from create_bot import bot
import kb, time

async def main_line(msg: types.Message):
    global them
    them = msg.text
    await UserState.select_deck.set()
    await msg.answer('Выбери колоду', reply_markup=kb.decks)
    await msg.answer('📍Колода «Радости внутреннего ребенка» помогает услышать истинные желания\n\n📍Колода «Внутренние страхи» помогает понять, что тебе мешает, тормозит или ограничивает в достижении целей\n\n📍Колода «Аллегории» - универсальная колода')

async def answer_yes_no(msg:types.Message):
    await UserState.estination.set()
    if msg.text == 'Да':
        await msg.answer('Я рада, что бот помог тебе!')
        if them == 'Финансы':
            await bot.send_video_note(msg.from_user.id, video_note='DQACAgIAAxkBAAIZyWTzJKMh3gyr5FRAshxTG5eUEahIAAIxMQACWgiBS9COFbzd8y4jMAQ')
            time.sleep(5)
            await msg.answer('Пожалуйста, оцени бота. Это нужно для его улучшения', reply_markup=kb.estination)
        elif them == 'Отношения':
            await bot.send_video_note(msg.from_user.id, video_note='DQACAgIAAxkBAAIZ0WTzJKM1L0IItaqYpOae0tncwMtoAAKBMQACWgiBSw3Sb9SI2HY-MAQ')
            time.sleep(5)
            await msg.answer('Пожалуйста, оцени бота. Это нужно для его улучшения', reply_markup=kb.estination)
        elif them == 'Здоровье':
            await bot.send_video_note(msg.from_user.id, video_note='DQACAgIAAxkBAAIZzWTzJKOEgG5EQY9ANLZSOcR6DIw0AAJgMQACWgiBSwpIfj7jXNEaMAQ')
            time.sleep(5)
            await msg.answer('Пожалуйста, оцени бота. Это нужно для его улучшения', reply_markup=kb.estination)
        elif them == 'Реализация':
            await bot.send_video_note(msg.from_user.id, video_note='DQACAgIAAxkBAAIZz2TzJKOznjLsvDdWENBVua-43tqsAAJmMQACWgiBS7lln0x0iVzwMAQ')
            time.sleep(5)
            await msg.answer('Пожалуйста, оцени бота. Это нужно для его улучшения', reply_markup=kb.estination)
        elif them == 'Состояние':
            await bot.send_video_note(msg.from_user.id, video_note='DQACAgIAAxkBAAIZy2TzJKNlgWyV1JA7_0_A-w_s0EocAAJJMQACWgiBSyYKBKPQ8GAcMAQ')
            time.sleep(5)
            await msg.answer('Пожалуйста, оцени бота. Это нужно для его улучшения', reply_markup=kb.estination)

    elif msg.text == 'Нет':
        await msg.answer('Сожалею, что бот не помог разобраться с волнующим запросом. Такое бывает, возможно, тебе стоит поразмыслить над самим запросом, действительно ли он главный для тебя сейчас? Если ты чувствуешь трудности с формулировкой запроса или трактовкой карты, то приглашаю тебя на консультацию, на которой мы подробно разберем твою ситуацию.',
                         reply_markup=kb.ocenka)
        time.sleep(2)
        await msg.answer('Пожалуйста, оцени бота. Это нужно для его улучшения', reply_markup=kb.estination)

def register_handler_thems_and_answer_your_question(dp:Dispatcher):
    dp.register_message_handler(answer_yes_no, state = UserState.question7, text = ['Да', 'Нет'])
    dp.register_message_handler(main_line, text=['Финансы', 'Отношения', 'Здоровье', 'Реализация', 'Состояние'], state=UserState.thems)