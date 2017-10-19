import requests
import json


class OctopusDeploy:

    def __init__(self, octopus_url, api_key):
        """
        :param octopus_url:
        :param api_key:

        """
        self.octopus_url = octopus_url
        self._validate_url()
        self.api_key = {'ApiKey': api_key}

    def _valid_status_code(self, result, error_msg):
        if not result.status_code:
            raise Exception(error_msg)

    def _validate_url(self):
        result = requests.get(self.octopus_url)
        self._valid_status_code(
            result, 'Unable to reach {0}\nPlease check if server is available '.format(self.octopus_url))

    def list_projects(self):
        """
        List All Projects in Octopus Server
        """
        projects = []
        Page = '/api/projects?skip=0'
        while(Page):
            api_url = self.octopus_url + Page
            result = requests.get(api_url, params=self.api_key)
            self._valid_status_code(
                result, 'Failed to list projects; error: {0}'.format(result.text))
            Items = json.loads(result.content)['Items']
            if('Page.Next' in json.loads(result.content)['Links']):
                Page = json.loads(result.content)['Links']['Page.Next']
            else:
                Page = ""

            for item in Items:
                projects.append((item['Id'],
                                 item['Name'], item['ProjectGroupId']))
        return projects

    def list_machines(self):
        """
        List All machines in Octopus Server
        """
        machines = []
        Page = '/api/machines?skip=0'
        while(Page):
            api_url = self.octopus_url + Page
            result = requests.get(api_url, params=self.api_key)
            self._valid_status_code(
                result, 'Failed to list machines; error: {0}'.format(result.text))
            Items = json.loads(result.content)['Items']
            if('Page.Next' in json.loads(result.content)['Links']):
                Page = json.loads(result.content)['Links']['Page.Next']
            else:
                Page = ""

            for item in Items:
                machines.append((item['Id'], item['Status'],
                                 item['Name'], item['EnvironmentIds']))
        return machines

    def list_releases(self):
        """
        List All releases in Octopus Server
        """
        releases = []
        Page = '/api/releases?skip=0'
        while(Page):
            api_url = self.octopus_url + Page
            result = requests.get(api_url, params=self.api_key)
            self._valid_status_code(
                result, 'Failed to list releases; error: {0}'.format(result.text))
            Items = json.loads(result.content)['Items']
            if('Page.Next' in json.loads(result.content)['Links']):
                Page = json.loads(result.content)['Links']['Page.Next']
            else:
                Page = ""

            for item in Items:
                releases.append((item['Id'], item['ProjectId'],
                                 item['ChannelId'], item['Version']))
        return releases

    def list_latestdeployments(self):
        """
        List Latest Deloyments in Octopus Server
        """
        latestdeployments = []
        Page = '/api/deployments?skip=0'
        while(Page):
            api_url = self.octopus_url + Page
            result = requests.get(api_url, params=self.api_key)
            self._valid_status_code(
                result, 'Failed to list Latest Deloyments; error: {0}'.format(result.text))
            Items = json.loads(result.content)['Items']
            if('Page.Next' in json.loads(result.content)['Links']):
                Page = json.loads(result.content)['Links']['Page.Next']
            else:
                Page = ""

            for item in Items:
                latestdeployments.append((item['Id'], item['EnvironmentId'],
                                          item['ProjectId'], item['Name'], item['Created']))

        return latestdeployments
