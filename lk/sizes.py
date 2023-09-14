def size_by_height(height):
	match height:
		case hs if hs in range(0, 122):
			return (0,)

		case hs if hs in range(122, 128):
			return (28, 29, 30)

		case hs if hs in range(128, 134):
			return (30, 31, 32)

		case hs if hs in range(134, 140):
			return (32, 33, 34)

		case hs if hs in range(140, 146):
			return (34, 35, 36)

		case hs if hs in range(146, 152):
			return (36, 37, 38)

		case hs if hs in range(152, 158):
			return (38, 39, 40)

		case hs if hs in range(158, 164):
			return (42, 43, 44)

		case hs if hs in range(164, 170):
			return (44, 45, 46)

		case hs if hs in range(170, 176):
			return (46, 47, 48, 49, 50)

		case hs if hs in range(176, 182):
			return (48, 49, 50, 51, 52)

		case hs if hs in range(182, 194):
			return (50, 51, 52, 53, 54)

		case hs if hs in range(194, 201):
			return (56, 57, 58, 59, 60)

		case hs if hs > 201:
			return (1,)


def size_by_chest(chest_size):
	match chest_size:
		case cs if cs in range(0, 56):
			return (0,)

		case cs if cs in range(56, 60):
			return (28, 29, 30)

		case cs if cs in range(60, 64):
			return (30, 31, 32)

		case cs if cs in range(64, 68):
			return (32, 33, 34)

		case cs if cs in range(68, 72):
			return (34, 35, 36)

		case cs if cs in range(72, 76):
			return (36, 37, 38)
			
		case cs if cs in range(76, 80):
			return (38, 39, 40)

		case cs if cs in range(80, 84):
			return (40, 41, 42)

		case cs if cs in range(84, 88):
			return (42, 43, 44)

		case cs if cs in range(88, 92):
			return (44, 45, 46)

		case cs if cs in range(92, 96):
			return (46, 47, 48)

		case cs if cs in range(96, 100):
			return (48, 49, 50)

		case cs if cs in range(100, 104):
			return (50, 51, 52)

		case cs if cs in range(104, 108):
			return (52, 53, 54)
			
		case cs if cs in range(108, 112):
			return (54, 55, 56)

		case cs if cs in range(112, 116):
			return (56, 57, 58)

		case cs if cs in range(116, 120):
			return (58, 59, 60)

		case cs if cs > 120:
			return (1,)


def size_by_waist(waist_size):
	# not 100% reliable info
	match waist_size:
		case ws if ws in range(0, 74):
			return (0,)

		case ws if ws in range(74, 78):
			return (44, )

		case ws if ws in range(78, 82):
			return (46, )

		case ws if ws in range(82, 86):
			return (48, )

		case ws if ws in range(86, 90):
			return (50, )

		case ws if ws in range(90, 95):
			return (52, )

		case ws if ws in range(95, 100):
			return (54, )

		case ws if ws in range(100, 105):
			return (56, )

		case ws if ws in range(105, 110):
			return (58, )

		case ws if ws in range(110, 115):
			return (60, )

		case ws if ws in range(115, 120):
			return (62, )

		case ws if ws in range(120, 125):
			return (64, )

		case ws if ws in range(125, 130):
			return (66, )

		case ws if ws in range(130, 135):
			return (68, )

		case ws if ws in range(135, 140):
			return (70, )

		case ws if ws > 140:
			return (1, )


def jacket_size(height, chest, waist):
	"""Функция запрашивает у других функций соответствие размера, после чего складывает в общий список.
	Затем этот список сортируется по возрастанию."""
	sizes = sorted(size_by_height(height) + size_by_chest(chest) + size_by_waist(waist))
	if 0 in sizes:
		return "Не определено"
	elif 1 in sizes:
		return "Не определено"
	else:
		return f"{sizes[-2]} - {sizes[-1]}"


def shorts_size(hips):
	size = 0
	if hips <= 60:
		size = 0
	elif hips == 60:
		size = 30
	elif hips in range(61, 65):
		size = 32
	elif hips in range(65, 69):
		size = 34
	elif hips in range(69, 73):
		size = 36
	elif hips in range(73, 77):
		size = 38
	elif hips in range(77, 81):
		size = 40
	elif hips in range(81, 85):
		size = 42
	elif hips in range(85, 89):
		size = 44
	elif hips in range(89, 93):
		size = 46
	elif hips in range(93, 97):
		size = 48
	elif hips in range(97, 101):
		size = 50
	elif hips in range(101, 105):
		size = 52
	elif hips in range(105, 109):
		size = 54
	elif hips in range(109, 113):
		size = 56
	elif hips in range(113, 117):
		size = 58
	elif hips in range(117, 121):
		size = 60
	else:
		size = 1

	if size < 2:
		return "Не определено"
	else:
		return size


def shoes_size(foot):
	size = 0
	if foot < 20:
		size = 0
	elif foot == 20:
		size = 30
	elif 20 < foot <= 20.5:
		size = 31
	elif 20.5 < foot <= 21:
		size = 32
	elif 21 < foot <= 21.5:
		size = 33
	elif 21.5 < foot <= 22:
		size = 34
	elif 22 < foot <= 23:
		size = 35
	elif 23 < foot <= 23.5:
		size = 36
	elif 23.5 < foot <= 24:
		size = 37
	elif 24 < foot <= 24.5:
		size = 38
	elif 24.5 < foot <= 25:
		size = 39
	elif 25 < foot <= 25.5:
		size = 40
	elif 25.5 < foot <= 26:
		size = 41
	elif 26 < foot <= 27:
		size = 42
	elif 27 < foot <= 28:
		size = 43
	elif 28 < foot <= 28.5:
		size = 44
	elif 28.5 < foot <= 29:
		size = 45
	elif 29 < foot <= 29.5:
		size = 46
	elif 29.5 < foot <= 30:
		size = 47
	else:
		size = 1

	if size < 2:
		return "Не определено"
	else:
		return size
