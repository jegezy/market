from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile, InputMediaPhoto
import keyboards.keyboards as kb
from data.products import WAKA, PUFFMI, LOSTMARY, PAFOS, GANG, HQD, GEEKBAR, ELFBAR, DUALL, PLONQ
from data.products2 import BRUSKO, GEEKVAPE, PASITO, SMOANTKNIGHT, VAPORESSO, VOOPOO, NEW, PLONQ1, PLASTIN
from data.products3 import ARQA, CORVUS, DRYMOST, KASTA, LYFT, GREH, ICEBERG, BJORN, ODENS
from data.products4 import RICK, DUALL1, CATS, OGGO, SUICIDE, FUMMO, INFLAVE, GANG1, PODONKI



router = Router()


@router.message(Command('start'))
async def start(message: Message):
    await message.answer(
        "*Доброго времени суток!\n\n🤖 С помощью данного бота Вы можете ознакомиться с каталогом\n\n/about - о нас\n\nЧтобы начать, нажмите на кнопку ниже⤵️*",
        parse_mode="MARKDOWN",
        reply_markup=kb.settings)


@router.message(Command('about'))
async def about(message: Message):
    await message.answer(
        "*Мы являемся крупным оптовым поставщиком никотиновой продукции. В день через нас проходит от 100  тысяч единиц товара и более. Обычно мы работаем с сетевыми магазинами и табачными лавками напрямую, но этот бот — наш собственный розничный проект. Мы продаём товар почти по той же закупочной цене, что и для розничных точек, без наценки «чужого» посредника. Именно поэтому наш товар стоит дешевле, чем у любого розничного игрока.\n\nДополнительно важно: Вся наша продукция 100% ОРИГИНАЛЬНАЯ — мы не торгуем подделками, так как работаем напрямую с производителями, а не с «серыми» рынками.*",
        parse_mode="MARKDOWN",
        reply_markup=kb.about)


@router.message(F.text == 'Назад')
async def nazad(message: Message):
    await message.answer(
        "*Доброго времени суток!\n\n🤖 С помощью данного бота Вы можете ознакомиться с каталогом\n\n/about - о нас\n\nЧтобы начать, нажмите на кнопку ниже⤵️*",
        parse_mode="Markdown",
        reply_markup=kb.settings
    )


@router.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        "*Нажмите, чтобы открыть каталог продукции:*",
        parse_mode="MARKDOWN",
        reply_markup = kb.catalog)


@router.callback_query(F.data == 'disposable_catalog')
async def disposable_catalog(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('*Выберите:*',
    parse_mode = "MARKDOWN",
    reply_markup=kb.disposable_catalog)


@router.callback_query(F.data == 'snus_catalog')
async def snus_catalog(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('*Выберите:*',
    parse_mode = "MARKDOWN",
    reply_markup=kb.snus_catalog)


@router.callback_query(F.data == 'liquids_catalog')
async def liquids_catalog(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('*Выберите:*',
    parse_mode = "MARKDOWN",
    reply_markup=kb.liquids_catalog)


@router.callback_query(F.data == 'pod_catalog')
async def pod_catalog(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('*Выберите:*',
    parse_mode = "MARKDOWN",
    reply_markup=kb.pod_catalog)


@router.callback_query(F.data == 'exit_catalog')
async def exit_catalog(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('*Нажмите, чтобы открыть каталог продукции:*',
    parse_mode="MARKDOWN",
    reply_markup=kb.catalog)


@router.callback_query(F.data == 'first')
async def first(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        "*Доброго времени суток!\n\n🤖 С помощью данного бота Вы можете ознакомиться с каталогом\n\n/about - о нас\n\nЧтобы начать, нажмите на кнопку ниже⤵️*",
        parse_mode="MARKDOWN",
        reply_markup=kb.settings)


user_index: dict[int, int] = {}
user_products: dict[int, list] = {}  # добавь это


def product_caption(p: dict) -> str:
    return (
        f"{p['name']}\n\n"
        f"{p['size']}\n"
        f"{p['color']}\n\n"
        f"{p['description']}\n\n"
        f"{p['price']}₽"
    )


async def send_product(target, user_id: int, edit: bool, products: list = None):
    if products is not None:
        user_products[user_id] = products

    current_products = user_products.get(user_id, [])
    if not current_products:
        return

    total = len(current_products)
    index = user_index.get(user_id, 0)
    p = current_products[index]
    caption = product_caption(p)
    photo = FSInputFile(p["photo"])

    if edit and isinstance(target, CallbackQuery):
        await target.message.edit_media(
            media=InputMediaPhoto(media=photo, caption=caption),
            reply_markup=kb.product_keyboard(index, total)
        )
    else:
        msg = target if isinstance(target, Message) else target.message
        await msg.answer_photo(
            photo=photo,
            caption=caption,
            reply_markup=kb.product_keyboard(index, total)
        )


@router.callback_query(F.data == "waka_catalog")
async def show_waka_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=WAKA)


@router.callback_query(F.data == "puffmi_catalog")
async def show_puffmi_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=PUFFMI)


@router.callback_query(F.data == "mary_catalog")
async def show_mary_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=LOSTMARY)


@router.callback_query(F.data == "pafos_catalog")
async def show_pafos_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=PAFOS)


@router.callback_query(F.data == "gang_catalog")
async def show_gang_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=GANG)


