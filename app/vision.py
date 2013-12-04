import cv2

def look_if_closed(image_path, template_path):
	base = cv2.imread(image_path, 0)
	template = cv2.imread(template_path, 0)

	res = cv2.matchTemplate(base, template, cv2.TM_CCOEFF_NORMED)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

	return max_loc[0] > 5