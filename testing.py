# import openai
# from openai import OpenAI
# import os
# from pydantic import BaseModel
# import re
# import time
# import difflib

# os.environ["OPENAI_API_KEY"] = "API KEY HERE"

# client = OpenAI()
# #final
# counter = 0
# conversation_history = []
# past_events_context = ""
# non_abridged_convo_history = []
# non_abridged_summarized_history = []



# skills = {
#     "Mining": 1,
#     "Farming": 1,
#     "Combat": 1,
#     "Enchanting": 1,
#     "Dungeoneering": 1,
#     "Fishing": 1,
#     "Foraging": 1,
#     "Alchemy": 1,
#     "Heart of the Mountain": 1
# }

# # Skill level caps
# skill_caps = {
#     "Mining": 50,
#     "Farming": 50,
#     "Combat": 50,
#     "Enchanting": 50,
#     "Dungeoneering": 50,
#     "Fishing": 50,
#     "Foraging": 50,
#     "Alchemy": 50,
#     "Heart of the Mountain": 10
# }

# def level_up_skill(input_string):
#     response = openai.chat.completions.create(
#     model="gpt-3.5-turbo",
#     temperature=0.0,
#     messages= [
#         {
#             "role": "system",
#             "content": "Analyze the following passage and identify any skill-level changes that occur. Return the results in the format '[INSERT SKILL NAME]: [INSERT SKILL LEVEL]' for each skill that leveled up. if no skill leveled up return null. PASSAGE: "
#         },
#         {
#             "role": "user",
#             "content": input_string
#         }
#     ]
    
# )
#     response = response.choices[0].message.content.strip()
#     print(response)
#     if "null" in response.lower():
#         return
    
#         global skills  # Declare that we will use the global skills variable
#     update_string = response
#     lines = update_string.strip().split('\n')
    
#     for line in lines:
#         if not line.strip():
#             continue

#         # Split skill name and level
#         skill_part, level_part = line.split(':', 1)
#         skill_name = skill_part.strip()
#         new_level_str = level_part.strip()

#         # Attempt to convert new level to integer
#         try:
#             new_level = int(new_level_str)
#         except ValueError:
#             continue

#         # Find the matching skill key ignoring case
#         matched_key = None
#         for key in skills:
#             if key.lower() == skill_name.lower():
#                 matched_key = key
#                 break

#         if matched_key is not None:
#             if (new_level <= skill_caps[matched_key]):
#                 skills[matched_key] = new_level


# level_up_skill("Skill Level Up: Mining 7! \nYou've reached Mining Level 7! Your hours of dedication have paid off, and you're ready to take on even more mining challenges. What's next on your agenda?")
# print(skills["Mining"])


badThings = [f"Instead of going to bed at a reasonable time, you ***HERE***. When you get to school the next day you do a little worse on a in class assignment that you should.",f"You had a bunch of homework to do tonight, but you don't want to think about as it's stressing you out, so intead you ***HERE***. ",f"You had a big day, you were up super late but before you go to bed you NEED to play at least an hour. You decide to ***HERE***. The next morning when you wake up, only 4 hours later you realize how bad you screwed up. It's ok, you take your ADHD medication, a stimulant, and forces you awake and makes you feel like you have energy.",f"Its been a couple of nights of bad sleep but this puts you over the edge and you can barely peel youself out of bed after ***HERE*** all night long. Because of this you don't focus super well in class the next day. But, even worse you can feel, your medication becoming less effective, but its enough to keep you going for now.",f"As you finished ***HERE*** you see the sun spill into your room through your curtains, you have barely slep for the last month, you take your pills as you get ready to head to school, as you step into class, the flourecent lights make your eyes ache and you can tell that it is not going to be a good day. As you sit down you realize that you are barely able to keep your eyes open, and then, you're sleeping. The teacher notices, of course she does, you're sleeping in the front row. She pulls you aside after class, she asks, \"Is everything ok?\". What can you even say back?"]

print(len(badThings))