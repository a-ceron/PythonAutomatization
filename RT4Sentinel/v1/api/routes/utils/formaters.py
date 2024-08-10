from . import pingplotter as pp

def get_ticket_from_pingplotter(body: dict, agent: dict)->dict:
    """
    This function formats the body of a pingplotter alarm and returns a ticket.
    """
    return {
        "name": body.get('alert').get('name'),
        "description": body.get('timestamps').get('utc_time'),
        "level": 1,
        "hostname": body.get('host').get('full_display_name'),
        "agent_id": agent.id
    }

def get_msg_from_pingplotter(body: dict, ticket:object)->dict:
    """
    This function formats the body of a pingplotter alarm and returns a message.
    """
    print("Creating message...")
    print(body)
    name = body.get('alert').get('name')
    print(name)
    time = body.get('timestamps').get('utc_time')
    print(time)
    ip = body.get('host').get('ip_address')
    print(ip)
    print("Message created!")

    return {
        "name": name,
        "description": pp.get_content_msg(ticket.id, name, time, ip),
        "level": pp.get_level_of_urgency(name),
        "hostname": body.get('host').get('full_display_name')
    }