import logging
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.parsemode import ParseMode
import schedule
import time
from decouple import config

API_KEY = config('KEY')

# import threading    
# import queue

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
users = [758799957]
bot = Bot(API_KEY)
reg = False

def send_msg(text):
    """Send the alarm message."""
    print(text)
    for user in users:
        bot.send_message(chat_id=user, text=text, parse_mode = ParseMode.MARKDOWN)
    
#     # return schedule.CancelJob

def start(update: Update, context: CallbackContext) -> None:
#     """Sends explanation on how to use the bot."""
    id = update.message.from_user.id
    if id not in users:
        users.append()
    
    update.message.reply_text('You have activated reminder bot. You will be reminded at the specified times!!')
    file = open('./tt.png','rb')
    update.message.reply_photo(file)
    global reg
    reg = True
    

def main() -> None:
    """Run bot."""
    updater = Updater(API_KEY)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()

    if reg:
        updater.stop()
    
#     def worker_main():
#         while 1:
#             job_func = jobqueue.get()
#             job_func()
#             jobqueue.task_done()

#     jobqueue = queue.Queue()

#     def run_threaded(job_func):
#         job_thread = threading.Thread(target=job_func)
#         job_thread.start()

    
    schedule.every().monday.at("08:40").do(send_msg, "time for PSAT class")
    schedule.every().monday.at("09:30").do(send_msg, "time for Meditation class")
    schedule.every().monday.at("10:00").do(send_msg, "time for Maths class")
    # schedule.every().monday.at("11:00").do(send_msg, "time for class")
    schedule.every().monday.at("12:00").do(send_msg, "time for class")
    schedule.every().monday.at("14:00").do(send_msg, "time for class")
    schedule.every().monday.at("16:00").do(send_msg, "time for class")
    schedule.every().tuesday.at("08:40").do(send_msg, "time for Maths class")
    schedule.every().tuesday.at("10:00").do(send_msg, "time for CSE101 class")
    # schedule.every().tuesday.at("12:00").do(send_msg, "time for class")
    schedule.every().tuesday.at("14:00").do(send_msg, "time for MEE class")
    # schedule.every().tuesday.at("16:00").do(send_msg, "time for class")
    # schedule.every().wednesday.at("08:40").do(send_msg, "time for class")
    schedule.every().wednesday.at("10:00").do(send_msg, "time for Maths class")
    schedule.every().wednesday.at("11:00").do(send_msg, "time for CUL class")
    schedule.every().wednesday.at("12:00").do(send_msg, "time for class")
    schedule.every().wednesday.at("14:00").do(send_msg, "time for LAB")
    # schedule.every().wednesday.at("16:00").do(send_msg, "time for class")
    schedule.every().thursday.at("08:40").do(send_msg, "time for maths class")
    # schedule.every().thursday.at("10:00").do(send_msg, "time for class")
    schedule.every().thursday.at("11:00").do(send_msg, "time for class")
    schedule.every().thursday.at("12:00").do(send_msg, "time for ENG class")
    schedule.every().thursday.at("14:00").do(send_msg, "time for LAB")
    # schedule.every().thursday.at("16:00").do(send_msg, "time for class")
    # schedule.every().friday.at("08:40").do(send_msg, "time for class")
    schedule.every().friday.at("10:00").do(send_msg, "time for ENG class")
    schedule.every().friday.at("11:00").do(send_msg, "time for class")
    schedule.every().friday.at("12:00").do(send_msg, "time for Maths class")
    # schedule.every().friday.at("16:00").do(send_msg, "time for class")

    # worker_thread = threading.Thread(target=worker_main)
    # worker_thread.start()    

    # schedule.run_all()

    while 1:
        schedule.run_pending()
        time.sleep(120)


if __name__ == '__main__':
    main()