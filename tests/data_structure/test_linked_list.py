from tests.testcases import TestCase
from data_structure.linked_lists import LinkedList


class TestLinkedList(TestCase):

    def test_linked_list(self):
        # 初始化链表并判断长度是否正确
        linked_list1 = LinkedList()
        self.assertEqual(len(linked_list1), 0)
        linked_list2 = LinkedList([1, 2, 3])
        self.assertEqual(len(linked_list2), 3)
        linked_list3 = LinkedList(range(100))
        self.assertEqual(len(linked_list3), 100)

        # 判断是否能按照索引的方式访问元素
        self.assertEqual(linked_list3[0], 0)
        self.assertEqual(linked_list3[66], 66)
        self.assertEqual(linked_list3[-1], 99)
        self.assertEqual(linked_list3[-66], 34)

        # 判断访问元素时索引错误能否抛出对应的异常
        self.assertRaisesRegexpForIndexType(linked_list2.__getitem__, 'a')
        self.assertRaisesRegexpForIndexRange(linked_list2.__getitem__, 3)
        self.assertRaisesRegexpForIndexRange(linked_list2.__getitem__, -4)

        # 判断是否能按索引的方式修改元素
        linked_list3[0] = 'hello'
        self.assertEqual(linked_list3[0], 'hello')
        linked_list3[66] = '666'
        self.assertEqual(linked_list3[66], '666')
        linked_list3[-1] = '99'
        self.assertEqual(linked_list3[-1], '99')
        linked_list3[-66] = '34'
        self.assertEqual(linked_list3[-66], '34')

        # 判断修改元素时索引错误能否抛出对应的异常
        self.assertRaisesRegexpForIndexType(linked_list2.__setitem__, 'a', 'value')
        self.assertRaisesRegexpForIndexRange(linked_list2.__setitem__, 3, 'value')
        self.assertRaisesRegexpForIndexRange(linked_list2.__setitem__, -4, 'value')

        # 判断对象的描述信息是否正确
        self.assertEqual(linked_list1.__str__(), '【head】')
        self.assertEqual(linked_list2.__str__(), '【head】->【1】->【2】->【3】')

        # 测试方法 append
        linked_list2.append(4)
        self.assertEqual(len(linked_list2), 4)
        self.assertEqual(linked_list2[3], 4)
        self.assertEqual(linked_list2.__str__(), '【head】->【1】->【2】->【3】->【4】')
        linked_list2.append('jiangpancjy')
        self.assertEqual(len(linked_list2), 5)
        self.assertEqual(linked_list2[4], 'jiangpancjy')
        self.assertEqual(linked_list2.__str__(), '【head】->【1】->【2】->【3】->【4】->【jiangpancjy】')

        # 判断插入元素时索引错误能否抛出对应的异常
        linked_list2 = LinkedList([1, 2, 3])
        self.assertRaisesRegexpForIndexType(linked_list2.insert, 'a', 'value')
        self.assertRaisesRegexpForIndexRange(linked_list2.insert, 4, 'value')
        self.assertRaisesRegexpForIndexRange(linked_list2.insert, -5, 'value')

        # 测试方法 insert
        linked_list2.insert(3, 4)
        self.assertEqual(linked_list2[3], 4)
        self.assertEqual(len(linked_list2), 4)
        self.assertEqual(linked_list2.__str__(), '【head】->【1】->【2】->【3】->【4】')
        linked_list2.insert(0, 0)
        self.assertEqual(linked_list2[0], 0)
        self.assertEqual(len(linked_list2), 5)
        self.assertEqual(linked_list2.__str__(), '【head】->【0】->【1】->【2】->【3】->【4】')
        linked_list2.insert(1, 0.5)
        self.assertEqual(linked_list2[1], 0.5)
        self.assertEqual(len(linked_list2), 6)
        self.assertEqual(linked_list2.__str__(), '【head】->【0】->【0.5】->【1】->【2】->【3】->【4】')
        linked_list2.insert(-1, 3.5)
        self.assertEqual(linked_list2[-2], 3.5)
        self.assertEqual(len(linked_list2), 7)
        self.assertEqual(linked_list2.__str__(), '【head】->【0】->【0.5】->【1】->【2】->【3】->【3.5】->【4】')
        linked_list2.insert(-8, -1)
        self.assertEqual(linked_list2[-8], -1)
        self.assertEqual(len(linked_list2), 8)
        self.assertEqual(linked_list2.__str__(), '【head】->【-1】->【0】->【0.5】->【1】->【2】->【3】->【3.5】->【4】')
