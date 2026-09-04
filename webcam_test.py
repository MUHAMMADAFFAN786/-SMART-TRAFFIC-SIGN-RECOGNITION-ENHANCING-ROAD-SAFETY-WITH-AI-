# this is our 3rd sem project code for webcam file 
# import cv2
# import numpy as np
# import pyttsx3
# import threading
# import queue
# from tensorflow.keras.models import load_model
# import time
# import serial

# # ✅ NEW IMPORTS (IoT Logging)
# import csv
# from datetime import datetime
# import os

# # -------------------- Arduino Setup --------------------
# arduino = serial.Serial('COM', 9600)  
# time.sleep(2)

# # -------------------- Load Trained Model --------------------
# model = load_model(r"E:\MY CODE\TRAFFIC_SIGN_RECO\GTSRB\traffic_sign_model.h5")
# print("Model Loaded Successfully")

# # -------------------- Voice Engine --------------------
# engine = pyttsx3.init()
# engine.setProperty('rate', 150)
# engine.setProperty('volume', 1.0)

# tts_queue = queue.Queue()

# def tts_worker():
#     while True:
#         message = tts_queue.get()
#         if message is None:
#             break
#         engine.say(message)
#         engine.runAndWait()
#         tts_queue.task_done()

# threading.Thread(target=tts_worker, daemon=True).start()

# # -------------------- IoT Logging Setup --------------------
# log_file = "traffic_log.csv"

# if not os.path.exists(log_file):
#     with open(log_file, 'w', newline='') as f:
#         writer = csv.writer(f)
#         writer.writerow(["Time", "Sign", "Confidence"])

# last_logged_sign = ""

# # -------------------- Traffic Sign Classes --------------------
# classes = {
#     0:'Speed limit (20km/h)',1:'Speed limit (30km/h)',2:'Speed limit (50km/h)',3:'Speed limit (60km/h)',
#     4:'Speed limit (70km/h)',5:'Speed limit (80km/h)',6:'End of speed limit (80km/h)',7:'Speed limit (100km/h)',
#     8:'Speed limit (120km/h)',9:'No passing',10:'No passing > 3.5 tons',11:'Right-of-way at intersection',
#     12:'Priority road',13:'Yield',14:'Stop',15:'No vehicles',16:'Vehicles > 3.5 tons prohibited',17:'No entry',
#     18:'General caution',19:'Dangerous curve left',20:'Dangerous curve right',21:'Double curve',22:'Bumpy road',
#     23:'Slippery road',24:'Road narrows right',25:'Road work',26:'Traffic signals',27:'Pedestrians',
#     28:'Children crossing',29:'Bicycles crossing',30:'Ice/Snow',31:'Wild animals crossing',
#     32:'End of restrictions',33:'Turn right ahead',34:'Turn left ahead',35:'Ahead only',
#     36:'Go straight or right',37:'Go straight or left',38:'Keep right',39:'Keep left',
#     40:'Roundabout mandatory',41:'End of no passing',42:'End no passing >3.5 tons'
# }

# # -------------------- Camera Setup --------------------
# cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)

# print("\nSmart Traffic Sign Detection Started... Press 'q' to quit.\n")

# # -------------------- Detection Buffer --------------------
# detected_buffer = []
# buffer_size = 7

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("Webcam disconnected.")
#         break

#     img_display = frame.copy()

#     img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     blur = cv2.GaussianBlur(img_gray, (5, 5), 0)
#     edges = cv2.Canny(blur, 40, 130)
#     contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#     best_sign = None
#     best_prob = 0
#     best_box = None

#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         if area > 2000:
#             x, y, w, h = cv2.boundingRect(cnt)
#             if w > 35 and h > 35:
#                 roi = img_rgb[y:y+h, x:x+w]
#                 try:
#                     img = cv2.resize(roi, (32, 32)) / 255.0
#                     img = np.expand_dims(img, axis=0)
#                     preds = model.predict(img, verbose=0)
#                     prob = np.max(preds)

#                     if prob > 0.90 and prob > best_prob:
#                         best_prob = prob
#                         best_sign = classes[np.argmax(preds)]
#                         best_box = (x, y, w, h)
#                 except:
#                     pass

#     if best_sign and best_box:
#         detected_buffer.append(best_sign)
#         if len(detected_buffer) > buffer_size:
#             detected_buffer.pop(0)

#         if detected_buffer.count(best_sign) > buffer_size // 2:
#             x, y, w, h = best_box
#             confidence = round(best_prob * 100, 2)

#             # Display with confidence
#             cv2.rectangle(img_display, (x, y), (x + w, y + h), (0, 255, 0), 2)
#             cv2.putText(img_display, f"{best_sign} ({confidence}%)", (x, y - 10),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

#             # -------------------- IoT Logging --------------------
#             if best_sign != last_logged_sign:
#                 time_now = datetime.now().strftime("%H:%M:%S")

#                 with open(log_file, 'a', newline='') as f:
#                     writer = csv.writer(f)
#                     writer.writerow([time_now, best_sign, confidence])

#                 print(f"Logged: {best_sign} at {time_now}")

#                 last_logged_sign = best_sign

#             # -------------------- Alerts --------------------
#             if best_sign == "Stop":
#                 tts_queue.put("Alert! Stop sign detected. Please stop immediately.")
#                 arduino.write(b'STOP\n')
#             else:
#                 tts_queue.put(f"{best_sign} detected")
#                 arduino.write(b'SPEED\n')

#     else:
#         arduino.write(b'CLEAR\n')

#     cv2.imshow("Smart Traffic Sign Detection (Webcam)", img_display)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # -------------------- Cleanup --------------------
# cap.release()
# tts_queue.put(None)
# arduino.write(b'CLEAR\n')
# cv2.destroyAllWindows()
# print("Program Closed Successfully")





































