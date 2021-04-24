import telebot
from keyboa import Keyboa
import time

bot = telebot.TeleBot('скрыт в целях безопасности')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.from_user.id, 'Привет!😉 Я - Cирин, умная птица🕊 экскурсовод. Я могу рассказать тебе о прекрасной'
                              ' федеральной территории Сириус⛰')
    time.sleep(2)
    menu = [{"Текстовая": "txt"}, {"Голосовая": "voice"}]
    keyboard = Keyboa(items=menu, front_marker="", back_marker="").keyboard
    bot.send_message(chat_id=message.from_user.id, text="В каком формате тебе наиболее удобна экскурсия?",
                     reply_markup=keyboard)


@bot.message_handler()
def send_wtf(message):
    bot.send_message(chat_id=message.from_user.id, text='Прости, я тебя совсем не понимаю🤷‍♀️, в чате'
                                                        ' доступна только команда'
                                                        ' /start для запуска(перезапуска) бота. Поговорить'
                                                        ' не получится😞'
                                                        '- я так себе слушатель, зато рассказчик отличный📢')


@bot.callback_query_handler(func=lambda call: True)
def inline(call):
    if call.data == "txt":
        going_txt(call)
    if call.data == 'voice':
        going_voice(call)
    # texts
    if call.data == "fisht":
        fisht(call)
    if call.data == 'big_ice':
        big_ice(call)
    if call.data == 'adler':
        adler(call)
    if call.data == 'shaiba':
        shaiba(call)
    if call.data == "sirius":
        sirius(call)
    if call.data == "sirius_hotel":
        sirius_hotel(call)
    if call.data == "sirius_lyceum":
        sirius_lyceum(call)
    if call.data == "fontains":
        fontains(call)
    # voice choise
    if call.data == "going_voice_m":
        start_voice_m(call)
    if call.data == "going_voice_w":
        start_voice_w(call)
    # male_voice
    if call.data == "fisht_v_m":
        fisht_v_m(call)
    if call.data == 'big_ice_v_m':
        big_ice_v_m(call)
    if call.data == 'adler_v_m':
        adler_v_m(call)
    if call.data == 'shaiba_v_m':
        shaiba_v_m(call)
    if call.data == "sirius_v_m":
        sirius_v_m(call)
    if call.data == "sirius_hotel_v_m":
        sirius_hotel_v_m(call)
    if call.data == "sirius_lyceum_v_m":
        sirius_lyceum_v_m(call)
    # woman_voice
    if call.data == "fontains_v_w":
        fontains_v_w(call)
    if call.data == "fisht_v_w":
        fisht_v_w(call)
    if call.data == 'big_ice_v_w':
        big_ice_v_w(call)
    if call.data == 'adler_v_w':
        adler_v_w(call)
    if call.data == 'shaiba_v_w':
        shaiba_v_w(call)
    if call.data == "sirius_v_w":
        sirius_v_w(call)
    if call.data == "sirius_hotel_v_w":
        sirius_hotel_v_w(call)
    if call.data == "sirius_lyceum_v_w":
        sirius_lyceum_v_w(call)
    if call.data == "fontains_v_w":
        fontains_v_w(call)
    if call.data == "end":
        end(call)


def going_txt(callback):
    bot.send_message(chat_id=callback.message.chat.id, text="Тогда начнем, чего же ждать!")
    time.sleep(4)
    bot.send_message(chat_id=callback.message.chat.id, text="Итак, прямо сейчас ты, наверное, вышел из поезда🚅 на"
                                                            " станции Имеритинский курорт и стоишь воле этого фонтана🌊"
                                                            "")
    bot.send_photo(chat_id=callback.message.chat.id,
                   photo='https://static.tildacdn.com/tild3564-6538-4830-b364-653563643435/_2.jpg')
    time.sleep(2)
    bot.send_message(chat_id=callback.message.chat.id, text="Пусть он и станет нашей отправной точкой😉")
    time.sleep(2)
    less_go(callback)


def going_voice(callback):
    menu = [{"Мужской голос": "going_voice_m"}, {"Женский голос": "going_voice_w"}]
    keyboard = Keyboa(items=menu, front_marker="", back_marker="").keyboard
    bot.send_message(chat_id=callback.message.chat.id, text="Выбери голос экскурсовода:",
                     reply_markup=keyboard)


