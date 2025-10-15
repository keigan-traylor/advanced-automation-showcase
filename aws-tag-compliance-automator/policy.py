# policy.py - Compliance rules and remediation helper (simulated)
REQUIRED_TAGS = ['Owner','Project','Environment']

def evaluate_resource(resource):
    """Return a tuple (missing_tags, present_tags)"""
    tags = resource.get('tags') or {}
    present = [k for k in REQUIRED_TAGS if k in tags]
    missing = [k for k in REQUIRED_TAGS if k not in tags]
    return missing, present

def remediation_actions(resource, missing):
    """Return a list of simulated remediation actions (YAML-playbook style)"""
    actions = []
    identifier = resource.get('id') or resource.get('name')
    for tag in missing:
        actions.append({'action':'add_tag','resource':identifier,'tag':tag,'value':'<TBD>'})
    # Suggest stopping non-critical instances without Owner
    if resource.get('state') == 'running' and 'Owner' in missing:
        actions.append({'action':'stop_instance','resource':identifier,'reason':'no-owner-tag'})
    return actions