# this is our new webcam file code for our updated project in 4th sem 
import cv2
import numpy as np
import pyttsx3
import threading
import queue
from tensorflow.keras.models import load_model
import time
import serial

# IoT Logging Imports
import csv
from datetime import datetime
import os

# -------------------- Arduino Setup --------------------
try:
    arduino = serial.Serial('COM5', 9600)
    time.sleep(2)
    print("Arduino Connected")
except:
    arduino = None
    print("Running in Simulation Mode")

# -------------------- Load Model --------------------
model = load_model(r"E:\MY CODE\TRAFFIC_SIGN_RECO\GTSRB\traffic_sign_model.h5")
print("Model Loaded Successfully")

# -------------------- Voice Engine --------------------
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

tts_queue = queue.Queue()

def tts_worker():
    while True:
        message = tts_queue.get()
        if message is None:
            break
        engine.say(message)
        engine.runAndWait()
        tts_queue.task_done()

threading.Thread(target=tts_worker, daemon=True).start()

# -------------------- IoT Logging --------------------
log_file = "traffic_log.csv"

if not os.path.exists(log_file):
    with open(log_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Time", "Sign", "Confidence"])

last_logged_sign = ""

# -------------------- Classes --------------------
classes = {
    0:'Speed limit (20km/h)',1:'Speed limit (30km/h)',2:'Speed limit (50km/h)',3:'Speed limit (60km/h)',
    4:'Speed limit (70km/h)',5:'Speed limit (80km/h)',6:'End of speed limit (80km/h)',7:'Speed limit (100km/h)',
    8:'Speed limit (120km/h)',9:'No passing',10:'No passing > 3.5 tons',11:'Right-of-way at intersection',
    12:'Priority road',13:'Yield',14:'Stop',15:'No vehicles',16:'Vehicles > 3.5 tons prohibited',17:'No entry',
    18:'General caution',19:'Dangerous curve left',20:'Dangerous curve right',21:'Double curve',22:'Bumpy road',
    23:'Slippery road',24:'Road narrows right',25:'Road work',26:'Traffic signals',27:'Pedestrians',
    28:'Children crossing',29:'Bicycles crossing',30:'Ice/Snow',31:'Wild animals crossing',
    32:'End of restrictions',33:'Turn right ahead',34:'Turn left ahead',35:'Ahead only',
    36:'Go straight or right',37:'Go straight or left',38:'Keep right',39:'Keep left',
    40:'Roundabout mandatory',41:'End of no passing',42:'End no passing >3.5 tons'
}

# -------------------- Camera --------------------
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

print("\nSmart Traffic Sign Detection Started...\n")

# -------------------- Buffer --------------------
detected_buffer = []
buffer_size = 7

while True:
    start_time = time.time()   # ✅ FPS Start

    ret, frame = cap.read()
    if not ret:
        break

    img_display = frame.copy()

    # ✅ STEP 3.1 UI TEXT
    cv2.putText(img_display, "Driver Assistance Mode", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    cv2.putText(img_display, "System Active", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(img_gray, (5, 5), 0)
    edges = cv2.Canny(blur, 40, 130)
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    best_sign = None
    best_prob = 0
    best_box = None

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 2000:
            x, y, w, h = cv2.boundingRect(cnt)
            if w > 35 and h > 35:
                roi = img_rgb[y:y+h, x:x+w]
                try:
                    img = cv2.resize(roi, (32, 32)) / 255.0
                    img = np.expand_dims(img, axis=0)
                    preds = model.predict(img, verbose=0)
                    prob = np.max(preds)

                    if prob > 0.90 and prob > best_prob:
                        best_prob = prob
                        best_sign = classes[np.argmax(preds)]
                        best_box = (x, y, w, h)
                except:
                    pass

    if best_sign and best_box:
        detected_buffer.append(best_sign)
        if len(detected_buffer) > buffer_size:
            detected_buffer.pop(0)

        if detected_buffer.count(best_sign) > buffer_size // 2:
            x, y, w, h = best_box
            confidence = round(best_prob * 100, 2)

            cv2.rectangle(img_display, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img_display, f"{best_sign} ({confidence}%)", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            # IoT Logging
            if best_sign != last_logged_sign:
                time_now = datetime.now().strftime("%H:%M:%S")

                with open(log_file, 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([time_now, best_sign, confidence])

                print(f"Logged: {best_sign} at {time_now}")
                last_logged_sign = best_sign

            # Smart Driver Assistance
            if best_sign == "Stop":
                tts_queue.put("Critical Alert! Stop immediately")
                if arduino:
                    arduino.write(b'STOP\n')

            elif "Speed limit" in best_sign:
                tts_queue.put("Speed limit detected. Maintain speed")
                if arduino:
                    arduino.write(b'SPEED\n')

            elif best_sign in ["Children crossing", "Pedestrians"]:
                tts_queue.put("Warning! Pedestrian zone")
                if arduino:
                    arduino.write(b'STOP\n')

            else:
                tts_queue.put(f"{best_sign} detected")
                if arduino:
                    arduino.write(b'SPEED\n')

    else:
        if arduino:
            arduino.write(b'CLEAR\n')

    # ✅ STEP 3.2 FPS DISPLAY
    fps = int(1 / (time.time() - start_time))
    cv2.putText(img_display, f"FPS: {fps}", (10, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

    cv2.imshow("Smart Traffic Sign Detection", img_display)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# -------------------- Cleanup --------------------
cap.release()
tts_queue.put(None)

if arduino:
    arduino.write(b'CLEAR\n')

cv2.destroyAllWindows()
print("Program Closed Successfully")
