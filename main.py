class Content:
    def __init__(self, text, version=None, version_dict=None, inspiration=None, concerns=None, error=None):
        self._text = text
        self.version = version or 1
        self.version_dict = version_dict or {}
        self.inspiration = inspiration
        self.concerns = concerns
        self.error = error

        # Save the initial version of the text
        self.version_dict[self.version] = self._text

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, new_text):
        if new_text != self._text:
            self.version += 1
            self.version_dict[self.version] = new_text
            self._text = new_text

    def get_version(self, version_number):
        return self.version_dict.get(version_number, "Version not found")


class ClientSide:
    def __init__(self, ui_layout_description, ui_user_interaction_details, client_action,
                 action_consequences_visual, action_consequences_internal_data, api_call):
        self.ui_layout_description = ui_layout_description
        self.ui_user_interaction_details = ui_user_interaction_details
        self.client_action = client_action
        self.action_consequences_visual = action_consequences_visual
        self.action_consequences_internal_data = action_consequences_internal_data
        self.api_call = api_call


class BackendSide:
    def __init__(self, api_package_receive_logic, api_data_auth_sanity_check_logic, api_package_preprocessing_logic,
                 business_logic, response_preparation):
        self.api_package_receive_logic = api_package_receive_logic
        self.api_data_auth_sanity_check_logic = api_data_auth_sanity_check_logic
        self.api_package_preprocessing_logic = api_package_preprocessing_logic
        self.business_logic = business_logic
        self.response_preparation = response_preparation


class E2EI:
    def __init__(self, client_side, backend_side, concerns, requirements, prerequisites):
        self.client_side = client_side
        self.backend_side = backend_side
        self.concerns = concerns
        self.requirements = requirements
        self.prerequisites = prerequisites


# Example usage:

# Creating Content instances for ClientSide
ui_layout_description = Content(text="Initial UI layout description")
ui_user_interaction_details = Content(text="Initial user interaction details")
client_action = Content(text="Initial client action")
action_consequences_visual = Content(text="Initial visual consequences")
action_consequences_internal_data = Content(text="Initial internal and data consequences")
api_call = Content(text="Initial API call details")

# Creating a ClientSide instance
client_side = ClientSide(
    ui_layout_description=ui_layout_description,
    ui_user_interaction_details=ui_user_interaction_details,
    client_action=client_action,
    action_consequences_visual=action_consequences_visual,
    action_consequences_internal_data=action_consequences_internal_data,
    api_call=api_call
)

# Creating Content instances for BackendSide
api_package_receive_logic = Content(text="Initial API package receive logic")
api_data_auth_sanity_check_logic = Content(text="Initial API data auth sanity check logic")
api_package_preprocessing_logic = Content(text="Initial API package preprocessing logic")
business_logic = Content(text="Initial business logic")
response_preparation = Content(text="Initial response preparation")

# Creating a BackendSide instance
backend_side = BackendSide(
    api_package_receive_logic=api_package_receive_logic,
    api_data_auth_sanity_check_logic=api_data_auth_sanity_check_logic,
    api_package_preprocessing_logic=api_package_preprocessing_logic,
    business_logic=business_logic,
    response_preparation=response_preparation
)

# Creating Content instances for concerns, requirements, and prerequisites
concerns = Content(text="Initial list of concerns")
requirements = Content(text="Initial list of requirements")
prerequisites = Content(text="Initial list of prerequisites")

# Creating an E2EI instance
e2e_interaction = E2EI(
    client_side=client_side,
    backend_side=backend_side,
    concerns=concerns,
    requirements=requirements,
    prerequisites=prerequisites
)

# Changing text in one of the Content instances
client_side.ui_layout_description.text = "Updated UI layout description"

# Printing the version history
print(client_side.ui_layout_description.version_dict)
# Output: {1: 'Initial UI layout description', 2: 'Updated UI layout description'}
