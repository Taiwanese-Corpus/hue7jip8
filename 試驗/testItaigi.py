from django.test.testcases import TestCase
from 臺灣言語服務.models import 訓練過渡格式
from django.core.management import call_command


class itaigi試驗(TestCase):
    @classmethod
    def setUpClass(cls):
        call_command('itaigi')
        return super().setUpClass()

    def test句數正確(self):
        self.assertGreater(訓練過渡格式.資料數量(), 8000)

    def test無教典(self):
        self.assertFalse(
            訓練過渡格式.objects.filter(外文='漂-亮', 文本='媠｜suí').exists()
        )

    def test無台華(self):
        self.assertFalse(
            訓練過渡格式.objects.filter(外文='跑-步', 文本='走｜tsáu').exists()
        )