@router.callback_query(F.data == "geekbar_catalog")
async def show_geekbar_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=GEEKBAR)


@router.callback_query(F.data == "hqd_catalog")
async def show_hqd_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=HQD)


@router.callback_query(F.data == "duall_catalog")
async def show_duall_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=DUALL)


@router.callback_query(F.data == "elfbar_catalog")
async def show_elfbar_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=ELFBAR)


@router.callback_query(F.data == "plonq_catalog")
async def show_plonq_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=PLONQ)


@router.callback_query(F.data == "geekvape_catalog")
async def show_geekvape_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=GEEKVAPE)


@router.callback_query(F.data == "brusko_catalog")
async def show_brusko_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=BRUSKO)


@router.callback_query(F.data == "pasito_catalog")
async def show_pasito_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=PASITO)


@router.callback_query(F.data == "smoantknight_catalog")
async def show_smoantknight_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=SMOANTKNIGHT)


@router.callback_query(F.data == "vaporesso_catalog")
async def show_vaporesso_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=VAPORESSO)


@router.callback_query(F.data == "voopoo_catalog")
async def show_voopoo_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=VOOPOO)


@router.callback_query(F.data == "plonq1_catalog")
async def show_plonq1_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=PLONQ1)


@router.callback_query(F.data == "new_catalog")
async def show_new_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=NEW)


@router.callback_query(F.data == "arqa_catalog")
async def show_arqa_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=ARQA)


@router.callback_query(F.data == "corvus_catalog")
async def show_corvus_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=CORVUS)


@router.callback_query(F.data == "drymost_catalog")
async def show_drymost_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=DRYMOST)


@router.callback_query(F.data == "kasta_catalog")
async def show_kasta_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=KASTA)


@router.callback_query(F.data == "lyft_catalog")
async def show_lyft_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=LYFT)


@router.callback_query(F.data == "greh_catalog")
async def show_greh_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=GREH)


@router.callback_query(F.data == "iceberg_catalog")
async def show_iceberg_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=ICEBERG)


@router.callback_query(F.data == "bjorn_catalog")
async def show_bjorn_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=BJORN)


@router.callback_query(F.data == "morty_catalog")
async def show_morty_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=RICK)


@router.callback_query(F.data == "duall1_catalog")
async def show_duall1_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=DUALL1)


@router.callback_query(F.data == "cats_catalog")
async def show_cats_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=CATS)


@router.callback_query(F.data == "oggo_catalog")
async def show_oggo_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=OGGO)


@router.callback_query(F.data == "suicide_catalog")
async def show_suicide_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=SUICIDE)


@router.callback_query(F.data == "fummo_catalog")
async def show_fummo_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=FUMMO)


@router.callback_query(F.data == "inflave_catalog")
async def show_inflave_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=INFLAVE)


@router.callback_query(F.data == "gang1_catalog")
async def show_gang1_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=GANG1)


@router.callback_query(F.data == "podonki_catalog")
async def show_podonki_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=PODONKI)


@router.callback_query(F.data == "plastin_catalog")
async def show_plastin_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=PLASTIN)


@router.callback_query(F.data == "odens_catalog")
async def show_odens_catalog(callback: CallbackQuery):
    await callback.answer()
    user_id = callback.from_user.id
    user_index[user_id] = 0
    await send_product(callback, user_id=user_id, edit=True, products=ODENS)
























@router.callback_query(F.data == 'aces_pod_catalog')
async def aces_pod(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        "*Данная категория продукции пока не добавлена. По вопросам наличия товара - пишите менеджеру.*",
        parse_mode="MARKDOWN",
        reply_markup = kb.aces_pod_catalog)


@router.callback_query(F.data == "nav:next")
async def nav_next(callback: CallbackQuery):
    user_id = callback.from_user.id
    products = user_products.get(user_id, [])
    user_index[user_id] = (user_index.get(user_id, 0) + 1) % len(products)
    await send_product(callback, user_id=user_id, edit=True)
    await callback.answer()


@router.callback_query(F.data == "nav:prev")
async def nav_prev(callback: CallbackQuery):
    user_id = callback.from_user.id
    products = user_products.get(user_id, [])
    user_index[user_id] = (user_index.get(user_id, 0) - 1) % len(products)
    await send_product(callback, user_id=user_id, edit=True)
    await callback.answer()


@router.callback_query(F.data == "noop")
async def noop(callback: CallbackQuery):
    await callback.answer()


@router.callback_query(F.data == "menu")
async def go_menu(callback: CallbackQuery):
    await callback.answer()
    await callback.message.delete()
    await callback.message.answer(
        text="*Нажмите, чтобы открыть каталог продукции:*",
        parse_mode="MARKDOWN",
        reply_markup=kb.catalog)


@router.message()
async def unknown_command(message: Message):
    await message.answer(
        "*Введите комманду /start*",
        parse_mode="MARKDOWN")