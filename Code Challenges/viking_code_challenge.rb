def not_string
	while true
		puts "Enter a string"
		my_string = gets.chomp
		if !my_string.start_with?("not")
			puts "not " + my_string
		else
			puts my_string
		end
	end
end

def flim_flam
	for i in 1..100
		if i % 15 == 0
			puts "FLIMFLAM"
		elsif (i % 3 == 0) && (i % 15 != 0)
			puts "FLIM"
		elsif (i % 5 == 0) && (i % 15 != 0)
			puts "FLAM"
		else
			puts i
		end
	end
end

def no_dupes(num_array)
	sorted_array = Array.new
	num_array.each do |num|
		unless sorted_array.include? (num)
			sorted_array.push(num)
		end 
	end

	sorted_array.each do |num|
		puts num
	end
end