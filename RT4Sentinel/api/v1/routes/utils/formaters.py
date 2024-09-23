"""
    alarms.py:
    Recibe señales de servicios externos para ejecutar pipelines de alertas.


    ---------------------------------------------------
    copyrigth 2024-2025
    Autor: @a-ceron
    v1.0
    ---------------------------------------------------

    Última modificación: Agosto 2024
"""

from . import pingplotter as pp

def get_ticket_from_pingplotter(body: dict, agent: dict)->dict:
    """
    This function formats the body of a pingplotter alarm and returns a ticket.
    """
    return {
        "name": body.get('alert').get('name'),
        "description": pp.get_ticket_description(
            body.get('alert').get('name'), 
            body.get('timestamps').get('utc_time'), 
            body.get('host').get('full_display_name')),
        "level": pp.get_str_level(body.get('alert').get('name')),
        "hostname": body.get('host').get('dns_name'),
        "agent_id": agent.id
    }

def get_msg_from_pingplotter(ticket:object)->dict:
    """
    This function formats the body of a pingplotter alarm and returns a message.
    """
    return {
        "name": ticket.get('name'),
        "description": ticket.get('description'),
        "level": pp.pingplotter.get('levels').get(ticket.get('level')),
        "hostname": ticket.get('hostname'),
    }