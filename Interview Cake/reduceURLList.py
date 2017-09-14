def reduceURLList(urls):
	triple_w = 'www.'
	url_dict = {}
	url_dict[triple_w] = {}

	for u in urls:
		if u[0:4] == triple_w:
			if u[4] in url_dict[triple_w]:
				url_dict[triple_w][u[4]].append(u[5:])
			else:
				url_dict[triple_w][u[4]] = u[5:]
		else:
			if u[0] in url_dict:
				url_dict[u[0]].append(u[1:])
			else:
				url_dict[u[0]] = u[1:]

	return url_dict