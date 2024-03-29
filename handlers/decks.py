from aiogram import types, Dispatcher

import kb
import time
from state import UserState


async def deck1(msg: types.Message):
    if msg.text == 'Аллегории':
        await UserState.allegorii.set()
    elif msg.text == 'Радости внутреннего ребенка':
        await UserState.radost.set()
    elif msg.text == 'Внутренние страхи':
        await UserState.strah.set()
    await msg.answer(
        'Правильно сформулированный запрос - ключевой момент в работе с МАК-картами. В нем уже содержится часть ответа. Я подготовила инструкцию, чтобы помочь тебе в этом',
        reply_markup=kb.tg)
    time.sleep(5)
    await msg.answer('Если ты хочешь попробовать самостоятельно, можешь продолжить вместе с ботом',
                     reply_markup=kb.s_botom1)

async def s_botom_1_handler1(callback:types.CallbackQuery):
    await UserState.strah2.set()
    await callback.message.answer('Важно адресовать запрос в отношении себя и своих чувств, не затрагивая действия и чувства других людей')
    await callback.message.answer(
        f'Пример:\n<i>Что я чувствую?\nЗачем мне эта работа?\nЧто я могу сделать, чтобы стать счастливее?</i>',
        parse_mode='HTML')
    await callback.message.answer('Если хочешь сохранить запрос только для себя, можешь не отправлять его в чат',
                                  reply_markup=kb.zhelanie)

async def s_botom_1_handler3(callback:types.CallbackQuery):
    await UserState.radost2.set()
    await callback.message.answer('Важно адресовать запрос в отношении себя и своих чувств, не затрагивая действия и чувства других людей')
    await callback.message.answer(
        f'Пример:\n<i>Что я чувствую?\nЗачем мне эта работа?\nЧто я могу сделать, чтобы стать счастливее?</i>',
        parse_mode='HTML')
    await callback.message.answer('Если хочешь сохранить запрос только для себя, можешь не отправлять его в чат',
                                  reply_markup=kb.zhelanie)

async def s_botom_1_handler4(callback:types.CallbackQuery):
    await UserState.allegorii2.set()
    await callback.message.answer('Важно адресовать запрос в отношении себя и своих чувств, не затрагивая действия и чувства других людей')
    await callback.message.answer(
        f'Пример:\n<i>Что я чувствую?\nЗачем мне эта работа?\nЧто я могу сделать, чтобы стать счастливее?</i>',
        parse_mode='HTML')
    await callback.message.answer('Если хочешь сохранить запрос только для себя, можешь не отправлять его в чат',
                                  reply_markup=kb.zhelanie)

def register_handler_decks(dp: Dispatcher):
    dp.register_message_handler(deck1, text=['Аллегории', 'Радости внутреннего ребенка', 'Внутренние страхи'], state=UserState.select_deck)
    dp.register_callback_query_handler(s_botom_1_handler1, text='С ботом1', state=UserState.strah)
    dp.register_callback_query_handler(s_botom_1_handler3, text='С ботом1', state=UserState.radost)
    dp.register_callback_query_handler(s_botom_1_handler4, text='С ботом1', state=UserState.allegorii)