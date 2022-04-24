DASHES = "--------------------------------------------------------------------------"

mental_tasks = ["If you're stuck doing something that lowers your confidence, do something you're good at.", "Take regular breaks from work! Sometimes, 5 minutes is all you need to feel refreshed!", "Don't be afraid to admit your feelings about a matter! Stay true to yourself and to others :)"]

physical_tasks = ["Try to get some physical activity throughout the day- it could even be taking a short walk!", "Eat food from ALL food groups; this keeps your body fueled.", "Drink a lot of water! it seems stupid, but it is known to make your appearance less puffy and is a great energizer!"]

social_tasks = ["Ask for help when you need it! If you would help someone in your shoes, others would probably help you too!", "Learn to say NO! It may seem hard to believe, but saying no is completely understandable and is human nature!", "Take a risk and approach people! You're rejecting yourself from their group if you don't!"]

men_keys = ["uninterest", "terrible at", "suck", "anxious", "nervous", "sad", "angry", "frustrate", "scare"]
phys_keys = ["ugly", "unathletic", "slow", "weak", "scrawny", "manly", "feminine", "nauseous", "sick", "hate myself", "looks", "muscular"]
soc_keys = ["lone", "friendless", "unpopular", "backstab", "abandon", "split", "break up", "cheater", "ignore", "overlook", "hate me", "betray"]

print("Welcome to Venout, your virtual best friend, therapist, advisor and so much more <3")
print(DASHES)

def new_ventor():#gives new users directions on what to do and how to do it
  more_questions = True
  FAQ_dict = {"Are my answers saved anywhere?" : "Not without your permission! We don't collect any personal information or stats pertaining to you, nor do we collect your vents!", "Do you give me tips on what I should do based on my vent?" : "Yes, we do! By analyzing your vent for specific things, we can give you suggestions on what you can do to make yourself happier!", "How long do vents have to be?": "In order to get the best results from your session, we recommend no longer than 100 words. However, this is just a suggestion to get better tips- you can make your vent as long as you want!"}
  
  #they can choose any question from the spread and Venout will answer them
  print(f"""At Venout's venting quarters, you can let go of all of your concerns without having to hold anything back. 
If you have any burning questions about the platform, feel free to check the FAQs below!
{DASHES}""")

  q_list = list(FAQ_dict.keys()) #converts the keys of the dictionary to a list to support later accessing attempts
  for question in q_list:
    print(question)
  
  print(DASHES)#just printing dashes to clean up display
    
  while more_questions:
    
    user_res = input("Would you like to learn more about any of these questions? Y/N ")
    
    if user_res == "Y":
      #if the user would like to see the answers to some of the questions
      ques_num = int(input("Which one? "))
      user_key = q_list[ques_num-1]
      print(FAQ_dict[user_key])
      
    elif user_res == "N":
      #if the user is done asking questions
      print("Welcome to Venout :)")
      more_questions = False
      
    else:
      #if the user types an unnaccepted response
      print("Whoopsies! That's not an option :( Type 'Y' if you would like to see some of these                   questions' answers or 'N' if you would not.")
      continue
  
def start_vent():
  word_limit = 100
  n_vent = input("Would you like to start a new vent? Y/N ")
  if n_vent == "Y":
    print(f"""Tell Venout what you're feeling. What emotions/memories are coming up to the surface?  
{DASHES}""")
    vent = input(f"(For best results, please keep your vents under {word_limit} words) \n")[:word_limit]
    return vent
  elif n_vent == "N":
    print("Alrighty, have a great day!")
  else:
    print("Whoopsies! That's not an option :( Type 'Y' if you would like to start a new vent                   or 'N' if you would not.")
    
  
def analyze_vent(vent_str, men_list, phys_list, soc_list):
  phys_count = 0
  men_count = 0
  soc_count = 0
  
  vent = vent_str.split()
  for word in vent:
    for m_item in men_list:
      if m_item in word:
        men_count +=1
    for p_item in phys_list:
      if p_item in word:
        phys_count +=1
    for s_item in soc_list:
      if s_item in word:
        soc_count +=1
  count_list = [men_count, phys_count, soc_count]
  return count_list


def share_tips(count_list):
  men_c, phys_c, soc_c = count_list
  print("Based on your rant, this is what Venout thinks you should hear. Remember, these are just meant to make you happier, not to look a certain way to others!")
  if men_c > 0:
    print(DASHES)
    print('Here are some easy things you could do to improve your mental health! -Venout \n')
    for tip in mental_tasks:
      print(tip)
  if phys_c > 0:
    print(DASHES)
    print('Here are some easy things you could do to improve your physical health! -Venout')
    for tip in physical_tasks:
      print(tip)
  if soc_c > 0:
    print(DASHES)
    print('Here are some easy things you could do to improve your social health! -Venout')
    for tip in social_tasks:
      print(tip)
  if men_c + phys_c + soc_c == 0:
    print(DASHES)
    print("Venout can't find anything to encourage you to improve upon. However, if you feel that we have gotten it wrong and should give you some tips, you could help others get the help they need by sharing your vent with Venout (coming soon)! This is fully optional though, so don't feel forced to do anything!")
is_new = input("Are you new to Venout? Y/N ")
if is_new == 'Y':
  new_ventor()
print(DASHES)

keep_venting = True

while keep_venting:
  my_vent = start_vent()
  counts = analyze_vent(my_vent, men_keys, phys_keys, soc_keys)
  print(DASHES)
  share_tips(counts)

  print(DASHES)
  vent_inp = input("Keep venting? Y/N ")
  
  if vent_inp == 'N':
    keep_venting = False
