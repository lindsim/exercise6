my_file = open("scores.txt")
rest_ratings = {}


for l in my_file: 
    line = l.rstrip()
    rest_ratings_list = line.split(':')
    rest_ratings[rest_ratings_list[0]] = rest_ratings_list[1]

ordered_rest_ratings = sorted(rest_ratings.items())

print rest_ratings

for name, rating in ordered_rest_ratings:
    print "Restaurant %s is rated at %s." % (name, rating)