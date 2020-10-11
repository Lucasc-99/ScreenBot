import threading
import pync
import RoboSitterThreads

threads = dict()  # Dictionary used to keep track of all RoboSitter related threads


def start_screen_track():
    """Starter function for screen time tracker"""
    s_thread = threading.Thread(target=RoboSitterThreads.track_screen_time())
    threads['screentime'] = s_thread
    s_thread.start()


def stop_screen_track():  # NOT TESTED
    """Starter function for screen time tracker"""
    if 'posture' in threads:
        threads['posture'].stop()
        del threads['posture']


def start_posture_reminders():
    """Starter function for posture reminders thread"""
    p_thread = threading.Thread(target=RoboSitterThreads.posture_reminders())
    threads['posture'] = p_thread
    p_thread.start()


def stop_posture_reminders():  # NOT TESTED
    """Stopper function for posture reminders thread"""
    if 'posture' in threads:
        threads['posture'].stop()
        del threads['posture']


def stop_all_threads():  # NOT TESTED
    """Function for stopping all RoboSitter related threads"""
    for i, j in enumerate(threads):
        threads[j].stop()
        del threads[j]


if __name__ == '__main__':
    pync.notify("Welcome, I am RoboSitter", appIcon="128.png", title="RoboSitter Says :")
    start_screen_track()
    start_posture_reminders()
