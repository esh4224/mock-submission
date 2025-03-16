
print('Anilate')
print("Welcome to Anilate, where we translate animal language into english!")
#Title
print('NOTICE: translation varies on different animals.')
print('Animal Languages Available')

array = ["cat", "dog", "bird", 'fish']

for animal in array:
    print('-'+animal)
#
choiceOfAnimal = input('please pick an animal\n').strip()

if choiceOfAnimal.lower() == "cat":
    print('Lets translate the language of a cat')
elif choiceOfAnimal.lower() == "dog":
    print('Lets translate the language of a dog')
elif choiceOfAnimal.lower() == 'bird':
    print('Lets translate the language of a bird')
elif choiceOfAnimal.lower() == 'fish':
    print('Lets translate the language of a fish')
elif choiceOfAnimal.lower() == 'bird':
    print('Lets translate the language of a bird')
elif choiceOfAnimal.lower() == 'fish':
    print('Lets translate the language of a fish')
else:
   print('please pick an animal from the following list')
catlist = [
    
        "Aelio: Food",
        "Lae: Milk",
        "Parriere: Open",
        "Aliloo: Water",
        "Bl: Meat",
        "Ptlee-bl: Mouse meat",
        "Bleeme-bl: Cooked meat",
        "Pad: Foot",
        "Leo: Head",
        "Pro: Nail or claw",
        "Tut: Limb",
        "Papoo: Body",
        "Oolie: Fur",
        "Mi-ouw: Beware",
        "Purrieu: Satisfaction or content",
        "Yow: Extermination",
        "Mieouw: Here"
]
   
if choiceOfAnimal.lower() == "cat":
      print('Lets start with the basics')
      print('Sounds:')
      print("Greeting:", "If a cat makes a short, high pitched meow, its often a sign of acknowledgement or greeting.")
   
      print("Request:", 'A mid-pitched meow could be a tender request for something like food, water, or playtime.')
      print('A longer, drawn-out meow might indicate a specific desire or a more insistent request. ')
      print('Repeated meows might signify excitement, or that the cat is trying to get your attention.')
      print('Meows accompanied by rubbing against your legs could mean your cat wants to be petted or wants your attention." ')
      print('Meows at certain times; If your cat meows consistently at certain times, its a good idea to check the food bowl or see if they need something else.')
      print('Feelings:', 'Higher-pitched meows can indicate that your cat is startled or hurt.')
      print('Lower-pitched meows can indicate anxiety, boredom, frustration, or even illness.')
      print('Excessive meowing could indicate that your cat is bored, anxious, confused, or that they have a medical problem.')
      
      print('And thats the end of the "Sounds"section!')
      
      print("[")
      for item in catlist:
        print(f'    "{item}",')
      print("]")

if choiceOfAnimal.lower() == 'dog':
     print('Lets start with the basics:')
     print('Barking:') 
     print('Short, sharp barks – Alert or excitement, example- Someones here!')
     print('Continuous barking with pauses – Warning or guarding behavior.')
     print('High-pitched, happy bark – Playfulness or excitement.')
     print('Low, slow barking – Threat or feeling uncomfortable.')
     print('Growling:')
     print('Low, deep growl – Warning or discomfort.')
     print('Play growl (softer, higher-pitched) – Excited and playful, not aggressive.')
     print('Growl followed by a bark – Feeling threatened but ready to act.')
     print('Whining/Whimpering:')
     print('Soft whimpering – Seeking attention, discomfort, or anxiety.')
     print('Persistent whining – Pain, stress, or a need (food, water, bathroom).')
     
     print('Whining while looking at something – Wanting something (like a toy or treat).')
     print('Howling:')
     print('Long, sustained howl – Communication (e.g., responding to sirens or calling pack members')
     print('Short, higher-pitched howls – Seeking attention or feeling lonely.')
     print('Other Vocalizations:')
     print('Sighing – Relaxation or mild frustration.')
     print('Moaning/Groaning – Comfort, enjoyment (often while being petted).')
     print('Snorting/Huffing – Mild frustration, excitement, or curiosity.')
     print('And thats the current definitions for as of now.')
if choiceOfAnimal.lower() == 'bird':
    print('Lets start with the basics:')
    print('Notice: There are no possible talking language for birds, rather body language.')
    print('Actions and meanings:')
    print('Standing on two feet- Im alright')
    print('Standing on one foot- Im relaxing')
    print('Standing on one foot, feathers fluffed- Im really relaxing')
    print('Standing on one foot, grinding beak- Im getting tired')
    print('Standing on one foot, hair fluffed, eyes glazed- Im trying to get some sleep')
    print('Head facing back, tucked under wing- Im sleeping')
    print('Tail shake- Ok,Im ready for something new, or im happy')
    print('Standing on one foot with head tucked backwards- Im cleaning my face')
    print('Standing on one foot with head tucked under- Just cleaning some feathers')
    print('Spread wings a little and rub face on back- Getting ready for some serious preening. ')
    print('')