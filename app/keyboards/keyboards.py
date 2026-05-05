from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="➡️Открыть каталог⬅️", callback_data="catalog")],
])

about = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Назад")]],
    resize_keyboard=True)


catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='НОВИНКИ🆕', callback_data="new_catalog")],
    [InlineKeyboardButton(text='Одноразовые системы', callback_data="disposable_catalog")],
    [InlineKeyboardButton(text='Жевательный табак (снюс)', callback_data="snus_catalog")],
    [InlineKeyboardButton(text='Никотиновые пластины (ватки)', callback_data="plastin_catalog")],
    [InlineKeyboardButton(text='Жидкости', callback_data="liquids_catalog")],
    [InlineKeyboardButton(text='POD-системы', callback_data="pod_catalog")],
    [InlineKeyboardButton(text='Аксессуары для POD-систем', callback_data="aces_pod_catalog")],
    [InlineKeyboardButton(text='← Главная', callback_data="first")],
])


disposable_catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='DUALL', callback_data="duall_catalog")],
    [InlineKeyboardButton(text='ELF BAR', callback_data="elfbar_catalog")],
    [InlineKeyboardButton(text='GANG', callback_data="gang_catalog")],
    [InlineKeyboardButton(text='GEEK BAR', callback_data="geekbar_catalog")],
    [InlineKeyboardButton(text='HQD', callback_data="hqd_catalog")],
    [InlineKeyboardButton(text='LOST MARY', callback_data="mary_catalog")],
    [InlineKeyboardButton(text='PAFOS', callback_data="pafos_catalog")],
    [InlineKeyboardButton(text='PLONQ', callback_data="plonq_catalog")],
    [InlineKeyboardButton(text='PUFFMI', callback_data="puffmi_catalog")],
    [InlineKeyboardButton(text='WAKA', callback_data="waka_catalog")],
    [InlineKeyboardButton(text='⬅ Вернуться', callback_data="exit_catalog")],
])


snus_catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='ARQA', callback_data="arqa_catalog")],
    [InlineKeyboardButton(text='BJORN', callback_data="bjorn_catalog")],
    [InlineKeyboardButton(text='CORVUS', callback_data="corvus_catalog")],
    [InlineKeyboardButton(text='DRYMOST', callback_data="drymost_catalog")],
    [InlineKeyboardButton(text='FEDRS', callback_data="fedrs_catalog")],
    [InlineKeyboardButton(text='ICEBERG', callback_data="iceberg_catalog")],
    [InlineKeyboardButton(text='KASTA', callback_data="kasta_catalog")],
    [InlineKeyboardButton(text='LYFT', callback_data="lyft_catalog")],
    [InlineKeyboardButton(text='ODENS', callback_data="odens_catalog")],
    [InlineKeyboardButton(text='ГРЕХ', callback_data="greh_catalog")],
    [InlineKeyboardButton(text='⬅ Вернуться', callback_data="exit_catalog")],
])


pod_catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='BRUSKO', callback_data="brusko_catalog")],
    [InlineKeyboardButton(text='GEEK VAPE', callback_data="geekvape_catalog")],
    [InlineKeyboardButton(text='PASITO', callback_data="pasito_catalog")],
    [InlineKeyboardButton(text='PLONQ', callback_data="plonq1_catalog")],
    [InlineKeyboardButton(text='SMOANT KNIGHT', callback_data="smoantknight_catalog")],
    [InlineKeyboardButton(text='VAPORESSO', callback_data="vaporesso_catalog")],
    [InlineKeyboardButton(text='VOOPOO', callback_data="voopoo_catalog")],
    [InlineKeyboardButton(text='⬅ Вернуться', callback_data="exit_catalog")],
])


liquids_catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='CATSWILL', callback_data="cats_catalog")],
    [InlineKeyboardButton(text='DUALL', callback_data="duall1_catalog")],
    [InlineKeyboardButton(text='FUMMO', callback_data="fummo_catalog")],
    [InlineKeyboardButton(text='GANG', callback_data="gang1_catalog")],
    [InlineKeyboardButton(text='INFLAVE', callback_data="inflave_catalog")],
    [InlineKeyboardButton(text='PODONKI', callback_data="podonki_catalog")],
    [InlineKeyboardButton(text='RICK AND MORTY', callback_data="morty_catalog")],
    [InlineKeyboardButton(text='САМОУБИЙЦА', callback_data="suicide_catalog")],
    [InlineKeyboardButton(text='⬅ Вернуться', callback_data="exit_catalog")],
])





























aces_pod_catalog = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text='⬅ Вернуться', callback_data="exit_catalog")],
])


exit_catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='⬅ Вернуться', callback_data="catalog")],
])


def product_keyboard(index: int, total: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Написать менеджеру →",
                url="https://t.me/lrerr2"
            )
        ],
        [
            InlineKeyboardButton(text="←", callback_data="nav:prev"),
            InlineKeyboardButton(text=f"{index + 1}/{total}", callback_data="noop"),
            InlineKeyboardButton(text="→", callback_data="nav:next"),
        ],
        [
            InlineKeyboardButton(text="В меню", callback_data="menu"),
        ],
    ])