def start_voice_m(callback):
    voice = open(r'C:\Users\yarsl\PycharmProjects\Bot_Kyoto2\Audio\Фонтан - м.mp3', 'rb')
    bot.send_photo(chat_id=callback.message.chat.id,
                   photo='https://static.tildacdn.com/tild3564-6538-4830-b364-653563643435/_2.jpg')
    bot.send_voice(chat_id=callback.message.chat.id, voice=voice)
    time.sleep(9)
    going_voice_m(callback)


def start_voice_w(callback):
    voice = open(r'C:\Users\yarsl\PycharmProjects\Bot_Kyoto2\Audio\введение1_1.mp3', 'rb')
    bot.send_photo(chat_id=callback.message.chat.id,
                   photo='https://static.tildacdn.com/tild3564-6538-4830-b364-653563643435/_2.jpg')
    bot.send_voice(chat_id=callback.message.chat.id, voice=voice)
    time.sleep(14)
    going_voice_w(callback)


def going_voice_m(callback):
    menu = [{"Стадион «Фишт»": "fisht_v_m"}, {"Ледовый дворец «Большой»": "big_ice_v_m"},
            {'Ледовая арена «Шайба»': 'shaiba_v_m'}, {'Адлер-Арена': 'adler_v_m'},
            {'Образовательный центр Сириус': "sirius_v_m"},
            {'Отель омега Сириус': 'sirius_hotel_v_m'}, {"Сириус Лицей": 'sirius_lyceum_v_m'},
            {"Фонтаны": "fontains_v_m"}, {"Закончить экскурсию": "end"}]
    keyboard = Keyboa(items=menu, front_marker="", back_marker="").keyboard
    bot.send_message(chat_id=callback.message.chat.id, text="Про какой объект тебе рассказать?",
                     reply_markup=keyboard)


def going_voice_w(callback):
    menu = [{"Стадион «Фишт»": "fisht_v_w"}, {"Ледовый дворец «Большой»": "big_ice_v_w"},
            {'Ледовая арена «Шайба»': 'shaiba_v_w'}, {'Адлер-Арена': 'adler_v_w'},
            {'Образовательный центр Сириус': "sirius_v_w"},
            {'Отель омега Сириус': 'sirius_hotel_v_w'}, {"Сириус Лицей": 'sirius_lyceum_v_w'},
            {"Фонтаны": "fontains_v_w"}, {"Закончить экскурсию": "end"}]
    keyboard = Keyboa(items=menu, front_marker="", back_marker="").keyboard
    bot.send_message(chat_id=callback.message.chat.id, text="Про какой объект тебе рассказать?",
                     reply_markup=keyboard)


def less_go(callback):
    menu = [{"Стадион «Фишт»": "fisht"}, {"Ледовый дворец «Большой»": "big_ice"},
            {'Ледовая арена «Шайба»': 'shaiba'}, {'Адлер-Арена': 'adler'}, {'Образовательный центр Сириус': "sirius"},
            {'Отель омега Сириус': 'sirius_hotel'}, {"Сириус Лицей": 'sirius_lyceum'},
            {"Фонтаны": "fontains"}, {"Закончить экскурсию": "end"}]
    keyboard = Keyboa(items=menu, front_marker="", back_marker="").keyboard
    bot.send_message(chat_id=callback.message.chat.id, text="Про какой объект тебе рассказать?",
                     reply_markup=keyboard)


def fisht(callback):
    bot.send_message(chat_id=callback.message.chat.id, text="Этот стадион - самое"
                                                            " огромное🤯 олимпийское сооружение, вместившее на"
                                                            " Олимпиаде 40 000 зрителей😳,"
                                                            " а на чемпионате мира по футболу"
                                                            " до 44 000 болельщиков. Назван в честь одноименной"
                                                            " горной вершины⛰ Кавказского хребта,"
                                                            " высотой 2868 метров,что в переводе"
                                                            " с адыгейского значит «белая голова».")
    bot.send_photo(chat_id=callback.message.chat.id,
                   photo='https://stadions.org/wp-content/uploads/2019/08/11458851-1024x759.jpg')
    time.sleep(7)
    less_go(callback)


