from aiogram import Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery

from deep_translator import GoogleTranslator

from state import Form
from aiogram.fsm.context import FSMContext

from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

markup = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='uz ➡  eng', callback_data='uz-en')],
    [InlineKeyboardButton(text='uz ➡  ru', callback_data='uz-ru')],
    [InlineKeyboardButton(text='uz ➡  tr', callback_data='uz-tr')]
])

language = {
    'uz': "O'zbekcha",
    'en': "Inglizcha",
    'ru': "Ruscha",
    'tr': "Turkcha"
}

router = Router()

@router.message(Command('choose'))
async def choose(msg: Message):
    await msg.reply(text='Kerakli tilga sozlang.', reply_markup=markup)

@router.callback_query(lambda c: c.data.startswith('uz'))
async def callback_uzb_eng(call: CallbackQuery, state: FSMContext):
    await call.answer(text="qabul qilindi ✅")
    src, dest = call.data.split('-')
    await call.message.answer(text=f"💡 {language[src]} xabar yuboring, men sizga {language[dest]} qilib qaytaraman.")
    if dest == "ru":
        await state.set_state(Form.uz_ru)
    elif dest == "en":
        await state.set_state(Form.uz_en)
    elif dest == "tr":
        await state.set_state(Form.uz_tr)

@router.message(Form.uz_tr, Command('choose'))
@router.message(Form.uz_ru, Command('choose'))
@router.message(Form.uz_en, Command('choose'))
async def uzb_eng(msg: Message, state: FSMContext):
    await msg.reply(text='Kerakli tilga sozlang.', reply_markup=markup)
    await state.clear()

@router.message(Form.uz_en)
async def uzb_eng(msg: Message, state: FSMContext):
    matn = msg.text
    tarjima = GoogleTranslator(source="uz",target='en').translate(matn)
    await state.set_state(Form.uz_en)
    await msg.reply(text=tarjima)

@router.message(Form.uz_ru)
async def uzb_eng(msg: Message, state: FSMContext):
    matn = msg.text
    tarjima = GoogleTranslator(source="uz",target='ru').translate(matn)
    await state.set_state(Form.uz_ru)
    await msg.reply(text=tarjima)

@router.message(Form.uz_tr)
async def uzb_eng(msg: Message, state: FSMContext):
    matn = msg.text
    tarjima = GoogleTranslator(source="uz",target='tr').translate(matn)
    await state.set_state(Form.uz_tr)
    await msg.reply(text=tarjima)


