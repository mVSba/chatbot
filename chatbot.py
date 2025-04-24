import re

# Dictionary of keywords and their corresponding responses
RESPONSES = {
    "panic attack": [
        "Focus on your breathing. Try to take slow, deep breaths. Breathe in for 4 counts, hold for 2, and exhale for 6 counts.",
        "Remember that panic attacks are temporary and will pass. They typically peak within 10 minutes.",
        "Try the 5-4-3-2-1 grounding technique: Acknowledge 5 things you see, 4 things you can touch, 3 things you hear, 2 things you smell, and 1 thing you taste."
    ],
    "anxiety": [
        "Try to focus on the present moment. What's one small thing you can observe right now?",
        "Progressive muscle relaxation can help. Tense and then release each muscle group in your body, starting from your toes and working upward.",
        "Consider trying some gentle stretching or walking to help release tension in your body."
    ],
    "breathing": [
        "Box breathing can be helpful: breathe in for 4 counts, hold for 4, exhale for 4, and hold for 4. Repeat several times.",
        "Place one hand on your chest and one on your stomach. Try to breathe so that only your stomach hand rises, keeping your chest still."
    ],
    "heart racing": [
        "It's common for your heart to race during a panic attack. Remember that this is a normal bodily response and not dangerous.",
        "Try placing your hand over your heart and focusing on slowing your breathing. This can help slow your heart rate."
    ],
    "dizzy": [
        "If you're feeling dizzy, try sitting down and lowering your head slightly between your knees if possible.",
        "Stay hydrated and take slow, deep breaths to help reduce dizziness."
    ],
    "scared": [
        "It's okay to feel scared. Acknowledge the feeling without judgment, and remember that this feeling will pass.",
        "Try saying to yourself: 'This is anxiety. It's uncomfortable, but it cannot harm me.'"
    ],
    "help": [
        "I'm here to help. Try focusing on your breathing first - slow, deep breaths can help calm your nervous system.",
        "Would it help to try a grounding exercise? Try naming 5 things you can see around you right now."
    ],
    "technique": [
        "The 4-7-8 breathing technique can be effective: Breathe in for 4 seconds, hold for 7 seconds, and exhale for 8 seconds.",
        "Progressive muscle relaxation involves tensing and relaxing different muscle groups to reduce physical tension."
    ],
    "thank": [
        "You're welcome. I'm here anytime you need support.",
        "I'm glad I could help. Remember to be kind to yourself during this time."
    ]
}

# Default responses when no keywords match
DEFAULT_RESPONSES = [
    "I'm here with you. Try taking a few deep breaths - in through your nose for 4 counts, and out through your mouth for 6 counts.",
    "It might help to ground yourself. Can you name 5 things you can see right now?",
    "Remember that you're safe, and these feelings will pass. Would you like to try a calming technique?",
    "How are you feeling right now? Remember that panic attacks, while uncomfortable, are not dangerous and will subside.",
    "You're doing well by reaching out. Let's focus on your breathing for a moment. Can you take a slow, deep breath with me?"
]

# Counter for default responses
default_response_index = 0

def get_response(user_input):
    """
    Generate a response based on the user's input.
    
    Args:
        user_input (str): The user's message text
        
    Returns:
        str: The chatbot's response
    """
    global default_response_index
    
    # Convert to lowercase for easier matching
    user_input = user_input.lower()
    
    # Check for keywords in the user input
    for keyword, responses in RESPONSES.items():
        if keyword in user_input:
            # Return a response for the matched keyword
            # Use modulo to cycle through responses for the same keyword
            index = sum(ord(c) for c in user_input) % len(responses)
            return responses[index]
    
    # If no keywords match, use a default response
    response = DEFAULT_RESPONSES[default_response_index]
    
    # Update the default response index for next time
    default_response_index = (default_response_index + 1) % len(DEFAULT_RESPONSES)
    
    return response