def big_ice(callback):
    bot.send_message(chat_id=callback.message.chat.id,
                     text="Невероятно красивый стадион😍, его форма напоминает замерзшую"
                          " огромную каплю💧 жемчужного цвета. Этот стадион был создан"
                          " как ледовая арена для хоккея во время Олимпиады 2014."
                          " Его стоимость оценивается почти в 10 миллиардов рублей."
                          " Вместительность - около 12 000 человек😲."
                          " Хоккейный стадион состоит из подземной и наземной частей"
                          " и имеет 6 уровней."
                          " На территории стадиона есть два ресторана,"
                          " фаст-фуды🍕 и буфеты.")
    bot.send_photo(chat_id=callback.message.chat.id,
                   photo='https://yugarf.ru/wp-content/uploads/2018/04/ledovyy-dvorets-bolshoy-v-sochi.jpg')
    time.sleep(3)
    bot.send_message(chat_id=callback.message.chat.id, text="Помимо соревнований ледовых видов спорта🏒 на сегодняшний"
                                                            " день здесь довольно часто проходят развлекательные,"
                                                            " зрелищные и культурные мероприятия,"
                                                            " к примеру, в 2016 году"
                                                            " именно здесь проводил мотивирующую лекцию🥇"
                                                            " «Жизнь без границ» всемирно известный оратор Ник Вуйчич,"
                                                            " родившийся без рук и ног. Также бывают разнообразные"
                                                            " ярмарки, фестивали, конференции и выставки.")
    time.sleep(7)
    less_go(callback)


def shaiba(callback):
    bot.send_message(chat_id=callback.message.chat.id, text="Второй по значимости🥈 олимпийский объект, его"
                                                            " вместимость составляет "
                                                            "7 000 зрителей, возводился он 3 года🏗. Было"
                                                            " потрачено более"
                                                            " 2,5 миллиардов рублей. Проектировался он как переносной🚛"
                                                            " стадион, чтобы его можно было перевозить в любой другой"
                                                            " город, но выяснилось, что сконструированный фундамент"
                                                            " этого сделать не позволит. Интересно, что в нем нет"
                                                            " ни одной ступеньки")
    bot.send_photo(chat_id=callback.message.chat.id,
                   photo="https://yugarf.ru/wp-content/uploads/2018/06/ledovaya-arena-shayba-v-adlere.jpg")
    less_go(callback)


def adler(callback):
    bot.send_message(chat_id=callback.message.chat.id, text="Задумывался как крытый центр для конькобежного спорта🥅,"
                                                            " строился 2 года. На строительство было затрачено 32,8"
                                                            " миллиона долларов. Овальный стадион длиной 400м, высотой"
                                                            "25м и общей площадью 2х этажей около 51 000 кв.м, "
                                                            "оформлен "
                                                            " витражными тонированными окнами🏙 и может"
                                                            " вместить 8000 зрителей🏠.")
    bot.send_photo(chat_id=callback.message.chat.id,
                   photo="https://nicko.ru/wp-content/uploads/2018/04/%D0%90%D0%B4%D0%BB%D0%B5%D1%80"
                         "-%D0%90%D1%80%D0%B5%D0%BD%D0%B0-%D0%A4%D0%BE%D1%82%D0%BE.jpg"
                         "/768_768_1/1404.jpg")
    time.sleep(7)
    less_go(callback)


def sirius(callback):
    bot.send_message(chat_id=callback.message.chat.id, text="Образовательный центр для детей по направлениям наука🔬,"
                                                            " творчество🖼 и спорт⚽️. Цель работы образовательного центра"
                                                            " «Сириус» – раннее выявление, развитие и дальнейшая"
                                                            " профессиональная поддержка одарённых детей, проявивших"
                                                            " выдающиеся способности в области искусств,"
                                                            " спорта, естественнонаучных дисциплин, а также "
                                                            "добившихся успеха в техническом творчестве."
                                                            " Центр работает круглый год⏱. Для школьников,"
                                                            " демонстрирующих успехи в точных, цифровых и естественных"
                                                            " науках, в Центре организованы образовательные программы"
                                                            " по математике👨‍🎓, информатике👨‍💻, физике, химии👨‍🔬, биологии🔬"
                                                            ", лингвистике🇺🇳 и проектной деятельности")
    bot.send_photo(chat_id=callback.message.chat.id,
                   photo="https://img.lookmytrips.com/images/look5j3j/"
                         "581b300bff93670f51018caa-5cc0a8a89323e-1ec1a58-lbcvr.jpg")
    time.sleep(7)
    less_go(callback)


