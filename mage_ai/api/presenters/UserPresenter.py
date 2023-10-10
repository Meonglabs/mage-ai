from mage_ai.api.operations import constants
from mage_ai.api.presenters.BasePresenter import BasePresenter
from mage_ai.shared.hash import extract


class UserPresenter(BasePresenter):
    default_attributes = [
        'avatar',
        'created_at',
        'email',
        'first_name',
        'id',
        'last_name',
        'owner',
        'project_access',
        'roles',
        'roles_display',
        'roles_new',
        'updated_at',
        'username',
    ]

    async def prepare_present(self, **kwargs):
        data = self.model.to_dict(include_attributes=self.default_attributes)
        data = extract(data, self.default_attributes, include_blank_values=True)

        roles_new = self.model.roles_new
        data['roles_new'] = [
            role.to_dict(include_attributes=['permissions'])
            for role in roles_new
        ]

        return data


UserPresenter.register_format(
    constants.CREATE, UserPresenter.default_attributes + ['token', ])


UserPresenter.register_formats([
    f'permission/{constants.DETAIL}',
    f'role/{constants.DETAIL}',
    f'role/{constants.LIST}',
], [
    'first_name',
    'id',
    'last_name',
    'username',
])
