# Each choice gives one point to every cluster in its list.
CLUSTERS = {
    "COMMS": "You might enjoy designing visuals, taking photos, or editing videos for MISA.",
    "OSG": "You might enjoy organizing documents and keeping project operations in order.",
    "MKT": "You might enjoy reaching out to partners and building MISA's network.",
    "OET": "You might enjoy planning budgets and keeping track of project finances.",
    "Events": "You might enjoy planning programs and sorting out event logistics.",
    "eServs": "You might enjoy designing and building IT solutions for clients.",
    "HR": "You might enjoy helping members get to know each other and feel included.",
}

QUESTIONS = [
    {
        "prompt": "Your group has an idea for a campus event. What do you pick up first?",
        "choices": {
            "a": {"text": "Sketch a small app that would help people sign up.", "clusters": ["eServs"]},
            "b": {"text": "Work on the poster and a pitch for possible partners.", "clusters": ["COMMS", "MKT"]},
            "c": {"text": "Put the schedule and room requirements in one document.", "clusters": ["Events", "OSG"]},
            "d": {"text": "Plan a member activity and check what the group can afford.", "clusters": ["HR", "OET"]},
        },
    },
    {
        "prompt": "A new person joins your project group. How would you help?",
        "choices": {
            "a": {"text": "Check in with them and introduce them to the team.", "clusters": ["HR"]},
            "b": {"text": "Walk them through the event plan using a visual guide.", "clusters": ["COMMS", "Events"]},
            "c": {"text": "Show them the project files and help them use the team's tools.", "clusters": ["OSG", "eServs"]},
            "d": {"text": "Explain our partner commitments and the budget behind them.", "clusters": ["MKT", "OET"]},
        },
    },
    {
        "prompt": "You have a free afternoon to work on something for MISA. What sounds good?",
        "choices": {
            "a": {"text": "Make a spending tracker so the numbers are easy to check.", "clusters": ["OET"]},
            "b": {"text": "Design a screen and try building it into a working page.", "clusters": ["COMMS", "eServs"]},
            "c": {"text": "Tidy up the team guide so new members can use it.", "clusters": ["OSG", "HR"]},
            "d": {"text": "Talk to a possible partner about an event idea.", "clusters": ["MKT", "Events"]},
        },
    },
    {
        "prompt": "Your group chat has four requests. Which would you volunteer for?",
        "choices": {
            "a": {"text": "Work out the order of activities for our event.", "clusters": ["Events"]},
            "b": {"text": "Turn scattered notes into a clear, readable project guide.", "clusters": ["COMMS", "OSG"]},
            "c": {"text": "Welcome guests and help them meet our members.", "clusters": ["MKT", "HR"]},
            "d": {"text": "Build a simple tool for checking project expenses.", "clusters": ["OET", "eServs"]},
        },
    },
    {
        "prompt": "What would you most like to have finished by the end of a project?",
        "choices": {
            "a": {"text": "A photo story or video that I'm proud to show people.", "clusters": ["COMMS"]},
            "b": {"text": "An organized record of the work and where the money went.", "clusters": ["OSG", "OET"]},
            "c": {"text": "A useful product shaped by conversations with a partner.", "clusters": ["MKT", "eServs"]},
            "d": {"text": "An activity where members had time to get to know each other.", "clusters": ["Events", "HR"]},
        },
    },
    {
        "prompt": "The group wants to improve its next project. Which task interests you?",
        "choices": {
            "a": {"text": "Sort the feedback and decisions into a document people can find.", "clusters": ["OSG"]},
            "b": {"text": "Help members tell their stories through photos or short videos.", "clusters": ["COMMS", "HR"]},
            "c": {"text": "Find a partner who could help with the next event.", "clusters": ["MKT", "Events"]},
            "d": {"text": "Automate a repetitive calculation in the expense tracker.", "clusters": ["OET", "eServs"]},
        },
    },
    {
        "prompt": "You can try one role on a small practice project. Which do you choose?",
        "choices": {
            "a": {"text": "Contact possible partners and listen to their ideas.", "clusters": ["MKT"]},
            "b": {"text": "Design a keepsake and work out the cost of producing it.", "clusters": ["COMMS", "OET"]},
            "c": {"text": "Keep the activity schedule and logistics notes up to date.", "clusters": ["OSG", "Events"]},
            "d": {"text": "Build a tool that helps members find people with shared interests.", "clusters": ["eServs", "HR"]},
        },
    },
]