def sirius_hotel(callback):
    bot.send_message(chat_id=callback.message.chat.id, text="Отель Omega Sirius 3⭐️ благодаря развитой инфраструктуре"
                                                            " служит прекрасным местом для семейного отдыха😴,"
                                                            " «умного туризма» и проведения деловых мероприятий👔 любого"
                                                            " масштаба. Расположен рядом с Олимпийским парком"
                                                            " в Имеретинской низменности.")
    bot.send_photo(chat_id=callback.message.chat.id,
                   photo="https://cdn.101hotels.com/uploads/image/hotel_image/5020/50017.jpg")
    time.sleep(2)
    bot.send_message(chat_id=callback.message.chat.id, text="К услугам гостей ресторан и лобби-бар, детская комната,"
                                                            " тренажерный зал, собственный оборудованный пляж"
                                                            " и парковка. Для проведения мероприятий на высоком уровне"
                                                            " предлагаются функциональные конференц-залы и зона для"
                                                            " кофе-брейков☕️. Возможность проживания с животными🧸 позволит"
                                                            " взять любимого питомца с собой на отдых.")
    time.sleep(4)
    less_go(callback)


def sirius_lyceum(callback):
    bot.send_message(chat_id=callback.message.chat.id, text="Лицей «Сириус» открыл свои двери🚪 1 сентября 2020 года."
                                                            " Он находится в городском округе Сириус (Сочи)🌅."
                                                            " Лицей объединяет крепкое классическое образование"
                                                            " и новейшие образовательные технологии. Особенности"
                                                            " обучения — индивидуальный учебный план и свободный выбор"
                                                            " образовательной траектории."
                                                            " Занятия проходят в современных"
                                                            " классах и лабораториях👨‍🔬 Центра «Сириус», Парка науки"
                                                            " и искусства, на спортивных объектах Олимпийского парка."
                                                            " Образовательная программа объединяет возможности 6 школ:"
                                                            " общеобразовательная, языковая, научно-исследовательская,"
                                                            " инженерно-математическая, спортивная,"
                                                            " художественно-музыкальная")
    bot.send_photo(chat_id=callback.message.chat.id,
                   photo="https://arch-sochi.ru/wp-content/uploads/2019/11/sochi-11205-1235.jpg")
    time.sleep(4)
    less_go(callback)


def fontains(callback):
    bot.send_message(chat_id=callback.message.chat.id, text="Мультимедийное аква-шоу🔮: красивейший аттракцион воды💦"
                                                            " и музыки, лазеров и пиротехники - фантастика"
                                                            " современного Сочи. В летнюю программу развлечений в Сочи"
                                                            " Парке входит мультимедийное водное шоу💧, сочетающее"
                                                            " танцующие под музыку фонтаны⛲️, видеопроекции, лазерные"
                                                            " и пиротехнические эффекты⚡️. Сценической площадкой для"
                                                            " представления стал бассейн площадью 1800 квадратных"
                                                            " метров с водяным экраном, высотой🔝 15 метров, образуемым"
                                                            " работой 168 форсунок. В шоу задействованы 17"
                                                            " двадцатиметровых и 3 пятидесятиметровых водомета,"
                                                            " 10 машин огня, более 200 дистанционно управляемых "
                                                            "приборов подсветки и современный комплекс лазерных🔦 "
                                                            "проекторов. Зрители шоу с удобством размещаются на "
                                                            "трибунах на 2000 мест.")
    bot.send_photo(chat_id=callback.message.chat.id,
                   photo="http://олимпийский-парк.рф/uploads/posts/2017-08/1502483385_2-op-feniks.jpg")
    time.sleep(4)
    less_go(callback)


def fisht_v_m(callback):
    voice = open(r'C:\Users\yarsl\PycharmProjects\Bot_Kyoto2\Audio\Фишт - м.mp3', 'rb')
    bot.send_photo(chat_id=callback.message.chat.id,
                   photo='https://stadions.org/wp-content/uploads/2019/08/11458851-1024x759.jpg')
    bot.send_voice(chat_id=callback.message.chat.id, voice=voice)
    going_voice_m(callback)


