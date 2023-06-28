import cv2
image = cv2.imread('D:\\Study\\VS Code\\t1.jpg')
original = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 100, 255, 1)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
close = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel, iterations=10)

cnts = cv2.findContours(close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]

for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 6)
    ROI = original[y:y+h, x:x+w]
    print(x,y)
    break
cv2.namedWindow('canny', cv2.WINDOW_NORMAL)
cv2.imshow('canny', canny)
cv2.namedWindow('close', cv2.WINDOW_NORMAL)
cv2.imshow('close', close)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', image)
cv2.imshow('ROI', ROI)
cv2.imwrite('canny.png', canny)
cv2.imwrite('close.png', close)
cv2.imwrite('ROI.png', ROI)
cv2.imwrite('image.png', image)
cv2.waitKey(0)