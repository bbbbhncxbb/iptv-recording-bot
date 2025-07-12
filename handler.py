from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from handlers.start_handler import start
from handlers.admin_handler import handle_admin_request
from handlers.help_handler import send_help
from handlers.schedule_handler import handle_schedule
from handlers.record_handler import handle_instant_record
from handlers.temp_admin_handler import add_temp_admin, remove_admin
from features.messaging import get_message_handlers
from telegram.ext import CommandHandler
from handlers.record_handler import handle_find_channel
from handlers.record_handler import show_help
from handlers.help_handler import cancel_recording_callback
from telegram.ext import CommandHandler
from features.status_broadcast import status_command, broadcast_command


def register_handlers(application: Application):
    """Register all handlers"""
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_admin_request, pattern="^request_admin$"))
    application.add_handler(CommandHandler(["h"], send_help))
    application.add_handler(CommandHandler(["schedule", "s"], handle_schedule))
    application.add_handler(CommandHandler(["rec", "r"], handle_instant_record))
    application.add_handler(CommandHandler(["addadmin", "add"], add_temp_admin))
    application.add_handler(CommandHandler(["removeadmin", "rem", "rm"], remove_admin))
    application.add_handlers(get_message_handlers())
    application.add_handler(CommandHandler("find", handle_find_channel))

    application.add_handler(CommandHandler("p1", handle_instant_record))
    application.add_handler(CommandHandler("p2", handle_instant_record))
    application.add_handler(CommandHandler("p3", handle_instant_record))
    application.add_handler(CommandHandler("help", show_help))
    application.add_handler(
        CallbackQueryHandler(
            cancel_recording_callback,
            pattern="^cancel_recording_"
        )
    )
    application.add_handler(CommandHandler("status", status_command))
    application.add_handler(CommandHandler("broadcast", broadcast_command))
    
    from features.verify import setup_verify_handlers

    setup_verify_handlers(application)

    
