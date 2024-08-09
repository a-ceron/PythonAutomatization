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