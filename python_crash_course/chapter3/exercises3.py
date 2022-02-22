## 3-1. Names -------------------------------------------------------------------
# store the names of a few of your friends in a list called names. Print each person's
# name by accessing each element in the list, one at a time.
names = ["michael", "omar", "cindy", "dave", "zo"]
for name in names:
  print(name.title())

## 3-2. Greetings --------------------------------------------------------------
# Start with the list you used in Exercise 3-1, but instead of just printing each
# person's name, print a message to them. The text of each message should be the same,
# but each message should be personalized with the person's name.
for name in names:
  message = f"Hey {name.title()}, I've missed you."
  print(message)

# 3-3. Your Own List ----------------------------------------------------------
# Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples. Use your list
# to print a series of statements about these items, such as "I would like to own
# Honda motocycle."
my_transporation = ["I want a bug to hop on and check-in with friends.",
  "I own a Honda CRV.",
  "I want a van to travel the world.",
  "I love to ride my bicycle."]

for transport in my_transporation:
  print(transport)

# 3-4. Guest List -------------------------------------------------------------
# if you could invite anyone, living or deceased, to dinner, who would you invite?
# Make a list that includes at least three people you'd like to invite to dinner.
# Then use your list to print a message to each person inviting them to dinner.
guest_list = ["Emma Stone", "Awkwafina", "Becky G", "Diane Guerrero"]
for guest in guest_list:
  invite = f"Dear {guest}, I am hosting a celebration and would be honored to have you join us."
  print(invite)

# 3-5. Changing Guest List ----------------------------------------------------
# you just heard that one of your guests can't make the dinner, so you need to send out
# a new set of invitations. You will have to think of someone else to invite.

# 1) start with your program from Exercise 3-4. Add a print() call at the end of your
# program stating the name of the guest who can't make it.
canceled_guest = "Emma Stone"
message = f"Unfortunately, {canceled_guest} won't be able to join us for the party."
print(message)

# 2) modify your list, replacing the name of the guest who can't make it with the name
# of the new person you are inviting.
new_guest = "Jennifer Lopez"
guest_list.remove(canceled_guest)
guest_list.append(new_guest)
print(guest_list)

# 3) Print a second set of invitation messsages, one for each person who is still
# in your list
for guest in guest_list:
  invite = f"Dear {guest}, I am hosting a celebration and would be honored to have you join us."
  print(invite)

# 3-6. More Guests ------------------------------------------------------------
# you just found a bigger dinner table, so now more space is available. Think of
# three more guests to invite to dinner. Add a new guest to the beginning and middle
# of the list using insert and lastly a guest to the end of the list and
# print out a new set of invitations.
print(guest_list)

update = "I just found a bigger dinner table!"
guest_list.insert(0, "Zo Antonow")
guest_list.insert(3, "Agnes Pham")
guest_list.append("Mom")

for guest in guest_list:
  invite = f"Dear {guest}, I am hosting a celebration and would be honored to have you join us."
  print(invite)

# 3-7. Shrinking Guest List ---------------------------------------------------
# You just found out that your new dinner table won’t arrive in time for the dinner,
# and you have space for only two guests. Write a message letting people know what
# happened and remove guests until you have two people left. For each guest you
# uninvite, write them a message. Finally use del to remove the last guests from your list
smaller_party_message = "Hey! I can only have two people over for the party because my table won't come in time."
print(smaller_party_message)

while len(guest_list) > 2:
  popped_guest = guest_list.pop()
  uninvite_message = f"Hey {popped_guest}, unfortunately I won't be able to host you at the party. I am planning something bigger for next month and hope to see you then instead!"
  print(uninvite_message)

print(guest_list)

while len(guest_list) > 0:
  del guest_list[0]

print(guest_list)

# 3-8. Seeing the World ---------------------------------------------------
# think of the least five places in the world you'd like to visit.
least_visit = ["Arizona", "South Carolina", "Texas", "Florida", "Arkansas"]
print(least_visit)
# sort the list without changing the list
print(sorted(least_visit))
# sort the list in reverse alphabetical order without changing the list
print(sorted(least_visit, reverse = True))
# print the list to show that the original list hasn't changed
print(least_visit)
# permanently reverse the order and show the original list has changed
least_visit.reverse()
print(least_visit)
# permanently reverse the order again
least_visit.reverse()
print(least_visit)
# permanently sort the order of the list
least_visit.sort()
print(least_visit)
# permanently reverse sort the order of the list
least_visit.sort(reverse=True)
print(least_visit)

# 3-9. Dinner Guests ------------------------------------------------------
# Working with one of the programs from Exercises 3-4 through 3-7 (page 42),
# use len() to print a message indicating the number of people you are
# inviting to dinner.
guest_list = ["Emma Stone", "Awkwafina", "Becky G", "Diane Guerrero"]
message = f"I am inviting a total of {len(guest_list)} people to my home."
print(message)

# 3-10. Every Function ----------------------------------------------------
# Think of something you could store in a list. For example, you could make a
# list of mountains, rivers, countries, cities, languages, or any- thing else
# you’d like. Write a program that creates a list containing these items and
# then uses each function introduced in this chapter at least once.

