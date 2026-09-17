# Each choice gives one point to every cluster in its list.
CLUSTERS = {
    "Communications": "You might enjoy designing visuals, taking photos, or editing videos for MISA.",
    "Office of the Secretary General": "You might enjoy organizing documents and keeping project operations in order.",
    "Marketing": "You might enjoy reaching out to partners and building MISA's network.",
    "Office of the Executive Treasurer": "You might enjoy planning budgets, working with suppliers, and keeping financial records clear.",
    "Events": "You might enjoy planning programs, preparing logistics, and running dry runs.",
    "eServices": "You might enjoy building websites and IT solutions, documenting systems, or helping others use technology.",
    "Human Resources": "You might enjoy supporting members through community activities, mentorship, and wellbeing work.",
}

QUESTIONS = [
    {
        "prompt": "Your group has an idea for a campus event. What do you pick up first?",
        "choices": {
            "a": {"text": "Sketch a small app that would help people sign up.", "clusters": ["eServices"]},
            "b": {"text": "Work on the poster and a pitch for possible partners.", "clusters": ["Communications", "Marketing"]},
            "c": {"text": "Put the schedule and room requirements in one document.", "clusters": ["Events", "Office of the Secretary General"]},
            "d": {"text": "Plan a member activity and check what the group can afford.", "clusters": ["Human Resources", "Office of the Executive Treasurer"]},
        },
    },
    {
        "prompt": "A new person joins your project group. How would you help?",
        "choices": {
            "a": {"text": "Check in with them and introduce them to the team.", "clusters": ["Human Resources"]},
            "b": {"text": "Walk them through the event plan using a visual guide.", "clusters": ["Communications", "Events"]},
            "c": {"text": "Show them the project files and help them use the team's tools.", "clusters": ["Office of the Secretary General", "eServices"]},
            "d": {"text": "Explain our partner commitments and the budget behind them.", "clusters": ["Marketing", "Office of the Executive Treasurer"]},
        },
    },
    {
        "prompt": "You have a free afternoon to work on something for MISA. What sounds good?",
        "choices": {
            "a": {"text": "Make a spending tracker so the numbers are easy to check.", "clusters": ["Office of the Executive Treasurer"]},
            "b": {"text": "Design a screen and try building it into a working page.", "clusters": ["Communications", "eServices"]},
            "c": {"text": "Tidy up the team guide so new members can use it.", "clusters": ["Office of the Secretary General", "Human Resources"]},
            "d": {"text": "Talk to a possible partner about an event idea.", "clusters": ["Marketing", "Events"]},
        },
    },
    {
        "prompt": "Your group chat has four requests. Which would you volunteer for?",
        "choices": {
            "a": {"text": "Work out the order of activities for our event.", "clusters": ["Events"]},
            "b": {"text": "Turn scattered notes into a clear, readable project guide.", "clusters": ["Communications", "Office of the Secretary General"]},
            "c": {"text": "Welcome partner guests and help them meet our members.", "clusters": ["Marketing", "Human Resources"]},
            "d": {"text": "Build a simple tool for checking project expenses.", "clusters": ["Office of the Executive Treasurer", "eServices"]},
        },
    },
    {
        "prompt": "What would you most like to have finished by the end of a project?",
        "choices": {
            "a": {"text": "A photo story or video that I'm proud to show people.", "clusters": ["Communications"]},
            "b": {"text": "An organized record of the work and where the money went.", "clusters": ["Office of the Secretary General", "Office of the Executive Treasurer"]},
            "c": {"text": "A useful product shaped by conversations with a partner.", "clusters": ["Marketing", "eServices"]},
            "d": {"text": "An activity where members had time to get to know each other.", "clusters": ["Events", "Human Resources"]},
        },
    },
    {
        "prompt": "The group wants to improve its next project. Which task interests you?",
        "choices": {
            "a": {"text": "Sort the feedback and decisions into a document people can find.", "clusters": ["Office of the Secretary General"]},
            "b": {"text": "Help members tell their stories through photos or short videos.", "clusters": ["Communications", "Human Resources"]},
            "c": {"text": "Find a partner who could help with the next event.", "clusters": ["Marketing", "Events"]},
            "d": {"text": "Automate a repetitive calculation in the expense tracker.", "clusters": ["Office of the Executive Treasurer", "eServices"]},
        },
    },
    {
        "prompt": "You can try one role on a small practice project. Which do you choose?",
        "choices": {
            "a": {"text": "Contact possible partners and listen to their ideas.", "clusters": ["Marketing"]},
            "b": {"text": "Design a keepsake and work out the cost of producing it.", "clusters": ["Communications", "Office of the Executive Treasurer"]},
            "c": {"text": "Keep the activity schedule and logistics notes up to date.", "clusters": ["Office of the Secretary General", "Events"]},
            "d": {"text": "Build a tool that helps members find people with shared interests.", "clusters": ["eServices", "Human Resources"]},
        },
    },
]
