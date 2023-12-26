import pytest
import os

pytest.main(['-sv', '--alluredir', './html', '--clean-alluredir'])
os.system(f'allure serve ./html')