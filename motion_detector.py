#1.     OBJECT SHAPED BOUNDARIES ---> Does not record the video

# import cv2

# cap = cv2.VideoCapture(0)
# frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# #fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# #out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))


# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     blur = cv2.GaussianBlur(gray, (5, 5), 0)
#     _, thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)

#     contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     # Draw shapes (contours) instead of rectangles
#     cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)

#     cv2.imshow("Shape Tracking", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# #out.release()
# cv2.destroyAllWindows()





#2.   Recording + Object Shaped Detection

import cv2

cap = cv2.VideoCapture(0)


frame_width = int(cap.get(3))  
frame_height = int(cap.get(4))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('motion_output.mp4', fourcc, 20.0, (frame_width, frame_height))

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)

    
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 800:
            continue
        cv2.drawContours(frame1, [contour], -1, (0, 255, 0), 2)

   
    cv2.imshow("Motion Detection", frame1)
    out.write(frame1)

    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()






