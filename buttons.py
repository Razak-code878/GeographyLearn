from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Реки🌊", callback_data="river"),
     InlineKeyboardButton(text="Виды водных объектов⛲", callback_data="ver_obj"),
     InlineKeyboardButton(text="Климатические пояса☀️", callback_data="climatic_zone")],
    [InlineKeyboardButton(text="Геохронология🦕", callback_data="geochronology"),
     InlineKeyboardButton(text="Часовые зоны⏰", callback_data="Hours")]

])

river_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Начало/Конец🛥️", callback_data="beg_end"),
    InlineKeyboardButton(text="Режим рек", callback_data="river_regime")],
    [InlineKeyboardButton(text="Тип питания", callback_data="river_feed"),
    InlineKeyboardButton(text="По протеканию", callback_data="flows")],
    [InlineKeyboardButton(text="Назад", callback_data="Back")]

])

Hours_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Что это?✈️", callback_data="Whatis")],
    [InlineKeyboardButton(text="Формула для нахождения", callback_data="formula")]
])


