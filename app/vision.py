import cv2

def look_if_closed(image_path, template_path='closed_template.jpg'):
	cap = cv2.VideoCapture(image_path)
	if(cap.isOpened()):
		ret, base = cap.read()

	template = cv2.imread(template_path, cv2.CV_LOAD_IMAGE_UNCHANGED)

	res = cv2.matchTemplate(base, template, cv2.TM_CCOEFF_NORMED)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

	return max_loc[0] > 5