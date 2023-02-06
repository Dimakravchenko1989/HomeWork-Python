from telegram.ext import ConversationHandler
CHOICE, RATIONAL_ONE, RATIONAL_TWO, OPERATIONS_RATIONAL = range(4)

# # Функция для старта нашего бота
def start(update, context):
    update.message.reply_text('Это - калькулятор. Выберите пожалуйста команду.\n' 'Команда /cancel, чтобы прекратить разговор.\n\n')
    update.message.reply_text('1 - Работа с рациональными числами; \n2 - Выйти из калькулятора \n')
    return CHOICE

# Выбор основного меню
def choice(update, context):
    user_choice = update.message.text
    if user_choice in '12':
        if user_choice == '1':
            update.message.reply_text('Введите число. \n Первое рациональное число - это: ')
            return RATIONAL_ONE
        if user_choice == '2':
            update.message.reply_text('Спасибо, до свидания!')
            return ConversationHandler.END     

# Получение первого числа
def rational_one(update, context):
    get_rational = update.message.text
    if get_rational.isdigit():
        get_rational = float(get_rational)
        context.user_data['rational_one'] = get_rational
        update.message.reply_text('Введите второе число')
        return RATIONAL_TWO

    else:
        update.message.reply_text('Нужно ввести число')

# Получение второго числа
def rational_two(update, context):
    get_rational = update.message.text
    if get_rational.isdigit():
        get_rational = float(get_rational)
        context.user_data['rational_two'] = get_rational
        update.message.reply_text('Выберите действие: \n\n+  для сложения; \n-  для вычетания; \n*  для умножения; \n/  для деления. \n')
        return OPERATIONS_RATIONAL

# Выбор действия и получение рультата
def operatons_rational(update, context):
    rational_one = context.user_data.get('rational_one')
    rational_two = context.user_data.get('rational_two')
    user_choice = update.message.text
    if user_choice in '+-/*':
        if user_choice == '+':
            result = rational_one + rational_two
        if user_choice == '-':
            result = rational_one - rational_two
        if user_choice == '*':
            result = rational_one * rational_two
        if user_choice == '/':
            try:
                result = rational_one / rational_two
            except:
                update.message.reply_text('Делить на ноль нельзя')
        update.message.reply_text(f'Результат:  {result}')
        return ConversationHandler.END
    else:
        update.message.reply_text('Ошибка ввода. Выберите действие: \n+  для сложения; \n-  для вычетания; \n*  для умножения; \n/  для деления. \n' )

# Функция для завершения работы
def cancel(update, context):
    update.message.reply_text('Спасибо, до свидания!')
    return ConversationHandler.END