import face_recognition
import cv2
import time
import pync
import random

"""Constants for track_screen_time"""
MODEL_NAME = "cnn"  # Convolutional Neural Network
VIDEO_PORT = 0  # Port for webcam

"""Constants for posture reminder thread"""
POSTURE_LOWER_BOUND = (60 * 60 * 60)  # Lower bound for timing of random notifications (1 hour)
POSTURE_UPPER_BOUND = (60 * 60 * 60) * 3  # Upper bound for timing of random notifications (3 hours)


def track_screen_time():
    """Thread to track user screen time using facial recognition
        TODO : Implement algorithm for session tracking

        Algorithm:
            Check if user is at screen
            if user is not at screen for 5 minutes, this is a break, reset timer
            else if user has been at screen for rand(50,60) minutes, as them to take a break
            if they come back after 5 minutess, begin counting the hour again
            else continue counting screen time and report it every hour
    """
    vid = cv2.VideoCapture(VIDEO_PORT)
    time.sleep(5)
    start_time = time.perf_counter()
    rest_time = random.randint(60 * 50, 60 * 60)
    while True:
        i, snapshot = vid.read()
        snapshot = cv2.cvtColor(snapshot, cv2.COLOR_RGB2BGR)
        snapshot = cv2.resize(snapshot, None, fx=0.20, fy=0.20, interpolation=cv2.INTER_AREA)  # Scale image down 1/5
        entities = face_recognition.face_locations(snapshot, model=MODEL_NAME)  # Run image through cnn
        if entities:
            curr_time = (time.perf_counter() - start_time) / 60.0  # minutes that user has been at screen for
            msg = f"Your screen time this session is {curr_time:.1f} minutes"
            pync.notify(msg, appIcon="128.png", title="RoboSitter Says:")
        else:
            start_time = time.clock()
            pync.notify("Where did u go?", appIcon="128.png", title="RoboSitter Says:")
        time.sleep(5)


def posture_reminders():
    """Thread to send user random reminders to fix their posture"""
    while True:
        s = random.randint(POSTURE_LOWER_BOUND, POSTURE_UPPER_BOUND)
        time.sleep(s)
        pync.notify("Fix your posture!", appIcon="128.png", title="RoboSitter Says:")
