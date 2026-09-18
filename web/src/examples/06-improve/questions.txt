# Every choice awards 2 points to its closest match and 1 point to a related cluster.
CLUSTERS = {
    "Communications": "You may enjoy shaping MISA's visual identity through branding, promotions, photography, video, and event creatives.",
    "Office of the Secretary General": "You may enjoy keeping projects organized through documentation, schedules, attendance, evaluations, and deadline tracking.",
    "Marketing": "You may enjoy building relationships with companies, organizations, and alumni while keeping partner commitments on track.",
    "Office of the Executive Treasurer": "You may enjoy planning budgets, working with suppliers, tracking transactions, and keeping financial records clear.",
    "Events": "You may enjoy turning ideas into events through program planning, logistics, contingency plans, and dry runs.",
    "eServices": "You may enjoy building websites and IT solutions, improving UI and UX, documenting systems, or helping others use technology.",
    "Human Resources": "You may enjoy supporting members through community activities, mentorship, wellbeing work, and one-on-one conversations.",
}

QUESTIONS = [
    {
        "prompt": "Your group has an idea for a campus event. What do you pick up first?",
        "choices": {
            "a": {
                "text": "Create the event look and a welcome post for members.",
                "points": {
                    "Communications": 2,
                    "Human Resources": 1
                }
            },
            "b": {
                "text": "Set up the schedule, venue checklist, and project files.",
                "points": {
                    "Office of the Secretary General": 2,
                    "Events": 1
                }
            },
            "c": {
                "text": "Pitch a useful event tool to a possible partner.",
                "points": {
                    "Marketing": 2,
                    "eServices": 1
                }
            },
            "d": {
                "text": "Plan a member activity that fits the available budget.",
                "points": {
                    "Office of the Executive Treasurer": 2,
                    "Human Resources": 1
                }
            },
        },
    },
    {
        "prompt": "A new person joins your project group. How would you help?",
        "choices": {
            "a": {
                "text": "Walk them through the event plan and registration tool.",
                "points": {
                    "Events": 2,
                    "eServices": 1
                }
            },
            "b": {
                "text": "Help them access the team's tools and check how they are doing.",
                "points": {
                    "eServices": 2,
                    "Human Resources": 1
                }
            },
            "c": {
                "text": "Introduce them to everyone and make a friendly welcome card.",
                "points": {
                    "Human Resources": 2,
                    "Communications": 1
                }
            },
            "d": {
                "text": "Turn the project guide into a clear visual checklist.",
                "points": {
                    "Communications": 2,
                    "Office of the Secretary General": 1
                }
            },
        },
    },
    {
        "prompt": "You have a free afternoon for a MISA project. What sounds good?",
        "choices": {
            "a": {
                "text": "Organize partner records so the next follow-up is easy to find.",
                "points": {
                    "Office of the Secretary General": 2,
                    "Marketing": 1
                }
            },
            "b": {
                "text": "Talk to a possible sponsor and map out what both sides can provide.",
                "points": {
                    "Marketing": 2,
                    "Office of the Executive Treasurer": 1
                }
            },
            "c": {
                "text": "Build a spending tracker for an upcoming event.",
                "points": {
                    "Office of the Executive Treasurer": 2,
                    "Events": 1
                }
            },
            "d": {
                "text": "Test the event flow and improve its signup page.",
                "points": {
                    "Events": 2,
                    "eServices": 1
                }
            },
        },
    },
    {
        "prompt": "Something changes on the morning of an event. Where do you jump in?",
        "choices": {
            "a": {
                "text": "Fix the check-in tool and help volunteers use it.",
                "points": {
                    "eServices": 2,
                    "Human Resources": 1
                }
            },
            "b": {
                "text": "Check on the team and prepare a quick update for attendees.",
                "points": {
                    "Human Resources": 2,
                    "Communications": 1
                }
            },
            "c": {
                "text": "Revise the announcement and keep the project notes accurate.",
                "points": {
                    "Communications": 2,
                    "Office of the Secretary General": 1
                }
            },
            "d": {
                "text": "Record the decision and tell partners what changed.",
                "points": {
                    "Office of the Secretary General": 2,
                    "Marketing": 1
                }
            },
        },
    },
    {
        "prompt": "Which finished project result would make you happiest?",
        "choices": {
            "a": {
                "text": "A partner relationship with clear commitments and costs.",
                "points": {
                    "Marketing": 2,
                    "Office of the Executive Treasurer": 1
                }
            },
            "b": {
                "text": "An event that stayed useful without going over budget.",
                "points": {
                    "Office of the Executive Treasurer": 2,
                    "Events": 1
                }
            },
            "c": {
                "text": "A smooth program supported by a tool people actually used.",
                "points": {
                    "Events": 2,
                    "eServices": 1
                }
            },
            "d": {
                "text": "A member tool that made someone feel supported.",
                "points": {
                    "eServices": 2,
                    "Human Resources": 1
                }
            },
        },
    },
    {
        "prompt": "Which message are you most likely to send in the project group chat?",
        "choices": {
            "a": {
                "text": "How is everyone holding up? I can also make the update card.",
                "points": {
                    "Human Resources": 2,
                    "Communications": 1
                }
            },
            "b": {
                "text": "I cleaned up the poster and put the final files in the right folder.",
                "points": {
                    "Communications": 2,
                    "Office of the Secretary General": 1
                }
            },
            "c": {
                "text": "I updated the tracker and noted which partner needs a reply.",
                "points": {
                    "Office of the Secretary General": 2,
                    "Marketing": 1
                }
            },
            "d": {
                "text": "The sponsor replied, and I checked the cost of their request.",
                "points": {
                    "Marketing": 2,
                    "Office of the Executive Treasurer": 1
                }
            },
        },
    },
    {
        "prompt": "MISA is preparing a booth for an organization fair. What would you own?",
        "choices": {
            "a": {
                "text": "Price the materials and keep the setup within budget.",
                "points": {
                    "Office of the Executive Treasurer": 2,
                    "Events": 1
                }
            },
            "b": {
                "text": "Plan the booth flow and test the interactive screen.",
                "points": {
                    "Events": 2,
                    "eServices": 1
                }
            },
            "c": {
                "text": "Build the signup form and help members use it confidently.",
                "points": {
                    "eServices": 2,
                    "Human Resources": 1
                }
            },
            "d": {
                "text": "Welcome visitors and capture photos of the team in action.",
                "points": {
                    "Human Resources": 2,
                    "Communications": 1
                }
            },
        },
    },
    {
        "prompt": "For a digital-literacy workshop with public-school students, what would you prepare?",
        "choices": {
            "a": {
                "text": "A friendly visual guide and an organized set of activity files.",
                "points": {
                    "Communications": 2,
                    "Office of the Secretary General": 1
                }
            },
            "b": {
                "text": "The attendance records and partner coordination notes.",
                "points": {
                    "Office of the Secretary General": 2,
                    "Marketing": 1
                }
            },
            "c": {
                "text": "The school partnership plan and the cost of workshop materials.",
                "points": {
                    "Marketing": 2,
                    "Office of the Executive Treasurer": 1
                }
            },
            "d": {
                "text": "The materials budget and the room setup checklist.",
                "points": {
                    "Office of the Executive Treasurer": 2,
                    "Events": 1
                }
            },
        },
    },
    {
        "prompt": "The plan changes at the last minute. What feels most natural?",
        "choices": {
            "a": {
                "text": "Adjust the program flow and check whether the event tools still work.",
                "points": {
                    "Events": 2,
                    "eServices": 1
                }
            },
            "b": {
                "text": "Update the shared system and make sure no teammate is left confused.",
                "points": {
                    "eServices": 2,
                    "Human Resources": 1
                }
            },
            "c": {
                "text": "Check on the team and rewrite the announcement in a calm tone.",
                "points": {
                    "Human Resources": 2,
                    "Communications": 1
                }
            },
            "d": {
                "text": "Fix the public update and document the new decision.",
                "points": {
                    "Communications": 2,
                    "Office of the Secretary General": 1
                }
            },
        },
    },
    {
        "prompt": "At a networking night, which task would you choose?",
        "choices": {
            "a": {
                "text": "Keep the guest list and partner details accurate.",
                "points": {
                    "Office of the Secretary General": 2,
                    "Marketing": 1
                }
            },
            "b": {
                "text": "Welcome company and alumni guests and track any commitments.",
                "points": {
                    "Marketing": 2,
                    "Office of the Executive Treasurer": 1
                }
            },
            "c": {
                "text": "Handle supplier payments and support the venue setup.",
                "points": {
                    "Office of the Executive Treasurer": 2,
                    "Events": 1
                }
            },
            "d": {
                "text": "Run the program and make sure the check-in system behaves.",
                "points": {
                    "Events": 2,
                    "eServices": 1
                }
            },
        },
    },
    {
        "prompt": "The team wants to learn from its last project. Which part interests you?",
        "choices": {
            "a": {
                "text": "Turn the feedback into a simple tool and help members read it.",
                "points": {
                    "eServices": 2,
                    "Human Resources": 1
                }
            },
            "b": {
                "text": "Ask how people felt and share their stories carefully.",
                "points": {
                    "Human Resources": 2,
                    "Communications": 1
                }
            },
            "c": {
                "text": "Design the report and keep its files easy to trace.",
                "points": {
                    "Communications": 2,
                    "Office of the Secretary General": 1
                }
            },
            "d": {
                "text": "Summarize the evaluation and prepare useful notes for partners.",
                "points": {
                    "Office of the Secretary General": 2,
                    "Marketing": 1
                }
            },
        },
    },
    {
        "prompt": "You are helping with a leadership bootcamp. What do you volunteer for?",
        "choices": {
            "a": {
                "text": "Invite a speaker and make sure the agreement fits the budget.",
                "points": {
                    "Marketing": 2,
                    "Office of the Executive Treasurer": 1
                }
            },
            "b": {
                "text": "Plan the spending and prepare the rooms and materials.",
                "points": {
                    "Office of the Executive Treasurer": 2,
                    "Events": 1
                }
            },
            "c": {
                "text": "Shape the program and test the activity tools before the session.",
                "points": {
                    "Events": 2,
                    "eServices": 1
                }
            },
            "d": {
                "text": "Set up the workshop system and support participants who need help.",
                "points": {
                    "eServices": 2,
                    "Human Resources": 1
                }
            },
        },
    },
    {
        "prompt": "What would we usually find open on your laptop during a project?",
        "choices": {
            "a": {
                "text": "A team check-in note beside a half-finished welcome graphic.",
                "points": {
                    "Human Resources": 2,
                    "Communications": 1
                }
            },
            "b": {
                "text": "A design file beside a very organized project folder.",
                "points": {
                    "Communications": 2,
                    "Office of the Secretary General": 1
                }
            },
            "c": {
                "text": "A project tracker beside a draft message to a partner.",
                "points": {
                    "Office of the Secretary General": 2,
                    "Marketing": 1
                }
            },
            "d": {
                "text": "A partner proposal beside a sheet of estimated costs.",
                "points": {
                    "Marketing": 2,
                    "Office of the Executive Treasurer": 1
                }
            },
        },
    },
    {
        "prompt": "MISA is planning its year-end celebration. Which job sounds best?",
        "choices": {
            "a": {
                "text": "Track the budget while helping the setup stay on schedule.",
                "points": {
                    "Office of the Executive Treasurer": 2,
                    "Events": 1
                }
            },
            "b": {
                "text": "Plan the program and prepare the system for awards or signups.",
                "points": {
                    "Events": 2,
                    "eServices": 1
                }
            },
            "c": {
                "text": "Build the event page and make it easy for members to get help.",
                "points": {
                    "eServices": 2,
                    "Human Resources": 1
                }
            },
            "d": {
                "text": "Plan a warm member moment and capture it through photos or video.",
                "points": {
                    "Human Resources": 2,
                    "Communications": 1
                }
            },
        },
    },
    {
        "prompt": "You can try one role on a small practice project. Which do you choose?",
        "choices": {
            "a": {
                "text": "Create the project's visual style and organize the final assets.",
                "points": {
                    "Communications": 2,
                    "Office of the Secretary General": 1
                }
            },
            "b": {
                "text": "Keep the project records and coordinate one partner follow-up.",
                "points": {
                    "Office of the Secretary General": 2,
                    "Marketing": 1
                }
            },
            "c": {
                "text": "Talk with a possible partner and prepare a realistic budget.",
                "points": {
                    "Marketing": 2,
                    "Office of the Executive Treasurer": 1
                }
            },
            "d": {
                "text": "Track the expenses and help run the activity itself.",
                "points": {
                    "Office of the Executive Treasurer": 2,
                    "Events": 1
                }
            },
        },
    },
]
