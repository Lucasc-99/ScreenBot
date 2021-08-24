import face_recognition
import cv2
import time
import pync
import random

"""CONSTANTS"""
MODEL_NAME = "cnn"  # Convolutional Neural Network
VIDEO_PORT = 0  # Port for webcam
BREAK_TIME = 60 * 2  # Length of breaks for user
IMAGE_DOWNSCALE = 0.2  # Downscale image for performance
SCREEN_LOWER_BOUND = 60 * 50  # Lower bound screen-time before break is required in (seconds)
SCREEN_UPPER_BOUND = 50 * 60  # Upper bound screen-time before break is required in (seconds)
SCREEN_CHECK_INTERVAL = 10  # Seconds to wait in-between screen checks
SCREEN_MISS_TOLERANCE = 3  # Tolerance for screen recognition misses, change this to be the same length as a break
POSTURE_LOWER_BOUND = (60 * 60 * 60)  # Lower bound for timing of random notifications (seconds)
POSTURE_UPPER_BOUND = (60 * 60 * 60) * 3  # Upper bound for timing of random notifications (seconds)


def track_screen_time():
    """Thread to track user screen time using facial recognition"""

    vid = cv2.VideoCapture(VIDEO_PORT)
    time.sleep(5)  # Not necessary
    start_time = time.perf_counter()
    rest_time = random.randint(SCREEN_LOWER_BOUND, SCREEN_UPPER_BOUND) / 60.0
    require_break = False
    t_break_issued = 0  # Time that break was issued at
    screen_misses = 0
    while True:
        i, snapshot = vid.read()
        snapshot = cv2.cvtColor(snapshot, cv2.COLOR_RGB2BGR)
        snapshot = cv2.resize(snapshot, None, fx=IMAGE_DOWNSCALE, fy=IMAGE_DOWNSCALE, interpolation=cv2.INTER_AREA)
        entities = face_recognition.face_locations(snapshot, model=MODEL_NAME)  # Run image through cnn
        curr_time = (time.perf_counter() - start_time) / 60.0
        if entities:
            if require_break:
                msg = "You should be taking a break! Break timer reset"
                pync.notify(msg, appIcon="128.png", title="ScreenBOT Says:")
                t_break_issued = time.perf_counter()
            elif curr_time >= rest_time:
                msg = f"You have been here {curr_time:.1f} minutes, take a break"
                t_break_issued = time.perf_counter()
                require_break = True
                pync.notify(msg, appIcon="128.png", title="ScreenBOT Says:")
        elif require_break:
            if (time.perf_counter() - t_break_issued) >= BREAK_TIME:  # BREAK_TIME minutes have elapsed
                require_break = False
                start_time = time.perf_counter()
                t_break_issued = 0
                pync.notify("You have completed your break!", appIcon="128.png", title="ScreenBOT Says:")
        else:
            if screen_misses > SCREEN_MISS_TOLERANCE:
                start_time = time.perf_counter()
                pync.notify("No one is home", appIcon="128.png", title="ScreenBOT Says:")
                screen_misses = 0
            else:
                screen_misses += 1

        # Sleep until next check
        time.sleep(SCREEN_CHECK_INTERVAL)


def posture_reminders():
    """Thread to send user random reminders to fix their posture"""
    while True:
        s = random.randint(POSTURE_LOWER_BOUND, POSTURE_UPPER_BOUND)
        time.sleep(s)
        pync.notify("Fix your posture!", appIcon="128.png", title="ScreenBOT Says:")
