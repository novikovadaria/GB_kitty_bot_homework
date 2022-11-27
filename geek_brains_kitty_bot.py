
import telebot
from wiki import getwiki
from calculations import calc
from weather_api import get_weather
from db_work import add_book
bot_token = '5484310907:AAHqaQsFv9'

bot = telebot.TeleBot(bot_token)


try:
    @bot.message_handler(commands=['start'])
    def start(message):
        mess = f'Прикот, <b>{message.from_user.first_name} </b>!'
        bot.send_message(message.chat.id, mess, parse_mode='html')

    @bot.message_handler(commands=['weather'])
    def weather(message):
        def asking(message):
            mesg = bot.send_message(
                message.chat.id, 'Введите название города на английском языке. Например, Krasnodar 😼')
            bot.register_next_step_handler(mesg, answer)

        def answer(message):
            bot.send_message(message.chat.id, get_weather(message.text))
        asking(message)

    @bot.message_handler(commands=['calc'])
    def math(message):
        bot.send_message(
            message.chat.id, 'Сейчас будем вычислять!')

        def asking(message):
            mesg = bot.send_message(
                message.chat.id, 'Напишите ваше математическое выражение через пробелы, например 2 + 2, мяу?')
            bot.register_next_step_handler(mesg, answer)

        def answer(message):
            bot.send_message(message.chat.id, calc(message.text))
        asking(message)
    
    @bot.message_handler(commands=["library"])
    def wiki(message):
        bot.send_message(
            message.chat.id, 'Напишите имя, фамилию автора, название книги и количество страниц через ","')

        def asking(message):
            mesg = bot.send_message(message.chat.id, 'Что вносим?')
            bot.register_next_step_handler(mesg, answer)

        def answer(message):
            bot.send_message(message.chat.id, add_book(message.text))
        asking(message)
    
    
    @bot.message_handler(commands=["wiki"])
    def wiki(message):
        bot.send_message(
            message.chat.id, 'Отправьте мне любое слово, и я найду его значение на котопедии, мяу')

        def asking(message):
            mesg = bot.send_message(message.chat.id, 'Что ищем?')
            bot.register_next_step_handler(mesg, answer)

        def answer(message):
            bot.send_message(message.chat.id, getwiki(message.text))
        asking(message)

        if 'песен' in message.text.lower() or 'музык' in message.text.lower() or 'песн' in message.text.lower():
            audio = open(
                'Zhanulka - Ты похож на кота, хочу забрать тебя домой (MATLY Remix).mp3', 'rb')
            bot.send_audio(message.chat.id, audio)
            bot.send_message(
                message.chat.id, 'вот, моя любимая песенка, мау 😸')
        elif 'твоё любимое аниме' in message.text.lower():
            bot.send_message(message.
                             chat.id, 'Моё любмое аниме то, в котором главный герой стремится к свободе, борется с внешними обстоятельствами несмотря не на что, а ещё я люблю чтобы там чмоки-чмоки были 😌')
        elif 'спой' in message.text.lower():
            bot.send_message(
                message.chat.id, 'кис-кис кис-кис\nя котик, ты котик\nа твои поцелуи почти как лёгкий наркотик 😽🎤')
        elif '😽' in message.text:
            bot.send_message(message.chat.id, '😽😽')
        elif 'котро' in message.text or 'котре' in message.text.lower():
            bot.send_message(message.chat.id, 'Доброе котро ☀️ !')

            def asking(message):
                mesg = bot.send_message(
                    message.chat.id, 'Вы хорошо спали?')
                bot.register_next_step_handler(mesg, answer)

            def answer(message):
                if 'да' in message.text.lower():
                    bot.send_message(
                        message.chat.id, 'Замечательно! Я тоже выспался, мау 😸')
                    return asking
                else:
                    bot.send_message(
                        message.chat.id, 'Ничего страшного, мне иногда сняться кошмаренькие, но на следующий день я сплю хорошо, мау')
                    return asking
            asking(message)
        elif "🐟" in message.text or "🐠" in message.text or "🐡" in message.text:
            def asking(message):
                mesg = bot.send_message(
                    message.chat.id, 'О! Рыбонький! Можно скушать? 😋')
                bot.register_next_step_handler(mesg, answer)

            def answer(message):
                if 'да' in message.text.lower() or 'можно' in message.text.lower():
                    bot.send_message(
                        message.chat.id, 'Амняамняням')
                    bot.send_message(
                        message.chat.id, 'Очень вкусно, спасибо!')

                    return asking
                else:
                    bot.send_message(
                        message.chat.id, 'миууу :с')
                    return asking
            asking(message)
        elif "🦉" in message.text or "🦅" in message.text or "🦆" in message.text or "🐥" in message.text or "🐤" in message.text or "🐤" in message.text or "🐦" in message.text or "🐧" in message.text or "🐔" in message.text or "🦜" in message.text or "🦤" in message.text or "🦩" in message.text or "🐓" in message.text:
            def asking(message):
                mesg = bot.send_message(
                    message.chat.id, 'Мау! Это птиченький! Можно я скушаю? 😋')
                bot.register_next_step_handler(mesg, answer)

            def answer(message):
                if 'да' in message.text.lower() or 'можно' in message.text.lower():
                    bot.send_message(
                        message.chat.id, 'Амняамняням')
                    bot.send_message(
                        message.chat.id, 'Очень вкусно, спасибо!')

                    return asking
                else:
                    bot.send_message(
                        message.chat.id, 'миууу :с')
                    return asking
            asking(message)
        elif "🐹" in message.text or "🐭" in message.text or "🐁" in message.text or "🐀" in message.text:
            def asking(message):
                mesg = bot.send_message(
                    message.chat.id, 'Мыыышенький! Наверное он вкусненький. Можно попробовать? 😋')
                bot.register_next_step_handler(mesg, answer)

            def answer(message):
                if 'да' in message.text.lower() or 'можно' in message.text.lower():
                    bot.send_message(
                        message.chat.id, 'Амняамняням')
                    bot.send_message(
                        message.chat.id, 'Очень вкусно, спасибо!')

                    return asking
                else:
                    bot.send_message(
                        message.chat.id, 'миууу :с')
                    return asking
            asking(message)
        elif "🐶" in message.text or "🐕‍🦺" in message.text or "🦮" in message.text or "🐩" in message.text or "🐕" in message.text:
            bot.send_message(
                message.chat.id, '<b>шииииии!</b> Это песёнький!! 😡', parse_mode='html')

            def asking(message):
                mesg = bot.send_message(
                    message.chat.id, 'Можно я ему кусь сделаю? 😾')
                bot.register_next_step_handler(mesg, answer)

            def answer(message):
                if 'да' in message.text.lower() or 'можно' in message.text.lower():
                    bot.send_message(
                        message.chat.id, '<em>кусь-кусь</em>', parse_mode='html')
                    bot.send_message(
                        message.chat.id, 'Трусливый пёсенький! Убежал 😼')

                    return asking
                else:
                    bot.send_message(
                        message.chat.id, 'миууу :с')
                    return asking
            asking(message)
        elif 'умничка' in message.text.lower():
            bot.send_message(message.chat.id, 'маауу ☺️')
        elif 'сладких' in message.text.lower():
            bot.send_message(message.chat.id, 'И вам сладких 😽')
        elif 'видео' in message.text.lower():
            video = open("cat-vaccum-cat-automatic.mp4", 'rb')
            bot.send_video(message.chat.id, video)
        elif 'мыша' in message.text.lower() or 'мышу' in message.text.lower():
            bot.send_message(
                message.chat.id, 'с мышей я друженькаю теперь 😸')
        elif 'плох' in message.text.lower() or 'хорош' in message.text.lower():
            bot.send_message(message.chat.id, 'коты самые лучшие ☺️')
        elif 'обним' in message.text.lower():
            stik = open('sticker.webp', 'rb')
            bot.send_sticker(message.chat.id, stik)
        elif 'воздушн' in message.text.lower():
            stik = open('AnimatedSticker.tgs', 'rb')
            bot.send_sticker(message.chat.id, stik)
        elif 'опрос' in message.text.lower():
            def asking(message):
                mesg = bot.send_message(
                    message.chat.id, 'На какую тему будет опрос, мау?')
                bot.register_next_step_handler(mesg, answer)

            def answer(message):
                bot.send_poll(message.chat.id, message.text.capitalize(), [
                    "Да", "Нет", "Возможно"])
            asking(message)
        elif 'помур' in message.text.lower():
            voice = open('audio_2022-08-11_21-14-41.ogg', 'rb')
            bot.send_voice(message.chat.id, voice)
        elif 'здравств' in message.text.lower():
            bot.send_message(message.chat.id, 'Здравствуйте коты!')
        elif 'как дела' in message.text.lower():
            bot.send_message(
                message.chat.id, 'У меня всё котошо, спасибо')

            def asking(message):
                mesg = bot.send_message(
                    message.chat.id, 'А у вас как дела, мау?')
                bot.register_next_step_handler(mesg, answer)

            def answer(message):
                if 'котошо' in message.text.lower() or 'замечатльно' in message.text.lower() or 'тоже' in message.text.lower() or 'прекрасно' in message.text.lower() or 'хорошо' in message.text.lower():
                    bot.send_message(message.chat.id, 'Я рад, мау!')
                else:
                    bot.send_message(
                        message.chat.id, 'Мау! Не расстраивайтесь! Все будет котошо 😽')
            asking(message)
        elif 'помяук' in message.text.lower():
            voice = open('audio_2022-08-11_21-19-53.ogg', 'rb')
            bot.send_voice(message.chat.id, voice)
        elif 'спасиб' in message.text.lower():
            bot.send_message(message.chat.id, 'Пожалуйста, мау 😸 ')
        elif 'записи' in message.text.lower():
            doc = open('your_notes.txt', 'rb')
            bot.send_document(message.chat.id, doc)
            bot.send_message(message.chat.id, 'Держите, мау!')
        elif 'фото кота' in message.text.lower():
            bot.send_photo(message.chat.id,
                           photo=open('cat.png', 'rb'))
        elif 'ты знал' in message.text.lower():
            bot.send_message(
                message.chat.id, 'Правданька? Нет, я не знал, мау')
        else:
            pass

        @bot.message_handler(content_types='photo')
        def user_sent_photo(message):
            bot.send_message(message.chat.id, 'Очень мило, мау')
except:
    pass
bot.polling()