def big_ice_v_m(callback):
    voice = open(r'C:\Users\yarsl\PycharmProjects\Bot_Kyoto2\Audio\Ледовый - м.mp3', 'rb')
    bot.send_photo(chat_id=callback.message.chat.id,
                   photo='https://yugarf.ru/wp-content/uploads/2018/04/ledovyy-dvorets-bolshoy-v-sochi.jpg')
    bot.send_voice(chat_id=callback.message.chat.id, voice=voice)
    going_voice_m(callback)


def shaiba_v_m(callback):
    voice = open(r'C:\Users\yarsl\PycharmProjects\Bot_Kyoto2\Audio\Шайба - м.mp3', 'rb')
    bot.send_photo(chat_id=callback.message.chat.id,
                   photo="https://yugarf.ru/wp-content/uploads/2018/06/ledovaya-arena-shayba-v-adlere.jpg")
    bot.send_voice(chat_id=callback.message.chat.id, voice=voice)
    going_voice_m(callback)


def adler_v_m(callback):
    voice = open(r'C:\Users\yarsl\PycharmProjects\Bot_Kyoto2\Audio\Адлер арена.mp3', 'rb')
    bot.send_photo(chat_id=callback.message.chat.id,
                   photo="https://nicko.ru/wp-content/uploads/2018/04/%D0%90%D0%B4%D0%BB%D0%B5%D1%80"
                         "-%D0%90%D1%80%D0%B5%D0%BD%D0%B0-%D0%A4%D0%BE%D1%82%D0%BE.jpg")
    bot.send_voice(chat_id=callback.message.chat.id, voice=voice)
    going_voice_m(callback)


def sirius_v_m(callback):
    voice = open(r'C:\Users\yarsl\PycharmProjects\Bot_Kyoto2\Audio\Сириус - м.mp3', 'rb')
    bot.send_photo(chat_id=callback.message.chat.id,
                   photo="https://img.lookmytrips.com/images/look5j3j/"
                         "581b300bff93670f51018caa-5cc0a8a89323e-1ec1a58-lbcvr.jpg")
    bot.send_voice(chat_id=callback.message.chat.id, voice=voice)
    going_voice_m(callback)


def sirius_hotel_v_m(callback):
    voice = open(r'C:\Users\yarsl\PycharmProjects\Bot_Kyoto2\Audio\Отель - м.mp3', 'rb')
    bot.send_photo(chat_id=callback.message.chat.id,
                   photo="https://cdn.101hotels.com/uploads/image/hotel_image/5020/50017.jpg")
    bot.send_voice(chat_id=callback.message.chat.id, voice=voice)
    going_voice_m(callback)


def sirius_lyceum_v_m(callback):
    voice = open(r'C:\Users\yarsl\PycharmProjects\Bot_Kyoto2\Audio\Лицей - м.mp3', 'rb')
    bot.send_photo(chat_id=callback.message.chat.id,
                   photo="https://arch-sochi.ru/wp-content/uploads/2019/11/sochi-11205-1235.jpg")
    bot.send_voice(chat_id=callback.message.chat.id, voice=voice)
    going_voice_m(callback)


def fontains_v_m(callback):
    voice = open(r'C:\Users\yarsl\PycharmProjects\Bot_Kyoto2\Audio\Фонтаны - м.mp3', 'rb')
    bot.send_photo(chat_id=callback.message.chat.id,
                   photo="http://олимпийский-парк.рф/uploads/posts/2017-08/1502483385_2-op-feniks.jpg")
    bot.send_voice(chat_id=callback.message.chat.id, voice=voice)
    going_voice_m(callback)


# woman voice

def fisht_v_w(callback):
    voice = open(r'C:\Users\yarsl\PycharmProjects\Bot_Kyoto2\Audio\Woman voice\стадион Фишт .mp3', 'rb')
    bot.send_photo(chat_id=callback.message.chat.id,
                   photo='https://stadions.org/wp-content/uploads/2019/08/11458851-1024x759.jpg')
    bot.send_voice(chat_id=callback.message.chat.id, voice=voice)
    time.sleep(3)
    going_voice_w(callback)


