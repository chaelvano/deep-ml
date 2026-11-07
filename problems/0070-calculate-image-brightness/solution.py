def calculate_brightness(img):
	# Write your code here
	if not img:
		return -1

	if len(img) == 0:
		return -1

	width = len(img[0])

	if width == 0:
		return -1

	sum = 0

	for row in img:
		if len(row) != width:
			return -1

		for pixel in row:
			if pixel < 0  or pixel > 255:
				return -1

			sum += pixel

	return sum / (len(img) * len(img[0]))