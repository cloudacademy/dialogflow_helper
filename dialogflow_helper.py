#!/usr/bin/env python
import os
import dialogflow_v2

def teardown():
    dh = dialogflow_helper(os.environ.get("GCP_PROJECT"))
    dh.delete_agent()

class dialogflow_helper:
    def __init__(self, project):
        self.client = dialogflow_v2.AgentsClient()
        self.project = project

    def set_agent(self):
        agent = {
            "parent": f"projects/{self.project}",
            "display_name": "ca-lab-agent",
            "default_language_code": "en",
            "time_zone": "America/Los_Angeles",
            "enable_logging": True,
            "match_mode": "MATCH_MODE_HYBRID",
            "classification_threshold": 0.3,
            "api_version": "API_VERSION_V2",
            "tier": "TIER_STANDARD"
        }

        response = self.client.set_agent(agent)

    def get_agent(self):
        parent = self.client.project_path(self.project)
        agent = self.client.get_agent(parent)
        print(agent)
        return agent

    def delete_agent(self):
        self.client.delete_agent(f"projects/{self.project}")


if __name__ == "__main__":
    dialogflow_helper = dialogflow_helper(os.environ.get("GCP_PROJECT"))
    dialogflow_helper.set_agent()
    dialogflow_helper.get_agent()