def big_ice_v_w(callback):
    voice = open(r'C:\Users\yarsl\PycharmProjects\Bot_Kyoto2\Audio\Woman voice\ледовый дворец Большой.mp3', 'rb')
    bot.send_photo(chat_id=callback.message.chat.id,
                   photo='https://yugarf.ru/wp-content/uploads/2018/04/ledovyy-dvorets-bolshoy-v-sochi.jpg')
    bot.send_voice(chat_id=callback.message.chat.id, voice=voice)
    time.sleep(3)
    going_voice_w(callback)


def shaiba_v_w(callback):
    voice = open(r'C:\Users\yarsl\PycharmProjects\Bot_Kyoto2\Audio\Woman voice\ледовая арена шайба_1.mp3', 'rb')
    bot.send_photo(chat_id=callback.message.chat.id,
                   photo="https://yugarf.ru/wp-content/uploads/2018/06/ledovaya-arena-shayba-v-adlere.jpg")
    bot.send_voice(chat_id=callback.message.chat.id, voice=voice)
    time.sleep(3)
    going_voice_w(callback)


def adler_v_w(callback):
    voice = open(r'C:\Users\yarsl\PycharmProjects\Bot_Kyoto2\Audio\Woman voice\адлер-арена_1.mp3', 'rb')
    bot.send_photo(chat_id=callback.message.chat.id,
                   photo="https://nicko.ru/wp-content/uploads/2018/04/%D0%90%D0%B4%D0%BB%D0%B5%D1%80"
                         "-%D0%90%D1%80%D0%B5%D0%BD%D0%B0-%D0%A4%D0%BE%D1%82%D0%BE.jpg")
    bot.send_voice(chat_id=callback.message.chat.id, voice=voice)
    time.sleep(3)
    going_voice_w(callback)


def sirius_v_w(callback):
    voice = open(r'C:\Users\yarsl\PycharmProjects\Bot_Kyoto2\Audio\Woman voice\образовательный центр сириус_1.mp3', 'rb')
    bot.send_photo(chat_id=callback.message.chat.id,
                   photo="https://img.lookmytrips.com/images/look5j3j/"
                         "581b300bff93670f51018caa-5cc0a8a89323e-1ec1a58-lbcvr.jpg")
    bot.send_voice(chat_id=callback.message.chat.id, voice=voice)
    time.sleep(3)
    going_voice_w(callback)


def sirius_hotel_v_w(callback):
    voice = open(r'C:\Users\yarsl\PycharmProjects\Bot_Kyoto2\Audio\Woman voice\отель сириус_1.mp3', 'rb')
    bot.send_photo(chat_id=callback.message.chat.id,
                   photo="https://cdn.101hotels.com/uploads/image/hotel_image/5020/50017.jpg")
    bot.send_voice(chat_id=callback.message.chat.id, voice=voice)
    time.sleep(3)
    going_voice_w(callback)


def sirius_lyceum_v_w(callback):
    voice = open(r'C:\Users\yarsl\PycharmProjects\Bot_Kyoto2\Audio\Woman voice\Сириус лицей1_1.mp3', 'rb')
    bot.send_photo(chat_id=callback.message.chat.id,
                   photo="https://arch-sochi.ru/wp-content/uploads/2019/11/sochi-11205-1235.jpg")
    bot.send_voice(chat_id=callback.message.chat.id, voice=voice)
    time.sleep(3)
    going_voice_w(callback)


def fontains_v_w(callback):
    voice = open(r'C:\Users\yarsl\PycharmProjects\Bot_Kyoto2\Audio\Woman voice\фонтаны .mp3', 'rb')
    bot.send_photo(chat_id=callback.message.chat.id,
                   photo="http://олимпийский-парк.рф/uploads/posts/2017-08/1502483385_2-op-feniks.jpg")
    bot.send_voice(chat_id=callback.message.chat.id, voice=voice)
    time.sleep(3)
    going_voice_w(callback)


def end(callback):
    bot.send_message(chat_id=callback.message.chat.id, text="Спасибо за использование нашего бота. Надеюсь вам"
                                                            " понравился мой рассказ😅. Вы также можете перезапустить"
                                                            " бота и изучить эксурсионный материал в другом формате)")
    time.sleep(2)
    bot.send_sticker(chat_id=callback.message.chat.id, data='CAACAgIAAxkBAAECOhNghI1MqYZN'
                                                            '8HpxE7MvJDwzu7MxPwACsQAD98zUGE-yzWOggc_4HwQ')


bot.polling()
