import Relay_module
import Wave_module
import cv2
import numpy as np
import time
import cameraModule
import paho.mqtt.client as mqtt
import ssl
import json
import _thread
import time
import Loadcell_module
import os
pins = []

def setUp():
    # Set up module
    Relay_module.relay_setup()
    Wave_module.TRIG_ECHO_set()
    
def publishData_default(logDate, excretaSeperation, excretaState,imgPathS3,weight,deviceId = 12345678):
    print(f"{deviceId}/dogLog")
    print(json.dumps({"deviceId":deviceId,"logDate":logDate,"excretaSeperation":excretaSeperation,"excretaState":excretaState,"imgPathS3":imgPathS3,"weight":weight}))
    client.publish(f"{deviceId}/dogLog", payload=json.dumps({"logDate":logDate,"excretaSeperation":excretaSeperation,"excretaState":excretaState,"imgPathS3":imgPathS3,"weight":weight}),qos=0, retain=False)
    time.sleep(5)

def publishData_alarm(userId, content, alarmDate,deviceId = 12345678):
    
    client.publish(f"{deviceId}/alarm", payload=json.dumps({"userId":userId,"content":content,"alarmDate":alarmDate}),qos=0, retain=False)
    time.sleep(5)

# yolo
def process_image(image_path):
    # Load YOLO
    net = cv2.dnn.readNet("/home/itsmung/final/custom-yolov4-tiny-detector_final.weights", "/home/itsmung/final/custom-yolov4-tiny-detector.cfg")
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    # Load image
    img = cv2.imread(image_path) 
    img = cv2.resize(img, None, fx=0.4, fy=0.4)
    height, width, channels = img.shape

    # Preprocess the image
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    # Pass the blob to the network and get the bounding boxes, confidences and classIDs
    net.setInput(blob)
    outs = net.forward(output_layers)

    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
           
            if confidence > 0.1:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Apply non-max suppression
    indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # Load the classes
    with open("./coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
    # Draw the bounding box on the image
        returnValue = 0
        for i in indices:
            print("label analyze")
            i = i[0]
            box = boxes[i]
            x = box[0]
            y = box[1]
            w = box[2]
            h = box[3]
            label = str(classes[class_ids[i]])
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            print(label)
            # Return 1 if 'dog' is detected, 2 if 'donut' is detected, 0 otherwise
            if label == 'dog' or label == "Dog":
                returnValue = 1
            elif label == 'blood':
                returnValue = 3
            elif label == 'normal':
                returnValue = 2
        
    # # Show the image
    # cv2.imshow("Image", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return returnValue



# while dogId == "":
def mainAct(test):
    # situation.
    hx = Loadcell_module.main()
    # Obtain userId for wifi communication. Update userId videoPath, regStatus based on devicedId in the device table


    # DB userId : have processDogId based on userId data in DB

    # setup
    # instance
    deviceId = 12345678
    userId = "test" 
    dogId = ""
    logDate = ""
    excretaSeperation = ""
    excretaState = ""
    imgPathS3 = ""
    imgPath = ""
    picturePath = "/home/itsmung/final/img/"
    weight = 5
    dog_check = False
    poop_check = False

    # for alarm
    content = ""
    alarmDate = ""

    # for device table
    videoPath = ""
    regStatus = ""

    #while True:
        # when weight increase
        # weight 
        # use Yolov4-tiny
        # checking weight middle value
    while True :
        weight_increasing = False
        # before_weight = None
        # while weight_increasing:  # Add a loop here to continuously get weights until the program is interrupted
        #     now_weight = Loadcell_module.get_weights(hx)
        #     if now_weight is not None:
                
        #         if before_weight is not None:
        #             diff_weight = before_weight - now_weight
        #             print(f"diff_weight: {diff_weight}")
        #             if diff_weight > -3000 and diff_weight <3000:
                    
        #                 continue
                
        #             else :
        #                 weight_increasing = False
        #         print(f"before : {before_weight}")
        #         print(f"now : {now_weight}")
        #         before_weight = now_weight
                
        #     time.sleep(0.1)  # Add a small delay of 0.1 seconds
        # #Loadcell_module.clean_and_exit()

        if(not weight_increasing) :
            dog_check= True
            while dog_check:
                time.sleep(1)
                #cameraModule.picture()  take picture return timestamp
                timestamp = cameraModule.picture()
                timestamp = timestamp + ".jpg"
                imgPath = picturePath + timestamp
                #imgPath = "/home/itsmung/final/img/dog.jpg"
                print(imgPath)
                labelValue = process_image(image_path= imgPath)
                print(labelValue)
                if labelValue == 1:
                    dog_check = True
                    os.remove(imgPath)
                    print(f"dogCheck :{dog_check}")
        
                
                else :
                    dog_check = False
                    print(f"dogCheck :{dog_check}")
                    
                # input data based on userId.
                # logDate excretaSeperation excretaState imagePath(aws) , weight
                #if blood , content, alarmDate == logDate
            print("while out")
        
            image_path = "/home/itsmung/final/img/donut.jpg"
            detection_value = process_image( imgPath)
            if detection_value == 2:
                print(f"donutCheck :normal")
                excretaSeperation = "poop"
                excretaState = "normal"
                logDate = cameraModule.nowTime()
                day , hour = logDate.split('_')
                logDate = day + " " + hour
                imgPathS3 = deviceId
                
                #weight
                publishData_default(deviceId = deviceId, logDate = logDate, excretaSeperation = excretaSeperation,  excretaState = excretaState,imgPathS3= imgPathS3,weight= weight)  
                print("publish")
                Relay_module.control_relay(19,0)
                time.sleep(5)
                Relay_module.control_relay(26,0)
                time.sleep(10)
                # water pump
                Relay_module.control_relay(19,1)
                time.sleep(20)
                Relay_module.control_relay(26,1)
            elif detection_value == 3 :
                print(f"donutCheck :blood")
                excretaSeperation = "poop"
                excretaState = "blood"
                logDate = cameraModule.nowTime()
                day , hour = logDate.split('_')
                logDate = day + " " + hour
                imgPathS3 = deviceId
            
                #weight
                publishData_default(deviceId = deviceId, logDate = logDate, excretaSeperation = excretaSeperation,  excretaState = excretaState,imgPathS3= imgPathS3,weight= weight)  
                print("publish")
                # for alarm
            
                
                content = "blood is detected. Please come to hospital soon."
                
                alarmDate = logDate
                publishData_alarm(deviceId = deviceId, userId= userId, content = content, alarmDate=alarmDate)
                Relay_module.control_relay(19,0)
                time.sleep(5)
                Relay_module.control_relay(26,0)
                time.sleep(10)
                # water pump
                Relay_module.control_relay(19,1)
                time.sleep(20)
                Relay_module.control_relay(26,1)
            else :
                print(f"donutCheck : nothing")
                os.remove(imgPath)
                excretaSeperation = "pee"
                excretaState = ""
                logDate = cameraModule.nowTime()
                day , hour = logDate.split('_')
                logDate = day + " " + hour
                imgPathS3 = ""
                #weight
                publishData_default(deviceId = deviceId, logDate = logDate, excretaSeperation = excretaSeperation,  excretaState = excretaState,imgPathS3= imgPathS3,weight= weight)  
                print("publish")
                # water pump
                print("relay control")
                Relay_module.control_relay(19,0)
                time.sleep(5)
                Relay_module.control_relay(26,0)
                time.sleep(10)
                # water pump
                Relay_module.control_relay(19,1)
                time.sleep(20)
                Relay_module.control_relay(26,1)
                
            # wave_check
            # water
            distance = Wave_module.wave_measurement(0)
            if distance is not None:
                content = "water is lack. You have to Fill it with water."
                logDate = cameraModule.nowTime()
                day , hour = logDate.split('_')
                alarmDate = day + " " + hour
                print(content)
                publishData_alarm(deviceId = deviceId, userId= userId, content = content, alarmDate=alarmDate)
            # pee bottle
            distance2 = Wave_module.wave_measurement(1)
            if distance2 < 5:
                content = "Pee bottle is full. You have to empty it."
                logDate = cameraModule.nowTime()
                day , hour = logDate.split('_')
                alarmDate = day + " " + hour
                print(content)
                publishData_alarm(deviceId = deviceId, userId= userId, content = content, alarmDate=alarmDate)
    





setUp()

def on_connect(client,userdata, flags, rc):
    print("Connected to AWs IoT : "+ str(rc))

client = mqtt.Client()
client.on_connect = on_connect
# aws key
client.tls_set(ca_certs="/home/itsmung/final/awsKey2/AmazonRootCA1.pem", certfile="/home/itsmung/final/awsKey2/3107b678ef8f8fb7b65aef58b863a04694a2adf5dfe3b0955a3f532c352de108-certificate.pem.crt", keyfile='/home/itsmung/final/awsKey2/3107b678ef8f8fb7b65aef58b863a04694a2adf5dfe3b0955a3f532c352de108-private.pem.key',tls_version=ssl.PROTOCOL_SSLv23)
client.tls_insecure_set(True)

# client: It refers to the MQTT client object. This object is used to manage MQTT communication and interact with the broker.

# .connect(): This is the method used to connect to the MQTT broker. By calling this method, the client can establish a connection with the specified broker.

# "TBD": It represents the address of the MQTT broker. You should replace this placeholder with the actual IP address or domain name of the broker. "TBD" stands for "To Be Determined," indicating that the address has not been determined yet. You need to replace this part with the actual broker address.

# 8883: It denotes the port number of the MQTT broker. Typically, MQTT communication using TLS/SSL for secure connections utilizes port 8883. The actual port number may vary depending on the broker's configuration.

# 60: It represents the connection timeout duration. It specifies the maximum time (in seconds) that the client will attempt to connect to the broker. For example, setting it to 60 means the client will try to connect to the broker for a maximum of 60 seconds, and if the connection fails within that time, it will be considered a failed connection attempt.
client.connect("a1nfogarwziq36-ats.iot.ap-northeast-2.amazonaws.com",8883,60)



_thread.start_new_thread(mainAct, ("Spin-up new Thread...",))

client.loop_forever()






  