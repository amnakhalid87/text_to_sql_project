from src.custom_state import CustomState
def check_visualize(state:CustomState):
    if state['should_visualize'] :
        return 'Yes'
    else:
        return 'No'
    