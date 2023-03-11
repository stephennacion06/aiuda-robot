import cv2
import numpy as np



def detect_color(img):
  global out

  roi_left = {
    "x": 302,
    "y": 431,
    "w": 60,
    "h": 40,
  }

  roi_center = {
    "x": 422,
    "y": 431,
    "w": 60,
    "h": 40,
  }

  roi_right = {
    "x": 542,
    "y": 431,
    "w": 60,
    "h": 40,
  }

  # red_max,red_min = 140, 120
  # green_max, green_min = 90, 70
  # blue_max, blue_min = 140, 120

	
  red_max,red_min = 145, 115
  green_max, green_min = 100, 70
  blue_max, blue_min = 145, 115

  left_clear = True
  center_clear = True
  right_clear = True
   


  left_roi_values = img[roi_left["y"]:roi_left["y"]+roi_left["h"], roi_left["x"]:roi_left["x"]+roi_left["w"]]
  center_roi_values = img[roi_center["y"]:roi_center["y"]+roi_center["h"], roi_center["x"]:roi_center["x"]+roi_center["w"]]
  right_roi_values = img[roi_right["y"]:roi_right["y"]+roi_right["h"], roi_right["x"]:roi_right["x"]+roi_right["w"]]
  

  left_mean_blue = int(np.mean(left_roi_values[:,:,0]))
  left_mean_green = int(np.mean(left_roi_values[:,:,1]))
  left_mean_red = int(np.mean(left_roi_values[:,:,2]))


  center_mean_blue = int(np.mean(center_roi_values[:,:,0]))
  center_mean_green = int(np.mean(center_roi_values[:,:,1]))
  center_mean_red = int(np.mean(center_roi_values[:,:,2]))

  right_mean_blue = int(np.mean(right_roi_values[:,:,0]))
  right_mean_green = int(np.mean(right_roi_values[:,:,1]))
  right_mean_red = int(np.mean(right_roi_values[:,:,2]))

  f = open("rbg_readings.txt", "a")
  rgb_text = "left: {},{},{}; center: {},{},{} right: {},{},{} \n".format(left_mean_red, left_mean_green, left_mean_blue, center_mean_red, center_mean_green, center_mean_blue, right_mean_red, right_mean_green, right_mean_blue)
  f.write(rgb_text)
  f.close()

  if (red_min <= left_mean_red <= red_max) and (green_min <= left_mean_green <= green_max) and (blue_min <= left_mean_blue <= blue_max):
    left_box = cv2.rectangle(img, (roi_left["x"],roi_left["y"]), (roi_left["x"]+roi_left["w"],roi_left["y"]+roi_left["h"]),(0, 255, 0), 2)
    left_clear = True
  else:
    left_box = cv2.rectangle(img, (roi_left["x"],roi_left["y"]), (roi_left["x"]+roi_left["w"],roi_left["y"]+roi_left["h"]),(255, 0, 0), 2)
    left_clear = False

  if (red_min <= center_mean_red <= red_max) and (green_min <= center_mean_green <= green_max) and (blue_min <= center_mean_blue <= blue_max):
    center_box = cv2.rectangle(img, (roi_center["x"],roi_center["y"]), (roi_center["x"]+roi_center["w"],roi_center["y"]+roi_center["h"]),(0, 255, 0), 2)
    center_clear = True 
  else:
    center_box = cv2.rectangle(img, (roi_center["x"],roi_center["y"]), (roi_center["x"]+roi_center["w"],roi_center["y"]+roi_center["h"]),(255, 0, 0), 2)
    center_clear = False

  if (red_min <= right_mean_red <= red_max) and (green_min <= right_mean_green <= green_max) and (blue_min <= right_mean_blue <= blue_max):
    right_box = cv2.rectangle(img, (roi_right["x"],roi_right["y"]), (roi_right["x"]+roi_right["w"],roi_right["y"]+roi_right["h"]),(0, 255, 0), 2)
    right_clear = True
  else:
    right_box = cv2.rectangle(img, (roi_right["x"],roi_right["y"]), (roi_right["x"]+roi_right["w"],roi_right["y"]+roi_right["h"]),(255, 0, 0), 2)
    right_clear = False

  #SPEED VALUE
  speed=0.0
  
  font = cv2.FONT_HERSHEY_SIMPLEX
  
  if left_clear == True and center_clear == True and right_clear == True:
    cv2.putText(img,  
                'MOVE STRAIGHT',  
                (50, 50),  
                font, 1,  
                (0, 255, 255),  
                2,  
                cv2.LINE_4)
    speed=4.0
  elif left_clear == False and center_clear == True and right_clear == True:
    cv2.putText(img,  
                'STEER RIGHT',  
                (50, 50),  
                font, 1,  
                (0, 255, 255),  
                2,  
                cv2.LINE_4)
    speed=4.0
  elif left_clear == True and center_clear == False and right_clear == True:
    cv2.putText(img,  
                'STOP',  
                (50, 50),  
                font, 1,  
                (0, 255, 255),  
                2,  
                cv2.LINE_4)
    speed=0.0
  elif left_clear == True and center_clear == True and right_clear == False:
    cv2.putText(img,  
                'STEER LEFT',  
                (50, 50),  
                font, 1,  
                (0, 255, 255),  
                2,  
                cv2.LINE_4)
    speed=4.0
  else:
    cv2.putText(img,  
                'STOP',  
                (50, 50),  
                font, 1,  
                (0, 255, 255),  
                2,  
                cv2.LINE_4)
    speed=0.0                
  return img,speed
