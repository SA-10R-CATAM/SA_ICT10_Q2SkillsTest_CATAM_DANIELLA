from pyscript import display, document

# Define club information using dictionaries
club_info = {
            "photo": {
                "name": "Photography Club 𝜗𝜚⋆₊˚",
                "description": "A club for photography enthusiasts of all skill levels. Take pictures for events",
                "meeting_time": "Every Friday 2:30-4:00 PM",
                "location": "Room 777",
                "advisor": "Ms. Valenzuela",
                "members": 12,
                "category": "Arts"
            },
            "drama": {
                "name": "Drama Club 𐙚⋆.˚",
                "description": "For students interested in theater, acting, and stage production.",
                "meeting_time": "Every Monday and Thursday 4:00-6:00 PM",
                "location": "MM Hall",
                "advisor": "Ms. Evangelista",
                "members": 22,
                "category": "Arts"
            },
            "dance": {
                "name": "Dance Club ⋆౨ৎ˚⟡˖ ࣪",
                "description": "Also known as Radiance, dance, learn, have fun and perform.",
                "meeting_time": "Every Thursday 3:00-5:00 PM",
                "location": "Room 220",
                "advisor": "Mr. Sumaoang",
                "members": 14,
                "category": "Non-Academic"
            },
            "music": {
                "name": "Music Club ೀ",
                "description": "Also known as Glee, sing, learn, perform.",
                "meeting_time": "Every Wednesday and Thursday 3:30-4:30 PM",
                "location": "Music Room",
                "advisor": "Ms. Llanes",
                "members": 32,
                "category": "music"
            },
            "art": {
                "name": "Art Club ⋆˚𝜗𝜚˚⋆",
                "description": "Explore various art mediums and techniques.",
                "meeting_time": "Every Wednesday 3:45-5:15 PM",
                "location": "Art Room",
                "advisor": "Mr. Balajadia",
                "members": 20,
                "category": "Arts"
            },
            "": {
                "name": "",
                "description": "",
                "meeting_time": "",
                "location": "",
                "advisor": "",
                "members": "",
                "category": ""
            }
        }
        
def show_club_info(e):
    document.getElementById('club-info').innerHTML = " "
    selected_club = document.getElementById("club-select").value
    info = club_info.get(selected_club, club_info[""])
            
    output = f"""
            {info['name']}
            Description:{info['description']}
            Meeting Time: {info['meeting_time']}
            Location: {info['location']}
            Advisor: {info['advisor']}
            Number of Members: {info['members']}
            Category: {info['category']}
            """
    display(output, target="club-info")