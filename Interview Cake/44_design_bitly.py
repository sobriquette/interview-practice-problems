bit.ly

"""
WHAT
- web interface, or api?
- can users modify or delete links?
- if links cannot be deleted, do they last forever or will they expire?
	- consider deleting links that were created X time ago?
	- consider deleting links that were visited X time ago?

- should users be able to customize shortlink? or is it autogenerated?

OPTIMIZE
- how quickly url is generated
- url storage
- following shortlink should be fast
- shortlink should be resilient to load spikes

DATA MODEL
slug, destination

ENDPOINT
ca.ke/api/v1/shortlink

POST request
curl --data '{"destination": "interviewcake.com"}' https://ca.ke/api/v1/shortlink
"""
import random

def shortlink(request):
	if request['method'] is not 'POST':
		return Response(501)

	destination = request['data']['destination']

	if 'slug' in request['data']:
		slug = request['data']['slug']
	else:
		slug = generate_random_slug()

	DB.insert({'slug': slug, 'destination': destination})

	response_body = {
		'slug': slug,
	}

	return Response(200, json_dumps(response_body))

def redirect(request):
	destination = DB.get({'slug': request['path']})['destination']
	return Response(302, destination)

# this approach may require a lot of re-rolls
# as we get more collisions
def generate_random_slug():
	chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
	max_slug_len = 7
	return ''.join([random.choice(chars) for i in range(max_slug_len)])

# use base conversion to generate slugs
def generate_random_slug():
	global current_slug_id
	while True
		slug = base_conversion(current_slug_id, base_62_alphabet)
		current_slug_id += 1

		existing = DB.get({'slug': slug})
		if not existing:
			return slug

