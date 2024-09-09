# mad lib example for functions
def madlib(adjective_1,noun_1,noun_2,verb_1,adjective_2,noun_3,verb_2,adjective_3,verb_3,noun_4,adjective_4):
    '''Mad Lib function'''



    story = f'''Puppies are known for their {adjective_1} energy and their ability to bring joy to any {noun_1} . Whether they are playing with a {noun_2} or learning to {verb_1} , their curious nature is always on display. It’s impossible not to smile when you see a puppy wagging its tail with {adjective_2} excitement. Taking care of a puppy requires a lot of responsibility. You have to make sure they get enough {noun_3} and teach them how to properly {verb_2} . It’s important to create a {adjective_3} routine so the puppy feels safe and comfortable in its new home. With time and patience, your puppy will learn to {verb_3} and become a well_behaved companion. The best part about having a puppy is watching them grow and develop their own {noun_4} . They’ll always remember the love and care you give them, and in return, they’ll show you endless {adjective_4} loyalty. Whether they’re snuggling on the couch or chasing a ball, puppies remind us of the pure joy that comes from simple moments.'''

    return story
# now put in our arguments into out output_story variable
output_story = madlib('Fierce','house','couch','barked','adjective_2','Donald Trump','pissed','smelled','threw-up','Main Campus','undying')
print(output_story)