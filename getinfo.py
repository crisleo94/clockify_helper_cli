from constants import API_KEY, API_URL
import json
import requests

basic_headers = {'x-api-key': API_KEY}

def get_user_info():
    user_response = json.loads(requests.get(f'{API_URL}/user', headers=basic_headers).text)

    current_user = {
        'id': user_response.get('id'),
        'name': user_response.get('name'),
        'email': user_response.get('email'),
        'activeWorkspace': user_response.get('activeWorkspace'),
        'timeZone': user_response.get('settings').get('timeZone'),
        'dateFormat': user_response.get('settings').get('dateFormat'),
        'project': get_project_info(user_response.get('activeWorkspace'))
    }
    
    return current_user


def get_project_info(current_workspace):
    projects = json.loads(requests.get(f'{API_URL}/workspaces/{current_workspace}/projects', headers=basic_headers).text)

    current_project = {
        'id': projects[0].get('id'),
        'name': projects[0].get('name'),
        'currency': projects[0].get('hourlyRate').get('currency'),
    }

    return current_project


def get_time_entries(current_workspace, current_user_id):
    time_entries_list = []
    
    time_entries = json.loads(requests.get(f'{API_URL}/workspaces/{current_workspace}/user/{current_user_id}/time-entries', headers=basic_headers).text)
    
    for time_entry in time_entries:
        new_time_entry = {
            'id': time_entry.get('id'),
            'description':time_entry.get('description'),
            'duration': time_entry.get('timeInterval').get('duration')
        }
        
        time_entries_list.append(new_time_entry)
    
    return time_entries_list


def add_new_entry_time(description, selected_date, current_workspace, projectId):
    try:
        new_entry = requests.post(
            f'{API_URL}/workspaces/{current_workspace}/time-entries',
            headers=basic_headers,
            json={
                'description': description,
                'projectId': projectId,
                'start': f'{selected_date}T15:00:00Z',
                'end': f'{selected_date}T23:00:00Z'
            }
        )
        
        if new_entry.status_code == 200 or new_entry.status_code == 201:
            print('New entry added to the timesheet')
        else:
            raise ValueError(f'Cannot create HTTP:{new_entry.text}')
        
        resp = json.loads(new_entry.text)
    except:
        raise ValueError('Cannot create a new time record!')
    
    return resp