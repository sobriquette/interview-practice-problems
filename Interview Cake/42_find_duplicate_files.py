import os
import hashlib

def sample_hash_file(path):
	num_bytes_to_read_per_sample = 4000
	total_bytes = os.path.getsize(path)

	hasher = hashlib.sha512()

	with open(path, 'rb') as file:
		if total_bytes < num_bytes_to_read_per_sample * 3:
			hasher.update(file.read())
		else:
			num_bytes_between_samples = \
				(total_bytes - num_bytes_to_read_per_sample * 3) / 2

			for offset_multiplier in range(3):
				start_of_sample = offset_multiplier * \
					(num_bytes_to_read_per_sample + num_bytes_between_samples)
				file.seek(start_of_sample)
				sample = file.read(num_bytes_to_read_per_sample)
				hasher.update(sample)

	return hasher.hexdigest()

def find_duplications(root_dir):
	file_dict = {}
	stack = [root_dir]
	res = []

	while stack:
		curr_path = stack.pop()

		if os.path.isfile(curr_path):
			file_hash = sample_hash_file(curr_path)
			last_edited_time = os.path.getmtime(curr_path)

			if file_hash in file_dict:
				existing_last_edited_time, existing_path = \
				file_dict[file_hash]

				if last_edited_time > existing_last_edited_time:
					duplicates.append((curr_path, existing_path))
				else:
					duplicates.append((existing_path, curr_path))
					file_dict[file_hash] = (last_edited_time, curr_path)
			else:
				file_dict[file_hash] = (last_edited_time, curr_path)
		else:
			for path in os.listdir(curr_path):
				full_path = os.path.join(curr_path, path)
				stack.append(full_path)

	return res