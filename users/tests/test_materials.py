# from django.urls import reverse

from utils.test_bases import ProjectsTestBase


class MaterialsTest(ProjectsTestBase):
    def test_material_add_succesful(self):
        self.register_and_login()
        response = self.base_test_function(
            'users:dashboard',
            data=self.material_form_data,
            method='post',
        )
        msg = 'Material adicionado com sucesso!'

        self.assertIn(msg, response.content.decode('utf-8'))

    def test_delete_material_succesful(self):
        self.register_and_login()
        self.add_material()

        response = self.base_test_function(
            'users:delete_material',
            data={'material_id': 1},
            method='post',
        )
        msg = 'Material deletado com sucesso!'

        self.assertIn(msg, response.content.decode('utf-8'))

    def test_delete_material_receive_get_method(self):
        self.register_and_login()

        response = self.base_test_function('users:delete_material')

        self.assertEqual(response.status_code, 404)

    def test_material_deleted_not_found(self):
        self.register_and_login()

        response = self.base_test_function(
            'users:delete_material',
            data={'material_id': 1},
            method='post',
        )

        self.assertEqual(response.status_code, 404)

    def test_material_stock_change(self):
        self.register_and_login()
        material_stocked = self.add_material()
        material_empty = self.add_material(stocked=False)
        materials = [material_stocked, material_empty]

        for material in materials:
            response = self.base_test_function(
                'users:dashboard',
                method='post',
                data={'material-stock': material.id}
            )
            msg = f'O estoque de {material.material} foi'

            self.assertIn(msg, response.content.decode('utf-8'))
